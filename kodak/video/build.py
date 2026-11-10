# Kodak: "It Invented the Future" (Paper Empire). One block per voice line. Run: python3 build.py
import sys, os; sys.path.insert(0, os.path.abspath("../../kit"))
from build_lib import *
import build_lib; build_lib.GAP = 0.9      # a little more breathing room between lines (this video ran 7:47)

# =========================== COLD OPEN ===========================
s, c = line_scene("In April twenty twelve")
s.kicker("April 2012 · Facebook buys an app", 192, 150, c("april"))
phone = "".join(f'<div class="k00-t" style="position:absolute;left:{28 + (k % 3) * 146}px;top:{120 + (k // 3) * 146}px;width:138px;height:138px;background:#{"141414" if (k * 7) % 3 else "6B6963"};opacity:0"></div>' for k in range(15))
s.raw(f'<div id="k00-ph" class="o0" style="position:absolute;left:1180px;top:110px;width:500px;height:860px;border:14px solid #141414;border-radius:56px">{phone}</div>',
      js=f"on('#k00-ph', {c('app'):.3f}); tl.fromTo('#root .k00-t', {{ opacity: 0 }}, {{ opacity: 1, duration: 0.001, stagger: 0.05 }}, {c('took|photos'):.3f});")
s.click(c("app"))
s.count(186, 260, 330, c("one|$1"), 1, "v => '$' + v.toFixed(1) + 'B'", d=1.3)
s.kicker("for an app that took photos", 192, 620, c("app"))
s.source("Source: Facebook–Instagram deal, April 2012 (Al Jazeera, Business Insider)")

s, c = line_scene("The company had thirteen")
s.dots(192, 300, 13, 1, 110, c("thirteen|13"), d=0.7, shape="sq")
s.text("13 employees", 186, 520, 260, t=c("employees"))

s, c = line_scene("Three months earlier", "ink")
s.photos([("tower", 0)], rate=0.015)
s.raw('<div class="fill" style="background:rgba(20,20,20,.5)"></div>')
s.kicker("Three months earlier", 192, 160, c("three|3"), "np")
s.text("130 years of photography", 186, 230, 160, color="np", t=c("hundred|130"))
s.stamp("Chapter 11", 900, 600, 220, c("bankruptcy"))
s.source("Photo: Kodak Tower, Rochester NY · Wikimedia Commons, CC BY-SA", light=True)

s, c = line_scene("That company was Kodak")
s.text("Kodak", 186, 140, 320, t=c("kodak"))
s.raw('<div id="k03-pw" class="o0" style="position:absolute;left:1020px;top:110px;width:720px;height:860px;background:#F7F5F0;box-shadow:0 14px 30px rgba(0,0,0,.2)"><img src="assets/img/p_sasson.jpg" style="width:100%;height:100%;object-fit:contain" alt=""></div>',
      js=f"tl.fromTo('#k03-pw', {{ opacity: 1, y: 60 }}, {{ y: 0, duration: 0.5, ease: 'expo.out' }}, {c('invented'):.3f});")
s.click(c("invented"))
s.text("invented the\ndigital camera", 186, 520, 170, t=c("invented"))
s.source("Image: Sasson's 1975 camera (patent drawing) · Wikimedia Commons, CC BY-SA 4.0")

s, c = line_scene("It built it in nineteen seventy-five")
s.text("1975 · built it", 186, 150, 200, t=c("built"))
s.text("1981 · studied the threat", 186, 380, 200, t=c("studied"))
s.text("No. 1 digital camera seller", 186, 610, 200, t=c("number|no"))

s, c = line_scene("It still lost.", "ink", hold=0.8, punch=True)
s.text("It still lost.", 330, 340, 380, color="np", t=c("still"), mode="on")
s.click(c("still"), "impact", 0.55)

s, c = line_scene("This is the story of a company", "ink", hold=0.6)
s.raw(f'<div id="k06-crown" class="o0" style="position:absolute;left:192px;top:300px">{CROWN_SVG.format(s=180)}</div>', js="on('#k06-crown', 0.25);")
s.kicker("Paper Empire", 410, 360, 0.3, "np")
s.text("Kodak", 186, 520, 320, color="np", t=c("company"))
s.kicker("The company that saw the future and couldn't afford it", 192, 840, c("saw"), "np")
s.click(c("company"), "impact", 0.4)

# =========================== CHAPTER 1 ===========================
chapter("ch1", "You press the button", ["p_eastman", "p_ad1888", "brownie", "p_kodakgirl", "p_ad1905", "film120", "p_film", "brownie2", "p_eastman_desk"], d=3.2)

s, c = line_scene("In eighteen eighty-eight")
portrait(s, "p_eastman", "George Eastman", "Bank clerk turned inventor", c("george"), pos="50% 20%")
s.kicker("1888 · the first Kodak", 192, 150, c("eighteen|1888"))
s.count(186, 220, 260, c("twenty|$25"), 25, "v => '$' + Math.round(v)", d=1.0)
s.kicker("film for 100 pictures", 192, 480, c("hundred|100"))
s.source("Source: Swiss Camera Museum · Photo: public domain")

s, c = line_scene("When the roll was full")
s.raw('<div id="k08-ad" class="o0" style="position:absolute;left:1100px;top:110px;width:620px;height:860px;background:#F7F5F0;box-shadow:0 14px 30px rgba(0,0,0,.2)"><img src="assets/img/p_ad1888.jpg" style="width:100%;height:100%;object-fit:contain" alt=""></div>',
      js=f"tl.fromTo('#k08-ad', {{ opacity: 1, x: 200, rotation: 3 }}, {{ x: 0, rotation: 1.5, duration: 0.5, ease: 'expo.out' }}, 0.3);")
s.click(0.3)
s.text("Mail the camera\nto Rochester", 186, 170, 170, t=c("mailed"))
s.text("Developed · reloaded\n· sent home", 186, 560, 140, color="grey", t=c("developed"))
s.source("Image: 1888 Kodak advert, public domain")

s, c = line_scene("The slogan was four words long")
for k, (w, lab) in enumerate([("you", "You press"), ("button", "the button."), ("we", "We do"), ("rest", "the rest.")]):
    s.text(lab, 186 + (k % 2) * 760, 260 + (k // 2) * 300, 240, t=c(w), mode="on")
    s.click(c(w), vol=0.25)
s.kicker("Kodak slogan, 1888", 192, 150, c("slogan"))

s, c = line_scene("In nineteen hundred")
s.photos([("brownie", 0)], rate=0.02, clicks=False)
s.raw('<div class="fill" style="background:linear-gradient(90deg,rgba(20,20,20,.85),rgba(20,20,20,0) 60%)"></div>')
s.kicker("1900 · the Brownie", 192, 300, c("nineteen|1900"), "np")
s.stamp("$1", 200, 400, 300, c("one|$1|dollar"), ink=True, sound=True)
s.source("Photo: Kodak Brownie, Wikimedia Commons, CC0", light=True)

s, c = line_scene("Kodak sold the idea")
s.raw('<div id="k11-ad" class="o0" style="position:absolute;left:1060px;top:110px;width:660px;height:860px;background:#F7F5F0;box-shadow:0 14px 30px rgba(0,0,0,.2)"><img src="assets/img/p_kodakgirl.jpg" style="width:100%;height:100%;object-fit:contain" alt=""></div>',
      js=f"tl.fromTo('#k11-ad', {{ opacity: 1, y: 80 }}, {{ y: 0, duration: 0.5, ease: 'expo.out' }}, {c('girl'):.3f});")
s.click(c("girl"))
s.text("Selling the idea", 186, 200, 150, t=c("idea"))
s.kicker("1914 · Saturday Evening Post", 192, 480, c("saturday"))
s.source("Image: The Kodak Girl advert, 1914, public domain")

s, c = line_scene("And that was the trick")
s.kicker("The trick", 192, 120, c("trick"))
loop = [("Camera", "camera"), ("Film", "film"), ("Chemicals", "chemicals"), ("Paper", "paper"), ("Processing", "processing")]
for k, (lab, w) in enumerate(loop):
    s.text(lab, 186 + (k % 3) * 520, 230 + (k // 3) * 220, 170, color="grey" if k == 0 else "", t=c(w))
s.text("Every photo paid Kodak again", 186, 760, 150, t=c("every"))
s.source("Kodak's razor-and-blades model (Forrester; business-history accounts)")

s, c = line_scene("By nineteen seventy-six")
s.kicker("1976 · US market share", 192, 150, c("nineteen|1976"))
for k, (pct, lab, w) in enumerate([(90, "of film", "ninety|90"), (85, "of cameras", "eighty|85")]):
    gx = 192 + k * 800
    cells = "".join(f'<div class="{"k13a" if k == 0 else "k13b"}" style="position:absolute;left:{(i % 10) * 44}px;top:{(i // 10) * 44}px;width:38px;height:38px;background:#C9C5BB"></div>' for i in range(100))
    gid = f"k13-g{k}"
    s.raw(f'<div id="{gid}" class="o0" style="position:absolute;left:{gx}px;top:230px;width:440px;height:440px">{cells}</div>',
          js=f"on('#{gid}', {c(w):.3f}); tl.fromTo('#root .{'k13a' if k == 0 else 'k13b'}:nth-child(-n+{pct})', {{ backgroundColor: '#C9C5BB' }}, {{ backgroundColor: '#141414', duration: 0.001, stagger: 0.008 }}, {c(w):.3f});")
    s.text(f"{pct}% {lab}", gx - 6, 700, 130, t=c(w, off=0.4))
s.source("Source: Columbia Business School case, “Leap into the Void”")

s, c = line_scene("At its peak, in nineteen eighty-eight")
s.kicker("1988 · Kodak employees worldwide", 192, 120, c("nineteen|1988"))
s.dots(192, 190, 145, 60, 10.6, c("hundred|145"), d=1.4, total=8700)
s.text("≈145,000", 1300, 860, 120, t=c("forty|145"), mode="on")
s.source("Source: Rochester Business Journal timeline · 1 dot ≈ 17 people")

s, c = line_scene("And in nineteen ninety-six")
s.kicker("1996 · revenue", 192, 200, c("nineteen|1996"))
s.count(186, 280, 420, c("sixteen|$16"), 16.2, "v => '$' + v.toFixed(1) + 'B'", d=1.4)
s.source("Source: Eastman Kodak 10-K, 1996 (SEC)")

s, c = line_scene("Even in two thousand, digital")
s.kicker("2000 · share of Kodak's sales", 192, 150, c("two|2000"))
cells = "".join(f'<div class="k16c" style="position:absolute;left:{(i % 25) * 60}px;top:{(i // 25) * 60}px;width:52px;height:52px;background:#C9C5BB"></div>' for i in range(100))
s.raw(f'<div id="k16-g" class="o0" style="position:absolute;left:192px;top:240px;width:1500px;height:240px">{cells}</div>',
      js=f"on('#k16-g', {c('digital'):.3f}); tl.fromTo('#root .k16c:nth-child(-n+21)', {{ backgroundColor: '#C9C5BB' }}, {{ backgroundColor: '#141414', duration: 0.001, stagger: 0.03 }}, {c('twenty|21'):.3f});")
s.text("Digital: 21%", 186, 560, 220, t=c("twenty|21"))
s.source("Source: Eastman Kodak 10-K, 2000 (SEC)")

# =========================== CHAPTER 2 ===========================
chapter("ch2", "The toaster in the lab", ["p_sasson", "p_tower", "film120", "p_film", "tower", "p_tower_night", "p_kodachrome", "brownie2", "p_ad1905"], d=3.2)

s, c = line_scene("But the most important thing")
s.text("Never went\non sale", 186, 240, 280, t=c("never"))

s, c = line_scene("In nineteen seventy-five, a young")
s.raw('<div id="k18-pw" class="o0" style="position:absolute;left:1020px;top:110px;width:720px;height:860px;background:#F7F5F0;box-shadow:0 14px 30px rgba(0,0,0,.2)"><img src="assets/img/p_sasson.jpg" style="width:100%;height:100%;object-fit:contain" alt=""></div>',
      js=f"tl.fromTo('#k18-pw', {{ opacity: 1, y: 60 }}, {{ y: 0, duration: 0.5, ease: 'expo.out' }}, {c('strange'):.3f});")
s.kicker("1975 · Kodak engineer", 192, 150, c("nineteen|1975"))
s.text("Steve Sasson", 186, 220, 200, t=c("steve"))
s.text("Toaster-sized", 186, 500, 150, t=c("toaster"))
s.text("8 pounds", 186, 680, 150, t=c("eight|8"))
s.source("Sources: IEEE Spectrum; AP interview (2023)")

s, c = line_scene("Its pictures were a hundred pixels")
px = "".join(f'<div class="k19p" style="position:absolute;left:{(i % 20) * 30}px;top:{(i // 20) * 30}px;width:28px;height:28px;background:#{["141414","6B6963","C9C5BB"][(i * 37 // 7) % 3]};opacity:0"></div>' for i in range(400))
s.raw(f'<div id="k19-g" style="position:absolute;left:1120px;top:180px;width:600px;height:600px">{px}</div>',
      js=f"tl.fromTo('#root .k19p', {{ opacity: 0 }}, {{ opacity: 1, duration: 0.001, stagger: 0.004 }}, {c('hundred|100'):.3f});")
s.text("100 × 100 pixels", 186, 200, 170, t=c("hundred|100"))
s.count(186, 470, 300, c("twenty|23"), 23, "v => Math.round(v) + ' sec'", d=2.0)
s.kicker("to save one photo to cassette tape", 192, 790, c("cassette"))
s.source("Source: IEEE Spectrum · grid is illustrative (20×20 shown)")

s, c = line_scene("It was the first digital camera.", "ink", hold=1.0)
s.text("The first\ndigital camera", 186, 260, 280, color="np", t=c("first"))

s, c = line_scene("It took its first picture")
s.kicker("December 1975", 192, 300, c("december"))
s.text("First digital photo", 186, 380, 240, t=c("first"))
s.source("Source: IEEE Spectrum")

s, c = line_scene("Sasson wasn't allowed")
s.text("Not allowed to talk\nabout it in public", 186, 200, 190, t=c("allowed"))
s.stamp("Confidential", 900, 640, 170, c("outside"), ink=True)
s.source("Source: IEEE Spectrum")

s, c = line_scene("But the popular version")
s.text("Locked in a drawer", 186, 160, 220, color="grey", t=c("locked"))
s.strike(176, 255, 1000, c("simple"), 20)
s.text("35 years at Kodak", 186, 480, 220, t=c("thirty|35"))
s.kicker("working on digital imaging", 192, 720, c("digital"))
s.source("Sources: IEEE Spectrum; RPI Davies Medal citation (2011)")

s, c = line_scene("It wasn't that Kodak didn't understand")
s.raw(f'<div id="k24-rep" class="o0" style="position:absolute;left:1100px;top:140px;width:620px;height:800px;background:#F7F5F0;box-shadow:0 14px 30px rgba(0,0,0,.2)">'
      f'<div class="kick grey" style="position:absolute;left:50px;top:60px;font-size:30px">1981 · MARKET INTELLIGENCE</div>'
      f'<div class="lg" style="position:absolute;left:50px;top:140px;font-size:110px;white-space:normal;width:520px">Film vs. digital</div>'
      f'<div class="rule" style="left:50px;top:420px;width:520px"></div>'
      f'<div style="position:absolute;left:50px;top:460px;font:400 28px Inter;color:#6B6963">Study led by Vince Barabba (rebuilt for illustration)</div></div>',
      js=f"tl.fromTo('#k24-rep', {{ opacity: 1, y: 60, rotation: -2 }}, {{ y: 0, rotation: -1, duration: 0.45, ease: 'expo.out' }}, {c('study'):.3f});")
s.kicker("1981", 192, 200, c("nineteen|1981"))
s.text("Vince Barabba", 186, 270, 190, t=c("vince"))
s.kicker("Head of market intelligence", 192, 480, c("market"), "grey")
s.source("Source: accounts of Barabba's study (Columbia/IIM case material)")

s, c = line_scene("According to later accounts")
s.kicker("The finding", 192, 160, c("finding"))
s.text("Digital could", 186, 240, 240, t=c("digital"))
s.text("replace film", 186, 470, 240, color="red", t=c("replace"))
s.source("Source: accounts of Barabba's 1981 study")

s, c = line_scene("Kodak knew.", hold=0.9)
s.text("Kodak knew.", 186, 200, 300, t=c("knew"))
s.text("What did knowing mean?", 186, 560, 180, color="grey", t=c("problem"))

s, c = line_scene("Every digital photo was a photo")
s.photos([("film120", 0)], rate=0.02, clicks=False)
s.raw('<div class="fill" style="background:rgba(233,230,223,.86)"></div>')
s.text("Every digital photo", 186, 240, 220, t=c("every"))
s.text("= a print nobody bought", 186, 500, 200, color="red", t=c("nobody"))

# =========================== CHAPTER 3 ===========================
chapter("ch3", "Winning the wrong race", ["dc40", "es1", "es2", "es3", "film120", "p_film", "tower", "p_kodachrome", "brownie"], d=3.2)

s, c = line_scene("Kodak kept building anyway")
s.photos([("dc40", 0)], rate=0.02, clicks=False)
s.raw('<div class="fill" style="background:linear-gradient(90deg,rgba(20,20,20,.88),rgba(20,20,20,0) 65%)"></div>')
s.kicker("March 1995", 192, 300, c("march"), "np")
s.text("Kodak DC40", 186, 370, 260, color="np", t=c("dc40|dc|d.c."))
s.kicker("one of the first consumer digital cameras", 192, 640, c("ordinary"), "np")
s.source("Photo: Kodak DC40, National Science and Media Museum · Wikimedia Commons, CC BY-SA 4.0", light=True)

s, c = line_scene("So Kodak tried to have it both ways")
s.photos([("es1", 0), ("es2", c("cameras")), ("es3", c("software"))], rate=0.03)
s.raw('<div class="fill" style="background:linear-gradient(0deg,rgba(20,20,20,.85),rgba(20,20,20,0) 60%)"></div>')
s.kicker("2001", 192, 680, c("two|2001"), "np")
s.text("EasyShare", 186, 740, 200, color="np", t=c("easyshare|easy"))
s.source(CC, light=True)

s, c = line_scene("And it worked")
s.kicker("2004 · US digital cameras (IDC)", 192, 150, c("two|2004"))
s.text("No. 1", 186, 220, 360, t=c("number|no"), mode="on")
s.click(c("number|no"), "impact", 0.35)
s.text("≈22% share · ahead of Sony", 186, 620, 150, t=c("twenty|22"))
s.source("Source: IDC via Reuters / NBC News")

s, c = line_scene("In two thousand five it held")
s.kicker("2005 · cameras shipped to US stores", 192, 200, c("two|2005"))
s.count(186, 280, 380, c("seven|7"), 7050000, INT, d=1.5)
s.source("Source: IDC via Reuters / NBC News")

s, c = line_scene("But here's the trap", hold=0.9)
s.text("A camera\nsells once", 186, 200, 260, t=c("camera"))
s.raw(f'<div id="k32-coin" class="o0" style="position:absolute;left:1400px;top:620px;width:200px;height:200px;border-radius:50%;background:#141414"></div>', js=f"on('#k32-coin', {c('once'):.3f});")
s.click(c("once"), "pop", 0.3)

s, c = line_scene("Film sold every single time")
coins = "".join(f'<div class="k33c" style="position:absolute;left:{(k % 12) * 120}px;top:{(k // 12) * 120}px;width:96px;height:96px;border-radius:50%;background:#141414;opacity:0"></div>' for k in range(36))
s.raw(f'<div style="position:absolute;left:192px;top:180px;width:1440px;height:360px">{coins}</div>',
      js=f"tl.fromTo('#root .k33c', {{ opacity: 0 }}, {{ opacity: 1, duration: 0.001, stagger: 0.04 }}, {c('film'):.3f});")
s.click(c("film"), "train", 0.25)
s.text("Film: paid every time", 186, 580, 170, t=c("every"))
s.text("Digital: a smaller prize", 186, 780, 170, color="red", t=c("smaller"))

s, c = line_scene("And the old business was disappearing")
s.raw('<div id="k34-k" class="o0" style="position:absolute;left:1180px;top:110px;width:540px;height:860px;overflow:hidden"><img src="assets/img/p_kodachrome.jpg" style="width:100%;height:100%;object-fit:cover" alt=""></div>',
      js=f"on('#k34-k', {c('kodachrome|codachrome|coda'):.3f});")
s.click(c("kodachrome|codachrome|coda"))
s.kicker("2009", 192, 200, c("twenty|2009"))
s.text("The end of\nKodachrome", 186, 270, 220, t=c("kodachrome|codachrome|coda"))
s.text("1935–2009", 186, 720, 150, t=c("seventy|74"))
s.hrule(186, 860, 560, c("years"), h=10, color="#D7261E")
s.source("Photo: Kodachrome II · Wikimedia Commons, CC BY-SA 3.0 AT")

s, c = line_scene("Kodachrome was so famous")
s.photos([("kodachrome_record", 0)], rate=0.02, clicks=False)
s.raw('<div class="fill" style="background:linear-gradient(90deg,rgba(20,20,20,.88),rgba(20,20,20,0) 60%)"></div>')
s.kicker("1973", 192, 360, c("nineteen|1973"), "np")
s.text("Paul Simon,\n“Kodachrome”", 186, 430, 200, color="np", t=c("paul"))
s.source("Photo: Paul Simon single · Wikimedia Commons, CC BY-SA 3.0 AT", light=True)

# =========================== CHAPTER 4 ===========================
chapter("ch4", "The phone in your pocket", ["es1", "es3", "p_tower", "tower", "p_tower_night", "dc40", "es2", "film120", "p_film"], d=3.2)

s, c = line_scene("Then the camera itself")
s.photos([("es2", 0)], rate=0.02, clicks=False)
s.js.append(f"tl.fromTo('#{s.sid}-ph1', {{ opacity: 1 }}, {{ opacity: 0, duration: 1.2, ease: 'power1.in', immediateRender: false }}, {c('disappear', off=-0.2):.3f});")
s.text("The camera\ndisappears", 186, 300, 280, t=c("disappear"))

s, c = line_scene("It moved into the phone")
s.raw('<div id="k37-ph" class="o0" style="position:absolute;left:1200px;top:110px;width:460px;height:860px;border:14px solid #141414;border-radius:56px"></div>', js=f"on('#k37-ph', {c('phone'):.3f});")
s.click(c("phone"))
s.text("Into the phone", 186, 200, 220, t=c("phone"))
s.text("No film · no paper\n· no Kodak", 186, 520, 170, color="grey", t=c("nobody"))

s, c = line_scene("Kodak's inventions didn't disappear")
s.kicker("Around 2010 · patent licences", 192, 150, c("around"))
s.text("Samsung", 186, 230, 200, t=c("samsung"))
s.text("LG", 186, 450, 200, t=c("lg|l.g."))
s.count(1000, 300, 300, c("billion"), 1, "v => '≈$' + v.toFixed(1) + 'B'", d=1.2)
s.source("Sources: AP via phys.org (2010); Globe and Mail")

s, c = line_scene("The digital camera Kodak invented")
s.raw('<div id="k39-ph" class="o0" style="position:absolute;left:1200px;top:110px;width:460px;height:860px;border:14px solid #141414;border-radius:56px"><div class="kick" style="position:absolute;left:60px;top:380px;font-size:34px;border:4px solid #141414;padding:10px 16px">KODAK PATENT</div></div>', js=f"on('#k39-ph', {c('phones'):.3f});")
s.text("Making money\ninside other\ncompanies' phones", 186, 220, 140, t=c("making"))

s, c = line_scene("In twenty eleven, Kodak went after Apple")
s.kicker("2011 · patent fight", 192, 200, c("twenty|2011"))
s.text("Kodak vs. Apple", 186, 270, 240, t=c("apple"))
s.text("$1B+ in royalties", 186, 560, 200, color="grey", t=c("billion"))
s.source("Source: AppleInsider, March 2011")

s, c = line_scene("On January nineteenth", "ink")
s.photos([("p_tower_night", 0, "50% 30%")], rate=0.015, clicks=False)
s.raw('<div class="fill" style="background:rgba(20,20,20,.45)"></div>')
s.kicker("January 19, 2012", 192, 160, c("january"), "np")
s.stamp("Chapter 11", 520, 380, 260, c("chapter|11"))
s.source("Photo: Kodak Tower at night · Wikimedia Commons, CC BY-SA 3.0", light=True)

s, c = line_scene("By then its workforce")
s.kicker("Kodak employees", 192, 120, c("workforce"))
d1 = s.dots(192, 190, 145, 60, 10.6, 0.0, d=0.01, total=8700, color="#C9C5BB")
s.dots(192, 190, 145, 60, 10.6, c("nineteen|19"), d=0.6, total=1120)
s.text("≈19,000", 1300, 860, 120, t=c("nineteen|19"), mode="on")
s.kicker("from ≈145,000 at the 1988 peak", 192, 980 - 60, c("hundred|145"), "grey")
s.source("Sources: bankruptcy coverage (Jan 2012); RBJ · 1 dot ≈ 17 people")

s, c = line_scene("And it was carrying the weight")
s.text("Retirees", 186, 200, 220, t=c("retirees"))
s.dots(192, 450, 20, 2, 70, c("retirees"), d=0.5, shape="sq")
s.text("Workers", 186, 640, 160, color="grey", t=c("workers"))
s.dots(192, 820, 20, 1, 70, c("workers"), d=0.4, shape="sq", color="#6B6963")
s.source("Source: Employee Benefit News (2012) · 2 : 1, illustrative counts")

s, c = line_scene("In Rochester, New York")
s.photos([("p_tower", 0, "50% 40%")], rate=0.02, clicks=False)
s.raw('<div class="fill" style="background:linear-gradient(90deg,rgba(20,20,20,.88),rgba(20,20,20,.1) 70%)"></div>')
s.kicker("Rochester, New York · end of 2011", 192, 300, c("rochester"), "np")
s.text("≈5,100 local jobs", 186, 380, 200, color="np", t=c("five|5"))
s.source("Source: Rochester Business Journal (Mar 2012) · Photo: Wikimedia Commons, CC BY-SA 3.0", light=True)

s, c = line_scene("Weeks later, Kodak said")
s.photos([("es3", 0)], rate=0.02, clicks=False)
s.raw('<div class="fill" style="background:rgba(20,20,20,.45)"></div>')
s.stamp("Discontinued", 380, 420, 230, c("stop"), ink=False)
s.source("Source: IndustryWeek (Feb 2012)", light=True)

s, c = line_scene("That April, Facebook bought Instagram")
s.kicker("April 2012", 192, 150, c("april"))
s.text("Instagram: $1 billion", 186, 220, 220, t=c("instagram"))
s.text("$300M cash + ≈23M shares", 186, 520, 150, color="grey", t=c("three|$300"))
s.source("Source: Al Jazeera (April 2012)")

s, c = line_scene("To pay its creditors")
s.kicker("Kodak's digital imaging patents", 192, 120, c("patents"))
s.dots(192, 190, 50, 22, 22, c("eleven|1,100|1100"), d=1.0, total=1100, shape="dot")
s.text("Once valued up to $2.6B", 186, 720, 110, color="grey", t=c("two|$2.6"))
s.source("Source: AppleInsider; Fox Business (Dec 2012)")

s, c = line_scene("They sold for about")
s.raw('<div id="k48-a" class="o0" style="position:absolute;left:192px;top:300px;width:1440px;height:110px;background:#C9C5BB"></div>'
      '<div id="k48-b" class="o0" style="position:absolute;left:192px;top:450px;width:291px;height:110px;background:#D7261E;transform-origin:0 50%"></div>',
      js=f"on('#k48-a', 0.2); tl.fromTo('#k48-b', {{ opacity: 1, scaleX: 0 }}, {{ scaleX: 1, duration: 0.5, ease: 'power3.out' }}, {c('five|$525'):.3f});")
s.kicker("Up to $2.6B, Kodak's own estimate", 192, 240, 0.2, "grey")
s.text("$525M", 520, 450, 120, color="red", t=c("five|$525"), mode="on")
s.source("Source: AppleInsider (Dec 2012)")

s, c = line_scene("The buyers were groups")
s.text("Apple", 186, 200, 300, t=c("apple"))
s.text("Google", 186, 520, 300, t=c("google"))
s.kicker("in the buying groups", 192, 860, c("groups"), "grey")

s, c = line_scene("The same Apple Kodak", hold=0.5)
s.text("$1B+ in royalties", 186, 300, 260, color="grey", t=0.1, mode="on")
s.strike(176, 420, 1500, c("billion", off=-0.3), 24)

s, c = line_scene("In September twenty thirteen")
s.kicker("September 3, 2013", 192, 250, c("september"))
s.text("A smaller Kodak", 186, 320, 260, t=c("smaller"))
s.kicker("focused on business customers", 192, 620, c("business"))
s.source("Source: Kodak announcement, via CBC")

# =========================== CHAPTER 5 ===========================
chapter("ch5", "The other film company", ["fujihq", "fujihq2", "p_film", "film120", "tower", "p_tower", "es1", "dc40", "brownie"], d=3.2)

s, c = line_scene("Kodak's great rival")
s.photos([("fujihq", 0)], rate=0.02, clicks=False)
s.raw('<div class="fill" style="background:linear-gradient(0deg,rgba(20,20,20,.85),rgba(20,20,20,0) 60%)"></div>')
s.text("Fujifilm", 186, 700, 260, color="np", t=c("fujifilm|fuji"))
s.source("Photo: Fujifilm HQ, Tokyo · Wikimedia Commons, CC0", light=True)

s, c = line_scene("Fujifilm squeezed")
for k, (w, lab) in enumerate([("squeezed", "Squeeze film"), ("prepared", "Prepare for digital"), ("whole|new", "Find new businesses")]):
    s.text(lab, 186, 160 + k * 260, 200, t=c(w))
    s.click(c(w))
s.source("Source: PetaPixel, “Why Kodak Died and Fujifilm Thrived”")

s, c = line_scene("In two thousand seven, it even launched")
s.kicker("2007 · Astalift skincare", 192, 200, c("two|2007"))
s.text("Film science", 186, 280, 220, t=c("antioxidant"))
s.text("→ skin science", 186, 520, 220, t=c("photographic"))
s.source("Sources: PetaPixel; Harvard D3 case post")

s, c = line_scene("Today, Fujifilm describes itself")
s.photos([("fujihq2", 0)], rate=0.02, clicks=False)
s.raw('<div class="fill" style="background:rgba(20,20,20,.6)"></div>')
for k, (w, lab) in enumerate([("healthcare", "Healthcare"), ("materials", "Materials"), ("imaging", "Imaging")]):
    s.text(lab, 186, 230 + k * 220, 190, color="np", t=c(w))
s.source("Photo: Fujifilm HQ, Tokyo Midtown · Wikimedia Commons, CC BY-SA 4.0", light=True)

# =========================== ENDING ===========================
s, c = line_scene("Kodak was not blind")
for k, (w, lab) in enumerate([("saw", "Saw it"), ("more", "Saw it again"), ("act", "Couldn't act")]):
    s.text(lab, 186, 160 + k * 260, 210, color="red" if k == 2 else "", t=c(w))

s, c = line_scene("Kodak invented the future", hold=0.8)
s.text("Kodak invented the future", 186, 230, 170, t=c("invented"))
s.text("It couldn't make it pay", 186, 480, 210, color="red", t=c("pay"))

s, c = line_scene("And that's the hardest kind", hold=1.0, punch=True)
s.text("Not the one you\ndon't see coming", 186, 160, 170, color="grey", t=c("not"))
s.text("The one you see,\nand can't afford", 186, 560, 200, t=c("see", 2))

end_card("This is Paper Empire", "Nokia", "The phone company that owned the world, and lost it in five years")
finish()
