# Development-only Authenticode demonstration. No release files or trust settings are changed.
$ErrorActionPreference = 'Stop'
$out = Join-Path $env:RUNNER_TEMP 'graal-signing-demo'
New-Item -ItemType Directory -Path $out -Force | Out-Null
$cert = $null
try {
    $params = @{
        Type = 'CodeSigningCert'
        Subject = 'CN=Kaio Gabriel da Silva - K&G Vision TEST ONLY'
        FriendlyName = 'K&G Vision - development test only'
        CertStoreLocation = 'Cert:\CurrentUser\My'
        KeyAlgorithm = 'RSA'
        KeyLength = 3072
        HashAlgorithm = 'SHA256'
        KeyExportPolicy = 'NonExportable'
        NotAfter = (Get-Date).AddDays(30)
    }
    $cert = New-SelfSignedCertificate @params
    $fixture = Join-Path $out 'Graal-Signing-Demo.ps1'
    Set-Content -LiteralPath $fixture -Encoding UTF8 -Value 'Write-Output "K&G Vision - signing demonstration only"'
    $before = (Get-FileHash -LiteralPath $fixture -Algorithm SHA256).Hash
    $null = Set-AuthenticodeSignature -LiteralPath $fixture -Certificate $cert -HashAlgorithm SHA256
    $sig = Get-AuthenticodeSignature -LiteralPath $fixture
    if (-not $sig.SignerCertificate -or $sig.SignerCertificate.Thumbprint -ne $cert.Thumbprint) {
        throw 'Expected embedded test signature is missing.'
    }
    if ($sig.Status -eq 'HashMismatch' -or $sig.Status -eq 'NotSigned') {
        throw 'Signature integrity check failed.'
    }
    $after = (Get-FileHash -LiteralPath $fixture -Algorithm SHA256).Hash
    if ($before -eq $after) { throw 'Expected signed bytes to differ.' }
    Export-Certificate -Cert $cert -FilePath (Join-Path $out 'Graal-Test-Public.cer') | Out-Null
    $evidence = [ordered]@{
        subject=$cert.Subject; issuer=$cert.Issuer; thumbprint=$cert.Thumbprint
        certificate_type='self-signed development only'; windows_status=$sig.Status.ToString()
        signed_fixture='Graal-Signing-Demo.ps1'; sha256_before=$before.ToLowerInvariant()
        sha256_signed=$after.ToLowerInvariant(); private_key_exported=$false
        trust_store_modified=$false; fixture_executed=$false; public_installers_signed=$false
        production_approved=$false
    }
    $evidence | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $out 'evidence.json') -Encoding UTF8
    $evidence | ConvertTo-Json
} finally {
    if ($cert) { Remove-Item -LiteralPath ("Cert:\CurrentUser\My\" + $cert.Thumbprint) -DeleteKey -ErrorAction Stop }
}
