#!/usr/bin/env python3
"""Audit public GRAAL websites without executing any installers."""
import argparse, hashlib, json, re, subprocess, threading
from functools import partial
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

PROJECTS = ("genesis", "rubedo", "argus", "aeris", "lilium")
NAMES = ("K&G Vision", "Genesis", "Rubedo", "Argus", "Aeris", "Lilium")
HOST = "kgasil.github.io"
ORIGIN = "https://" + HOST
EXCLUDED = ("backups/", "extension/", "core/")
VIEWPORTS = ((390, 844), (768, 1024), (1440, 900))
errors, pages, snapshots = [], {}, {}
diagnostics = []
stats = {"links": 0, "checksums": 0, "browser_views": 0, "experience_views": 0}

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.nav = set(), [], []
        self.in_nav = self.in_anchor = False
        self.label = ""
        self.feed(text)
    def handle_starttag(self, tag, attributes):
        a = dict(attributes)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag in ("a", "link", "img", "script"):
            v = a.get("href") or a.get("src")
            if v:
                self.links.append((tag, v))
        if tag == "nav" and "kg-graal-bar" in a.get("class", "").split():
            self.in_nav = True
        if self.in_nav and tag == "a":
            self.in_anchor, self.label = True, ""
    def handle_data(self, data):
        if self.in_anchor:
            self.label += data
    def handle_endtag(self, tag):
        if tag == "a" and self.in_anchor:
            self.nav.append(" ".join(self.label.split()))
            self.in_anchor = False
        if tag == "nav" and self.in_nav:
            self.in_nav = False

def tracked(root):
    return subprocess.check_output(["git", "-C", str(root), "ls-files", "-z"]).decode().split("\0")

def local_file(root, url):
    u = urlsplit(url)
    if u.hostname != HOST:
        return None
    path = root / unquote(u.path).lstrip("/")
    if not path.resolve().is_relative_to(root.resolve()):
        return None
    return path / "index.html" if path.is_dir() else path

def check_static(root, repos):
    for prefix, directory in repos.items():
        snapshots[prefix or "institutional"] = subprocess.check_output(
            ["git", "-C", str(directory), "rev-parse", "HEAD"], text=True).strip()
        for relative in tracked(directory):
            if not relative.endswith(".html") or relative.startswith(EXCLUDED):
                continue
            url = ORIGIN + "/" + (prefix + "/" if prefix else "") + relative
            source = (directory / relative).read_text(encoding="utf-8")
            doc = Page(source)
            pages[url] = doc
            if not relative.startswith("portfolio/"):
                if tuple(doc.nav) != NAMES:
                    errors.append(f"{url}: unexpected ecosystem labels {doc.nav}")
                if "justify-content:center!important" not in source:
                    errors.append(f"{url}: centered ecosystem CSS missing")
            if re.search(r"\bProject Genesis\s+4000\b", source, re.I):
                errors.append(f"{url}: outdated Genesis name")
        readme = directory / "README.md"
        if readme.exists() and re.search(r"\bProject Genesis\s+4000\b", readme.read_text(), re.I):
            errors.append(f"{prefix or 'institutional'} README: outdated Genesis name")
        for sums in (directory / "downloads").glob("*SHA256SUMS.txt"):
            for line in sums.read_text().splitlines():
                if not line.strip():
                    continue
                m = re.fullmatch(r"([0-9a-fA-F]{64})\s+\*?(.+)", line.strip())
                if not m:
                    errors.append(f"{prefix}/{sums.name}: malformed checksum")
                    continue
                expected, filename = m.groups()
                file = sums.parent / filename
                if not file.resolve().is_relative_to(sums.parent.resolve()) or not file.is_file() or hashlib.sha256(file.read_bytes()).hexdigest() != expected.lower():
                    errors.append(f"{prefix}/{filename}: checksum missing or different")
                stats["checksums"] += 1
        if prefix in ("genesis", "rubedo", "argus"):
            manifest = json.loads((directory / "extension/manifest.json").read_text())
            mini = (directory / "mini/index.html").read_text()
            if not re.search(r"MINI LAB\s+" + re.escape(manifest["version"]) + r"\b", mini, re.I):
                errors.append(f"{prefix}: Mini Lab version differs from manifest")
        if prefix in ("genesis", "argus"):
            home = (directory / "index.html").read_text()
            if not re.search(r"instalação permanece suspensa|instalação suspensa", home, re.I):
                errors.append(f"{prefix}: distribution hold missing; review required")
            if any(re.search(r"\.zip(?:$|\?)", link, re.I) for tag, link in Page(home).links if tag == "a"):
                errors.append(f"{prefix}: direct ZIP link during distribution hold")
    for url, doc in pages.items():
        for tag, raw in set(doc.links):
            target = urljoin(url, raw)
            file = local_file(root, target)
            if file is None:
                continue
            stats["links"] += 1
            if not file.is_file():
                errors.append(f"{url}: missing resource {raw}")
                continue
            fragment = unquote(urlsplit(target).fragment)
            if fragment and file.suffix == ".html" and "=" not in fragment:
                if fragment not in Page(file.read_text(encoding="utf-8")).ids:
                    errors.append(f"{url}: missing anchor {raw}")

def check_experience(page, base, path):
    """Targeted keyboard, language, menu contrast and logo smoke checks."""
    issues = []
    def require(ok, label):
        if not ok:
            issues.append(label)
    pt_title = page.title()
    skip = page.locator("a.skip[href='#main'], a.skip[href='#home']").first
    skip.focus()
    require(skip.evaluate("(e) => {const r=e.getBoundingClientRect();return r.top>=0&&r.left>=0&&r.bottom<=innerHeight}"), "skip link not visible when focused")
    page.keyboard.press("Enter")
    require(page.evaluate("document.activeElement === document.querySelector('main')"), "skip link did not move keyboard focus to main")
    for lang, label in (("en", "English"), ("pt", "Português (Brasil)")):
        btn = page.locator("#"+lang)
        require(btn.get_attribute("aria-label") == label, "language accessible label missing: "+lang)
        btn.click()
        require(page.locator("html").get_attribute("lang") == ("en" if lang=="en" else "pt-BR"), "document language mismatch: "+lang)
        require(btn.get_attribute("aria-pressed") == "true", "language pressed state mismatch")
        other = page.locator("#"+("pt" if lang=="en" else "en"))
        require(other.get_attribute("aria-pressed") == "false", "language inactive state mismatch")
        require((page.title()!=pt_title) if lang=="en" else (page.title()==pt_title), "localized title mismatch: "+lang)
        require(page.locator("nav.kg-graal-bar a").evaluate_all("(links, lang) => links.every(a => new URL(a.href).searchParams.get('lang') === (lang==='en'?'en':null))", lang), "ecosystem link language mismatch: "+lang)
    result = page.locator("nav.kg-graal-bar").evaluate("""nav => {
      function rgb(s){return (s.match(/[\\d.]+/g)||[]).slice(0,3).map(Number)}
      function lum(c){const x=c.map(v=>{v/=255;return v<=0.04045?v/12.92:((v+0.055)/1.055)**2.4});return x[0]*0.2126+x[1]*0.7152+x[2]*0.0722}
      return {ratios:[...nav.querySelectorAll('a')].map(a=>{const s=getComputedStyle(a);const bg=s.backgroundColor==='rgba(0, 0, 0, 0)'||s.backgroundColor==='transparent'?getComputedStyle(nav).backgroundColor:s.backgroundColor;const x=lum(rgb(s.color)),y=lum(rgb(bg));return (Math.max(x,y)+0.05)/(Math.min(x,y)+0.05)}),logo:!!nav.querySelector('img.kg-graal-shield')};
    }""")
    require(len(result["ratios"]) == 6 and all(v >= 4.5 for v in result["ratios"]), "ecosystem menu normal text contrast below 4.5:1")
    require(result["logo"], "institutional shield reference absent")
    page.goto(base + path + "?lang=en", wait_until="domcontentloaded", timeout=20000)
    require(page.locator("html").get_attribute("lang")=="en", "direct English URL did not initialize English")
    require(page.locator("#en").get_attribute("aria-pressed")=="true", "direct English URL inactive")
    page.locator("#pt").click()
    stats["experience_views"] += 1
    return issues

def check_browser(root, output):
    from playwright.sync_api import sync_playwright
    class QuietHandler(SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(root)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{server.server_port}"
    shots = output / "screenshots"
    shots.mkdir(exist_ok=True)
    try:
        with sync_playwright() as pw:
            for engine in ("chromium", "firefox"):
                browser = getattr(pw, engine).launch()
                for width, height in VIEWPORTS:
                    context = browser.new_context(viewport={"width": width, "height": height}, accept_downloads=False)
                    def route_request(route):
                        u = urlsplit(route.request.url)
                        if u.hostname == "127.0.0.1":
                            route.continue_()
                        elif u.hostname == HOST and route.request.resource_type in ("image", "stylesheet", "font", "script"):
                            file = local_file(root, route.request.url)
                            if file and file.is_file():
                                route.fulfill(path=str(file))
                            else:
                                route.abort()
                        else:
                            route.abort()
                    context.route("**/*", route_request)
                    for url, doc in pages.items():
                        page = context.new_page()
                        js_errors, issues = [], []
                        page.on("pageerror", lambda error: js_errors.append(str(error)))
                        key = f"{engine}-{width}-" + urlsplit(url).path.strip("/").replace("/", "-")
                        try:
                            response = page.goto(base + urlsplit(url).path, wait_until="domcontentloaded", timeout=20000)
                            if not response or not response.ok:
                                raise RuntimeError("page did not return HTTP 200")
                            result = page.evaluate("""() => {
                              const nav = document.querySelector('nav.kg-graal-bar');
                              const links = nav ? [...nav.querySelectorAll('a')] : [];
                              return {title: document.title, width: document.documentElement.scrollWidth,
                                viewport: document.documentElement.clientWidth,
                                background: getComputedStyle(document.body).backgroundColor,
                                first: links.length ? links[0].getBoundingClientRect().left : null,
                                last: links.length ? links.at(-1).getBoundingClientRect().right : null};
                            }""")
                            stats["browser_views"] += 1
                            # Local CI timing is diagnostic only; it is not real-user performance.
                            path = urlsplit(url).path
                            if path in ("/index.html", "/distribuicao.html", "/genesis/business.html", *("/"+p+"/index.html" for p in PROJECTS)):
                                timing = page.evaluate("""() => {
                                  const n = performance.getEntriesByType('navigation')[0];
                                  const nav = document.querySelector('nav.kg-graal-bar');
                                  return {dom_interactive_ms:n?.domInteractive,dom_content_loaded_ms:n?.domContentLoadedEventEnd,
                                    response_end_ms:n?.responseEnd,document_transfer_bytes:n?.transferSize,
                                    nav_links:nav?.querySelectorAll('a').length,
                                    images_without_alt:document.querySelectorAll('img:not([alt])').length,
                                    headings_h1:document.querySelectorAll('h1').length,
                                    unnamed_buttons:[...document.querySelectorAll('button')].filter(b=>!(b.getAttribute('aria-label')||b.getAttribute('aria-labelledby')||b.textContent.trim()||b.querySelector('img[alt]'))).length};
                                }""")
                                diagnostics.append({"engine":engine,"viewport":width,"page":path,**timing})

                            if not result["title"]:
                                issues.append("missing title")
                            if result["width"] > result["viewport"] + 3:
                                issues.append(f"horizontal overflow {result['width'] - result['viewport']}px")
                            if width == 1440 and doc.nav and abs((result["first"] + result["last"]) / 2 - result["viewport"] / 2) > 12:
                                issues.append("ecosystem navigation not centered")
                            rgb = re.findall(r"[\d.]+", result["background"])
                            if len(rgb) >= 3 and sum(float(x) for x in rgb[:3]) / 3 > 160:
                                issues.append("unexpected bright body background")
                            path = urlsplit(url).path
                            if path in ("/index.html", "/distribuicao.html", "/genesis/business.html", *("/"+p+"/index.html" for p in PROJECTS)):
                                issues.extend(check_experience(page, base, path))
                            issues.extend("JS: " + e for e in js_errors)
                            if issues or (engine == "chromium" and width == 1440 and urlsplit(url).path.count("/") <= 2 and url.endswith("/index.html")):
                                page.screenshot(path=str(shots / (key + ".png")), timeout=10000)
                        except Exception as exc:
                            issues.append(str(exc))
                        finally:
                            page.close()
                        errors.extend(f"{engine} {width}px {url}: {issue}" for issue in issues)
                    context.close()
                browser.close()
    finally:
        server.shutdown()
        server.server_close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--webroot", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--browser", action="store_true")
    args = parser.parse_args()
    root, output = args.webroot.resolve(), args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    repos = {"": root, **{n: root / n for n in PROJECTS}}
    check_static(root, repos)
    if args.browser:
        check_browser(root, output)
    scope = "Local links, menus, nominal versions, tracked checksums, browser smoke tests and targeted keyboard/language/menu contrast checks; not full accessibility, malware certification or third-party link validation."
    report = {"commits": snapshots, "pages": len(pages), **stats, "errors": errors, "scope": scope}
    (output / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2))
    if args.browser:
        (output / "experience-baseline.json").write_text(json.dumps({"scope":"Local CI navigation timing and limited DOM accessibility indicators; not real-user metrics or WCAG compliance","samples":diagnostics},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        print(f"Experience baseline samples: {len(diagnostics)}")
        for metric in ("dom_interactive_ms","dom_content_loaded_ms","document_transfer_bytes","images_without_alt","unnamed_buttons"):
            values=[r[metric] for r in diagnostics if isinstance(r.get(metric),(int,float))]
            if values:
                print(f"Diagnostic {metric}: min={min(values):.2f}, max={max(values):.2f}, samples={len(values)}")

    summary = ["# GRAAL website audit", "", f"- Public pages: {len(pages)}",
               f"- Local links checked: {stats['links']}", f"- Tracked checksums: {stats['checksums']}",
               f"- Browser views: {stats['browser_views']}", f"- Targeted experience views: {stats['experience_views']}", f"- Errors: {len(errors)}", "",
               *[f"- {e}" for e in errors], "", scope]
    (output / "summary.md").write_text("\n".join(summary) + "\n")
    print("\n".join(summary))
    raise SystemExit(bool(errors))

if __name__ == "__main__":
    main()
