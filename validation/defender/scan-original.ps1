# GRAAL Security & Trust 1.1: standard Defender scan, never runs a product.
# Run only on a disposable, updated Windows test machine. No settings changed.
[CmdletBinding()]
param(
  [Parameter(Mandatory)][string]$PackagePath,
  [Parameter(Mandatory)][string]$EvidencePath
)
$ErrorActionPreference = 'Stop'
$expected = @{
  'Genesis-Mini-v0.1.0-install.zip' = '654d46b77439a4c196bd6c70bda0fc664f1f59e8a6fe745cad76e10ed7fc67b4'
  'Argus-Mini-v0.1.0-install.zip' = '3248c6c204b5651a9f63c5630547e1a18f021a0ffdc08feaba1566e7925fb8b1'
  'Rubedo-Mini-v1.0.0-install.zip' = '1799dc6ccadd786eb960f38c4f7d67cf241e9630942a9e69daebfe96fcfe6ab2'
  'Rubedo-Mini-v0.3.0-install.zip' = 'ee1bcf4a225783dd60a332ba1720d14127c2c9b88f213ee8e29f4872bd12f1c8'
  'Aeris-Extension-v1.0.0-install.zip' = 'e77e6e8596c14e54f22303e7a5d368356c19eaa79df8c8597752790755d9a0d9'
  'Aeris-Extension-v1.0.0-completa.zip' = 'd0f064c1b73c46465171cc1fb208b530ed66573e054c2ca211b216547bbb3c00'
  'Lilium-Mini-0.1.1-experimental.zip' = '5fde935bfcd3bb3f2e1dda983b54a431b380f56c9ce85808608e17b89a524cf7'
  'Lilium-0.14.0-windows-x64-preview.zip' = '95ef0b0b96824b47c87e3784e8c9985796cefdfb76e1bea445b3e09ab0efe392'
}
function Read-Gate {
  $s = Get-MpComputerStatus
  $p = Get-MpPreference
  $age = if ($s.AntivirusSignatureLastUpdated) { ((Get-Date) - $s.AntivirusSignatureLastUpdated).TotalHours } else { $null }
  $counts = @(
    @($p.ExclusionPath | Where-Object { $_ }).Count
    @($p.ExclusionExtension | Where-Object { $_ }).Count
    @($p.ExclusionProcess | Where-Object { $_ }).Count
  )
  $ok = $s.AntivirusEnabled -eq $true -and $s.AMServiceEnabled -eq $true -and
    $s.RealTimeProtectionEnabled -eq $true -and $s.BehaviorMonitorEnabled -eq $true -and
    $s.AMRunningMode -eq 'Normal' -and $null -ne $age -and $age -ge 0 -and $age -le 24 -and
    $p.DisableArchiveScanning -eq $false -and ($counts | Measure-Object -Sum).Sum -eq 0
  [ordered]@{
    eligible = $ok
    antivirus = $s.AntivirusEnabled
    service = $s.AMServiceEnabled
    realtime = $s.RealTimeProtectionEnabled
    behavior_monitor = $s.BehaviorMonitorEnabled
    mode = $s.AMRunningMode
    platform = $s.AMProductVersion
    engine = $s.AMEngineVersion
    definitions = $s.AntivirusSignatureVersion
    definitions_utc = if ($s.AntivirusSignatureLastUpdated) { $s.AntivirusSignatureLastUpdated.ToUniversalTime().ToString('o') } else { $null }
    definition_age_hours = $age
    archive_scan_disabled = $p.DisableArchiveScanning
    exclusion_counts = $counts
  }
}
if ($env:OS -ne 'Windows_NT') { throw 'Windows required.' }
if (Test-Path -LiteralPath $EvidencePath) { throw 'Evidence path must be new.' }
$report = [ordered]@{
  schema = 1
  utc = [DateTime]::UtcNow.ToString('o')
  status = 'BLOCKED_OR_INCOMPLETE'
  scan_requested = $false
  scan_completed_confirmed = $false
  release_approved = $false
  scope = 'One exact original archive; separate verified extracted-content scan and human review required.'
}
try {
  $os = Get-CimInstance Win32_OperatingSystem
  $report.os = $os.Caption
  $report.os_build = $os.BuildNumber
  $report.before = Read-Gate
  if (-not $report.before.eligible) { throw 'Defender environment gate did not pass.' }
  $file = Get-Item -LiteralPath $PackagePath
  if ($file.PSIsContainer -or ($file.Attributes -band [IO.FileAttributes]::ReparsePoint) -or -not $expected.ContainsKey($file.Name)) { throw 'Unknown original package or unsupported file type.' }
  $report.file = $file.Name
  $report.expected_sha256 = $expected[$file.Name]
  $report.before_sha256 = (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
  if ($report.before_sha256 -ne $report.expected_sha256) { throw 'Original package digest mismatch.' }
  # Do not record raw paths, usernames, detection resources or scan command output.
  $start = Get-Date
  $report.scan_requested = $true
  Start-MpScan -ScanType CustomScan -ScanPath $file.FullName -ErrorAction Stop
  $report.after = Read-Gate
  $report.after_sha256 = if (Test-Path -LiteralPath $file.FullName -PathType Leaf) { (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash.ToLowerInvariant() } else { $null }
  $detections = @(Get-MpThreatDetection | Where-Object { $_.InitialDetectionTime -ge $start.AddMinutes(-2) -or $_.LastThreatStatusChangeTime -ge $start.AddMinutes(-2) })
  $report.recent_detection_count = $detections.Count
  $report.recent_detection_ids = @($detections | Select-Object -ExpandProperty ThreatID -Unique)
  if ($detections.Count -gt 0 -or $report.after_sha256 -ne $report.before_sha256) {
    $report.status = 'DETECTION_OR_FILE_CHANGE_REVIEW_REQUIRED'
  } elseif (-not $report.after.eligible) {
    $report.status = 'BLOCKED_OR_INCOMPLETE'
  } else {
    # Start-MpScan returning is not proof of completed scope or clean result.
    $report.status = 'SCAN_REQUESTED_REVIEW_REQUIRED'
  }
  $report.instructions = 'Review Windows Security protection history and Defender Operational scan start/end/detection events; verify scope, outcome, and separately scan verified extracted contents. Do not restore quarantined files.'
} catch {
  $report.error_type = $_.Exception.GetType().Name
  $report.status = 'BLOCKED_OR_INCOMPLETE'
  # Error text can contain private paths. Never emit it to a public evidence file.
} finally {
  $report.finished_utc = [DateTime]::UtcNow.ToString('o')
  # CreateNew prevents overwriting evidence or the original.
  $stream = [IO.File]::Open([IO.Path]::GetFullPath($EvidencePath), [IO.FileMode]::CreateNew, [IO.FileAccess]::Write)
  try {
    $writer = [IO.StreamWriter]::new($stream, [Text.UTF8Encoding]::new($false))
    try { $writer.WriteLine(($report | ConvertTo-Json -Depth 6)) } finally { $writer.Dispose() }
  } finally { $stream.Dispose() }
  Write-Host ('Status: ' + $report.status + '; review local evidence. No release approval.')
}
if ($report.status -ne 'SCAN_REQUESTED_REVIEW_REQUIRED') { exit 1 }
