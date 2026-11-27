import json, hashlib, sys, threading
from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright, expect

def digest(record):
    return hashlib.sha256(json.dumps(record,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
server=ThreadingHTTPServer(("127.0.0.1",0),SimpleHTTPRequestHandler)
threading.Thread(target=server.serve_forever,daemon=True).start()
base=f"http://127.0.0.1:{server.server_port}/graal/"
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
with sync_playwright() as p:
    for name in ("chromium","firefox"):
        b=getattr(p,name).launch()
        page=b.new_page(viewport={"width":320,"height":800},accept_downloads=True)
        external=[];errors=[]
        page.on("pageerror",lambda error:errors.append(str(error)))
        def route(r):
            if not r.request.url.startswith(f"http://127.0.0.1:{server.server_port}/"):
                external.append(r.request.url);r.abort()
            else:r.continue_()
        page.route("**/*",route)
        page.goto(base)
        expect(page.locator("#status")).to_have_text("Evidências verificadas. Autorize o início.")
        expect(page.locator("#advance")).to_be_disabled()
        expect(page.locator("#export")).to_be_disabled()
        page.keyboard.press("Tab")
        expect(page.locator(".skip")).to_be_focused()
        page.keyboard.press("Enter")
        expect(page.locator("#main")).to_be_focused()
        for width in (320,768,1440):
            page.set_viewport_size({"width":width,"height":900})
            assert page.evaluate("document.documentElement.scrollWidth<=document.documentElement.clientWidth")
        page.locator("#en").click()
        expect(page.locator("html")).to_have_attribute("lang","en")
        expect(page.locator("h1")).to_have_text("GRAAL integrated lab")
        assert page.locator("nav.kg-graal-bar a").count()==6
        assert page.locator("nav img.kg-graal-shield").count()==1
        assert page.locator("nav a").evaluate_all("(links)=>links.every(a=>new URL(a.href).searchParams.get('lang')==='en')")
        assert page.locator("nav").evaluate("n=>getComputedStyle(n).justifyContent==='center'")
        expect(page.locator("#services-title")).to_have_text("04 · Solutions and business presentation")
        expect(page.locator("#qual-status")).to_contain_text("0/4 simulated conditions")
        for i in range(4): page.locator(f"#qual-{i}").check()
        expect(page.locator("#qual-status")).to_contain_text("no real authorization")
        page.locator("#pt").click()
        expect(page.locator("#qual-status")).to_contain_text("4/4 condições simuladas")
        assert page.locator("nav a").evaluate_all("(links)=>links.every(a=>!new URL(a.href).searchParams.has('lang'))")
        page.locator("#en").click()
        page.locator("#qual-reset").click()
        expect(page.locator("#qual-status")).to_contain_text("0/4 simulated conditions")
        page.locator("#services").screenshot(path=str(out/f"{name}-commercial.png"))
        for n in range(5):
            expect(page.locator("#advance")).to_be_disabled()
            page.locator("#permit").check()
            page.locator("#advance").click()
            expect(page.locator("#progress")).to_have_text(f"{n+1}/5")
        for i in range(3):
            expect(page.locator(f"#pilot-run-{i}")).to_be_disabled()
            page.locator(f"#pilot-grant-{i}").check()
            page.locator(f"#pilot-run-{i}").click()
        expect(page.locator("#export")).to_be_enabled()
        with page.expect_download() as d:page.locator("#export").click()
        record=json.loads(Path(d.value.path()).read_bytes());assert digest({k:v for k,v in record.items() if k!="sha256"})==record["sha256"]
        assert len(record["session_approvals"])==5 and len(record["pilots"])==3 and record["release_approved"] is False
        page.screenshot(path=str(out/f"{name}-completed.png"),full_page=True)
        page.locator("#pilot-grant-1").uncheck()
        with page.expect_download() as d:page.locator("#export").click()
        record=json.loads(Path(d.value.path()).read_bytes());assert len(record["pilots"])==2
        page.locator("#reset").click()
        expect(page.locator("#progress")).to_have_text("0/5")
        expect(page.locator("#qual-status")).to_contain_text("0/4 simulated conditions")
        expect(page.locator("#export")).to_be_disabled()
        assert page.evaluate("localStorage.length===0 && sessionStorage.length===0 && document.cookie===''")
        assert not external and not errors,(external,errors)
        page.goto(base+"?lang=en");expect(page.locator("h1")).to_have_text("GRAAL integrated lab")
        expect(page.locator("#progress")).to_have_text("0/5")
        data=json.loads(Path("graal/evidence.json").read_text());data["trace"]["steps"][0]["payload"]["reading_words"]=99
        page.route("**/evidence.json",lambda r:r.fulfill(json=data))
        page.reload()
        expect(page.locator("#status")).to_have_text("Invalid or unavailable evidence. Execution blocked.")
        expect(page.locator("#permit")).to_be_disabled()
        expect(page.locator("#export")).to_be_disabled()
        b.close()
        print(name,"PASS: language, keyboard, 3 widths, consent, all pilots, export hash, revocation, reload, tampering, no external requests/storage; commercial scopes, language links and qualification")
server.shutdown()
