# Nokia: "The Morning It Burned Its Own Platform" (Paper Empire). One block per voice line. Run: python3 build.py
import sys, os; sys.path.insert(0, os.path.abspath("../../kit"))
from build_lib import *
import build_lib; build_lib.GAP = 0.8

PH = "Photo: Wikimedia Commons (credits in description)"

# =========================== COLD OPEN ===========================
s, c = line_scene("In two thousand seven, one company")
s.kicker("2007 · phones sold worldwide", 192, 150, c("two|2007"))
s.dots(192, 240, 20, 5, 64, c("four|4"), d=0.6, shape="sq", color="#C9C5BB")
s.dots(192, 240, 20, 5, 64, c("ten|10", off=0.2), d=0.8, shape="sq", total=38)
s.text("≈38%", 1100, 600, 200, t=c("ten|10", off=0.6), mode="on")
s.text("4 in 10 phones", 186, 620, 170, t=c("ten|10", off=0.4))
s.source("Source: Nokia 2007 results (SEC 6-K)")

s, c = line_scene("It wasn't Apple.")
s.text("Apple", 186, 140, 200, color="grey", t=c("apple"))
s.strike(176, 230, 420, c("samsung", off=-0.2), 18)
s.text("Samsung", 186, 340, 200, color="grey", t=c("samsung"))
s.strike(176, 430, 560, c("nokia", off=-0.2), 18)
s.text("Nokia", 186, 560, 340, t=c("nokia"), mode="on")
s.kicker("A company from Finland", 192, 900, c("finland"))

s, c = line_scene("Six years later, Nokia sold", "ink")
s.photos([("hq", 0)], rate=0.015, clicks=False)
s.raw('<div class="fill" style="background:rgba(20,20,20,.5)"></div>')
sh = s.sheet(96, 560, 1728, 424, c("sold"), "bottom")
s.in_sheet(sh, "Nokia phones", 96, 60, 150, t=c("sold"))
s.in_sheet(sh, "→ Microsoft · 2013", 92, 230, 150, t=c("microsoft"))
s.source("Photo: Nokia HQ, Espoo · Wikimedia Commons, CC BY-SA 3.0", light=True)

s, c = line_scene("The story everyone tells")
s.kicker("The story everyone tells", 192, 160, c("story"), "grey")
s.text("The iPhone killed it", 186, 230, 240, t=c("iphone|i-phone"))
for k, (w, lab) in enumerate([("slow", "Too slow"), ("proud", "Too proud"), ("late", "Too late")]):
    s.text(lab, 186 + k * 520, 600, 150, color="grey", t=c(w))

s, c = line_scene("But in two thousand eleven")
s.text("The iPhone killed it", 186, 140, 150, color="grey", t=0.05, mode="on")
s.strike(176, 210, 1060, c("but"), 18)
s.kicker("2011 · four years after the iPhone", 192, 420, c("eleven|2011"))
s.text("Still No. 1", 186, 490, 320, t=c("biggest"), mode="on")
s.click(c("biggest"), "pop", 0.3)
s.source("Source: Bloomberg (2012): Nokia was the biggest phone maker from 1998 until Q1 2012")

s, c = line_scene("Then, in a single morning", "ink", hold=0.9, punch=True)
s.raw('<div id="n05-plat" class="o0" style="position:absolute;left:192px;top:620px;width:1536px;height:60px;background:#E9E6DF"></div>', js=f"on('#n05-plat', {c('own'):.3f});")
s.strike(560, 640, 260, c("finished"), 22)
s.strike(1000, 640, 320, c("finished", off=0.15), 22)
s.text("Its own software:\nfinished", 186, 200, 200, color="np", t=c("finished"))
s.kicker("Before the replacement existed", 192, 740, c("replacement"), "np")

s, c = line_scene("This is how the world's biggest", "ink", hold=0.6)
s.raw(f'<div id="n06-crown" class="o0" style="position:absolute;left:192px;top:300px">{CROWN_SVG.format(s=180)}</div>', js="on('#n06-crown', 0.25);")
s.kicker("Paper Empire", 410, 360, 0.3, "np")
s.text("Nokia", 186, 520, 320, color="np", t=c("company"))
s.kicker("The company that burned its own platform", 192, 840, c("burned"), "np")
s.click(c("company"), "impact", 0.4)

# =========================== CHAPTER 1 ===========================
chapter("ch1", "A paper mill in Finland", ["mill1894", "rapids", "nokiariver", "ad1936", "mill1894", "p_idestam", "rapids", "hq", "nokiariver"], d=3.2)

s, c = line_scene("The story starts in eighteen sixty-five")
photo_card(s, "p_idestam", 1180, 160, 520, 740, c("fredrik|frederick"), rot=-1.2)
s.kicker("1865", 192, 200, c("eighteen|1865"))
s.text("Fredrik Idestam", 186, 270, 170, t=c("fredrik|frederick"))
s.kicker("Mining engineer", 192, 470, c("mining"), "grey")
s.source("Portrait: Fredrik Idestam, public domain")

s, c = line_scene("He built a wood pulp mill")
s.photos([("rapids", 0)], rate=0.025)
s.raw('<div class="fill" style="background:linear-gradient(0deg,rgba(20,20,20,.85),rgba(20,20,20,0) 60%)"></div>')
s.kicker("Tampere, Finland", 192, 680, c("tampere"), "np")
s.text("A wood pulp mill", 186, 750, 170, color="np", t=c("pulp|wood"))
s.source("Photo: Tammerkoski rapids, Tampere · Wikimedia Commons, CC BY 3.0", light=True)

s, c = line_scene("A few years later, he opened")
s.photos([("mill1894", 0)], rate=0.02)
s.raw('<div class="fill" style="background:linear-gradient(0deg,rgba(20,20,20,.85),rgba(20,20,20,0) 55%)"></div>')
s.kicker("The Nokia mill, 1894", 192, 640, c("second"), "np")
s.text("Nokia", 186, 700, 260, color="np", t=c("nokia"), mode="on")
s.source("Photo: Nokia paper mill, 1894 · public domain", light=True)

s, c = line_scene("For most of the next century")
photo_card(s, "ad1936", 1100, 140, 640, 820, c("rubber"), rot=1.2, fit="cover")
for k, (w, lab) in enumerate([("paper", "Paper"), ("rubber", "Rubber boots"), ("tires|tyres", "Car tires"), ("cables", "Cables")]):
    s.text(lab, 186, 140 + k * 200, 170, t=c(w))
s.source("Image: Nokia advert, Helsinki 1936 · Wikimedia Commons, CC BY 4.0")

s, c = line_scene("In nineteen sixty-seven, three Finnish")
s.kicker("1967 · one Nokia Corporation", 192, 150, c("nineteen|1967"))
for k, (w, lab) in enumerate([("paper", "Paper"), ("rubber", "Rubber"), ("cable", "Cable")]):
    bid = s.i("blk")
    s.raw(f'<div id="{bid}" class="o0" style="position:absolute;left:{192 + k * 520}px;top:320px;width:480px;height:300px;background:#141414"><div class="lg np" style="position:absolute;left:36px;top:90px;font-size:150px">{lab}</div></div>',
          js=f"on('#{bid}', {c(w):.3f});")
s.text("= Nokia", 186, 700, 220, t=c("corporation"))

s, c = line_scene("The cable business led it")
s.text("Cables", 186, 200, 200, color="grey", t=c("cable"))
s.text("→ Electronics", 186, 420, 200, color="grey", t=c("electronics"))
s.text("→ Telephones", 186, 640, 200, t=c("telephones"))

s, c = line_scene("On July first, nineteen ninety-one")
s.kicker("1 July 1991 · Finland", 192, 160, c("july"))
s.text("The world's first\nGSM call", 186, 230, 220, t=c("first"))
s.kicker("Nokia helped build the network", 192, 740, c("helped"))
s.source("Sources: The Next Web (2011); Network World")

s, c = line_scene("Then, in nineteen ninety-two")
portrait(s, "p_ollila", "Jorma Ollila", "CEO from 1992", c("jorma"), pos="50% 20%")
s.kicker("1992", 192, 200, c("nineteen|1992"))
s.text("The biggest bet", 186, 270, 110, t=c("biggest"))
s.source("Photo: Jorma Ollila (2013) · Wikimedia Commons, CC BY-SA 3.0")

s, c = line_scene("He sold almost everything")
for k, (w, lab) in enumerate([("paper", "Paper"), ("rubber", "Rubber"), ("cables", "Cables"), ("televisions", "Televisions")]):
    s.text(lab, 186, 130 + k * 200, 170, color="grey", t=c(w))
    s.stamp("Sold", 900, 150 + k * 200, 90, c(w, off=0.2), rot=-4, ink=True, sound=k == 0)

s, c = line_scene("Nokia would be a phone company", hold=0.5)
s.text("Phones.", 186, 260, 420, t=c("phone"), mode="on")
s.kicker("Nothing else", 192, 760, c("nothing"))

# =========================== CHAPTER 2 ===========================
chapter("ch2", "A phone in every pocket", ["p_n3310", "p_n1100", "p_n6110", "p_n95", "n95open", "hq2", "p_n3310", "p_n1100", "hq"], d=3.2)

s, c = line_scene("The bet paid off faster")
s.kicker("1998 · world's biggest phone makers", 192, 150, c("nineteen|1998"))
for k, (lab, wd, col) in enumerate([("Motorola", 1100, "#C9C5BB"), ("Nokia", 1400, "#141414")]):
    bid = s.i("bar")
    s.raw(f'<div id="{bid}" class="o0" style="position:absolute;left:192px;top:{300 + k * 230}px;width:{wd}px;height:170px;background:{col};transform-origin:0 50%"></div>',
          js=f"tl.fromTo('#{bid}', {{ opacity: 1, scaleX: 0 }}, {{ scaleX: 1, duration: 0.9, ease: 'power2.out' }}, {c('motorola') + k * 0.25:.3f});")
    s.text(lab, 230, 310 + k * 230, 130, color="np" if k else "", t=c("motorola") + k * 0.25 + 0.4, mode="on")
s.text("No. 1", 1640 - 300, 820, 150, t=c("biggest"))
s.source("Sources: CNN Money (Feb 1999); Fortune (2000) · bar lengths illustrative")

s, c = line_scene("It would hold that title")
s.dots(192, 360, 14, 1, 110, c("fourteen|14"), d=0.9, shape="sq")
s.text("14 years", 186, 560, 240, t=c("fourteen|14", off=0.6))

s, c = line_scene("Nokia phones were simple")
photo_card(s, "p_n3310", 1100, 120, 420, 840, c("simple"), rot=-1.5)
for k, (w, lab) in enumerate([("simple", "Simple"), ("tough", "Tough"), ("cheap", "Cheap")]):
    s.text(lab, 186, 180 + k * 240, 200, t=c(w))
s.source(PH)

s, c = line_scene("In nineteen ninety-seven, the Nokia sixty-one ten")
photo_card(s, "p_n6110", 1180, 120, 480, 840, c("nokia"), rot=1.2)
cells = "".join(f'<div class="n20s" style="position:absolute;left:{x * 46}px;top:{y * 46}px;width:40px;height:40px;background:#141414;opacity:0"></div>' for x, y in [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(5,1),(5,2),(5,3),(4,3),(3,3),(2,3),(2,4),(2,5)])
s.raw(f'<div style="position:absolute;left:192px;top:520px;width:300px;height:300px">{cells}</div>',
      js=f"tl.fromTo('#root .n20s', {{ opacity: 0 }}, {{ opacity: 1, duration: 0.001, stagger: 0.12 }}, {c('snake'):.3f});")
s.kicker("1997 · Nokia 6110", 192, 180, c("nineteen|1997"))
s.text("Snake", 186, 250, 260, t=c("snake"))
s.source("Photo: Nokia 6110 · Wikimedia Commons, CC BY-SA 4.0")

s, c = line_scene("The Nokia thirty-three ten")
photo_card(s, "p_n3310", 1200, 120, 440, 840, 0.3, rot=-1.5)
s.kicker("Nokia 3310 · units sold", 192, 220, c("thirty|3310|33"))
s.count(186, 300, 260, c("hundred|126"), 126000000, INT, d=1.5)
s.source("Source: Nokia 3310 sales figures (widely reported) · " + PH)

s, c = line_scene("The Nokia eleven hundred")
photo_card(s, "p_n1100", 1200, 120, 440, 840, 0.3, rot=1.2)
s.kicker("Nokia 1100 · units sold", 192, 160, c("eleven|1100"))
s.count(186, 240, 230, c("two|250"), 250000000, "v => Math.round(v).toLocaleString('en-US') + '+'", d=1.5)
s.stamp("Guinness record", 200, 560, 110, c("guinness"), rot=-4, ink=True)
s.kicker("Best-selling mobile phone ever", 192, 800, c("best"))
s.source("Source: Guinness World Records · " + PH)

s, c = line_scene("In Lagos, in Delhi")
for k, (w, lab) in enumerate([("lagos", "Lagos"), ("delhi", "Delhi"), ("jakarta", "Jakarta")]):
    s.text(lab, 186 + k * 520, 220, 200, t=c(w))
s.text("Their first phone\nwas a Nokia", 186, 520, 210, t=c("first"))

s, c = line_scene("And Nokia was already selling smartphones")
photo_card(s, "n95open", 1060, 160, 680, 680, c("converged|devices"), rot=-1.2, fit="cover")
s.kicker("2007 · 'converged devices'", 192, 180, c("two|2007"))
s.count(186, 250, 280, c("sixty|60"), 60.5, "v => v.toFixed(1) + 'M'", d=1.3)
for k, (w, lab) in enumerate([("photos", "Photos"), ("music", "Music"), ("web", "Web")]):
    s.text(lab, 186 + k * 300, 620, 100, color="grey", t=c(w))
s.source("Source: Nokia in 2007 (annual report) · Photo: Nokia N95, Wikimedia Commons, CC BY-SA 4.0")

s, c = line_scene("They ran on Nokia's own software")
photo_card(s, "p_n95", 1200, 120, 460, 840, 0.2, rot=1.2)
s.raw('<div id="n25-f" class="o0" style="position:absolute;left:192px;top:640px;width:880px;height:120px;background:#141414"></div>', js=f"tl.fromTo('#n25-f', {{ opacity: 1, scaleX: 0 }}, {{ scaleX: 1, transformOrigin: '0 50%', duration: 0.6, ease: 'power3.out' }}, {c('symbian'):.3f});")
s.text("Symbian", 186, 360, 280, t=c("symbian"))
s.kicker("Nokia's own software", 192, 800, c("software"))

s, c = line_scene("That year, Nokia shipped four hundred")
s.kicker("2007 · devices shipped", 192, 150, c("year"))
s.count(186, 230, 300, c("four|437"), 437000000, INT, d=1.5)
s.text("≈ €51 billion in sales", 186, 640, 160, t=c("fifty|51"))
s.kicker("all of Nokia, not just phones", 192, 840, c("whole"), "grey")
s.source("Sources: Nokia 2007 results; Nokia in 2007 annual report")

# =========================== CHAPTER 3 ===========================
chapter("ch3", "The screen without buttons", ["iphone2007", "iphones", "p_n95", "n95open", "p_n3310", "hq", "iphone2007", "p_n1100", "hq2"], d=3.2)

s, c = line_scene("In January two thousand seven, Apple", "ink")
s.photos([("iphone2007", 0)], rate=0.02, clicks=False)
s.raw('<div class="fill" style="background:linear-gradient(0deg,rgba(20,20,20,.88),rgba(20,20,20,0) 60%)"></div>')
s.kicker("January 2007", 192, 700, c("january"), "np")
s.text("The iPhone", 186, 770, 200, color="np", t=c("iphone|i-phone"))
s.source("Photo: first iPhone, Macworld 2007 · Wikimedia Commons, CC BY-SA 4.0 · Source: Apple", light=True)

s, c = line_scene("It had no keyboard")
keys = "".join(f'<div class="n28k" style="position:absolute;left:{40 + (k % 3) * 120}px;top:{430 + (k // 3) * 90}px;width:100px;height:70px;background:#141414"></div>' for k in range(12))
s.raw(f'<div style="position:absolute;left:1200px;top:110px;width:440px;height:860px;border:14px solid #141414;border-radius:56px">{keys}</div>',
      js=f"tl.fromTo('#root .n28k', {{ opacity: 1 }}, {{ opacity: 0, duration: 0.001, stagger: 0.04, immediateRender: false }}, {c('keyboard'):.3f});")
s.text("No keyboard", 186, 220, 220, t=c("keyboard"))
s.text("One button", 186, 460, 220, color="grey", t=c("button"))
s.text("A screen you touch", 186, 700, 170, t=c("screen"))

s, c = line_scene("Less than two years later")
s.kicker("2008", 192, 300, c("less|two"))
s.text("Android", 186, 370, 340, t=c("android"), mode="on")
s.kicker("Google's software, on many companies' phones", 192, 760, c("google"))
s.source("Source: T-Mobile G1 launch (Oct 2008)")

s, c = line_scene("Suddenly, a phone wasn't just hardware")
for k, (w, lab, col) in enumerate([("hardware", "Hardware", "grey"), ("software", "Software", ""), ("apps", "Apps", ""), ("developers", "Developers", "")]):
    s.text(lab, 186, 120 + k * 210, 180, color=col, t=c(w))

s, c = line_scene("Nokia knew how to build phones")
photo_card(s, "p_n95", 1200, 120, 460, 840, 0.3, rot=-1.2)
s.text("Best hardware", 186, 200, 200, t=c("build"))
s.text("Symbian: built for\nan older kind of phone", 186, 460, 150, color="grey", t=c("symbian"))
s.text("Slow and hard to change", 186, 800, 110, t=c("slow"))

s, c = line_scene("Nokia was still selling enormous")
s.text("Still selling\nenormous numbers", 186, 160, 190, t=c("enormous"))
s.text("But the high end\nwas moving", 186, 560, 190, color="grey", t=c("profitable"))

s, c = line_scene("In September twenty ten, Nokia hired")
portrait(s, "p_elop", "Stephen Elop", "CEO from Sept 2010", c("stephen"), pos="50% 25%")
s.kicker("First non-Finnish CEO", 192, 200, c("outside"))
s.text("From Microsoft", 186, 270, 120, t=c("microsoft"))
s.source("Photo: Stephen Elop · Wikimedia Commons, CC BY-SA 2.0")

# =========================== CHAPTER 4 ===========================
chapter("ch4", "The burning platform", ["elop", "p_elop", "lumia", "hq", "iphone2007", "p_n95", "hq2", "p_lumia", "iphones"], d=3.2)

s, c = line_scene("Five months later, on February eighth")
s.quote(960, 150, 760, 700, "INTERNAL MEMO · FEB 8 2011", "From: Stephen Elop. To: all Nokia staff", "Leaked to the press, published in full by Engadget", c("memo"), qsize=100)
s.kicker("February 8, 2011", 192, 220, c("february"))
s.stamp("Leaked", 200, 330, 200, c("leaked"), rot=-6, ink=True)
s.source("Source: Engadget (Feb 8 2011)")

s, c = line_scene("In it, he compared Nokia")
plat = ('<svg id="n35-p" class="o0" style="position:absolute;left:1040px;top:180px" width="700" height="700" viewBox="0 0 700 700">'
        '<rect x="80" y="300" width="540" height="40" fill="#141414"/><rect x="140" y="340" width="24" height="320" fill="#141414"/><rect x="536" y="340" width="24" height="320" fill="#141414"/>'
        '<rect x="330" y="340" width="24" height="320" fill="#141414"/><rect x="200" y="120" width="300" height="180" fill="#141414"/>'
        '<path id="n35-f" d="M260 120 C 240 60 300 40 290 0 C 340 40 380 50 360 120 Z" fill="#D7261E" opacity="0"/>'
        '<rect x="0" y="640" width="700" height="60" fill="#C9C5BB"/></svg>')
s.raw(plat, js=f"on('#n35-p', {c('oil'):.3f}); on('#n35-f', {c('burning'):.3f});")
s.text("Stay, and burn", 186, 280, 180, t=c("stay"))
s.text("Or jump into\nfreezing water", 186, 520, 180, t=c("jump"))
s.source("Source: the memo, as published by Engadget (2011)")

s, c = line_scene("His message was clear")
s.text("“Our platform\nis burning”", 186, 260, 260, t=c("platform"))
s.kicker("— the memo's message", 192, 760, c("fire"), "grey")

s, c = line_scene("The memo didn't hold back")
s.quote(192, 160, 1536, 640, "THE MEMO · STEPHEN ELOP, 2011", "“The first iPhone shipped in 2007, and we still don't have a product that is close to their experience.”", "Published by Engadget, Feb 8 2011", c("first"), qsize=110)

s, c = line_scene("He wrote that Android had just taken")
s.text("Android: many makers", 186, 220, 190, t=c("android"))
s.text("Nokia: one", 186, 460, 190, color="grey", t=c("one"))
s.kicker("Android had just taken the lead in smartphone volumes", 192, 760, c("lead"))

s, c = line_scene("At the cheap end")
s.quote(192, 180, 1536, 600, "THE MEMO, ON CHINESE MANUFACTURERS", "“They are fast, they are cheap, and they are challenging us.”", "Stephen Elop, Feb 2011", c("they"), qsize=130)

s, c = line_scene("And he named the real fight")
s.text("Devices", 186, 220, 240, color="grey", t=c("devices"))
s.strike(176, 330, 540, c("become"), 18)
s.text("→ ecosystems", 186, 520, 240, t=c("ecosystems"))
s.kicker("“The battle of devices has now become a war of ecosystems”", 192, 820, c("war"))

s, c = line_scene("Then the line that made headlines", hold=0.6)
s.quote(192, 180, 1536, 600, "THE LINE THAT MADE HEADLINES", "“We poured gasoline on our own burning platform.”", "Stephen Elop, internal memo, Feb 2011", c("poured"), qsize=140)

s, c = line_scene("Three days later, Nokia made its jump")
s.kicker("February 11, 2011", 192, 300, c("three|3"))
s.text("The jump", 186, 370, 340, t=c("jump"), mode="on")

s, c = line_scene("It announced a partnership with Microsoft")
s.text("Nokia + Microsoft", 186, 220, 230, t=c("microsoft"))
s.text("Windows Phone", 186, 520, 230, t=c("windows"))
s.kicker("Nokia's main smartphone software from now on", 192, 800, c("main"))
s.source("Source: Nokia stock exchange release, Feb 11 2011 (SEC)")

s, c = line_scene("And Symbian, the software running")
s.text("Symbian", 186, 300, 340, t=c("symbian"), mode="on")
s.stamp("Phased out", 200, 640, 180, c("phased"), rot=-5)
s.source("Source: Nokia, Feb 11 2011")

s, c = line_scene("Nokia itself counted around two hundred")
s.kicker("People using Symbian phones", 192, 160, c("symbian"))
s.count(186, 240, 300, c("two|200"), 200000000, INT, d=1.4)
s.stamp("No future", 300, 640, 170, c("future"), rot=-4, ink=True)
s.source("Source: Nokia strategy release, Feb 11 2011")

s, c = line_scene("That day, Nokia's shares fell")
line = '<svg id="n46-ch" class="o0" style="position:absolute;left:192px;top:200px" width="1536" height="600" viewBox="0 0 1536 600"><path id="n46-l" d="M0 120 L 700 140 L 760 470 L 1536 500" stroke="#D7261E" stroke-width="16" fill="none" pathLength="100" stroke-dasharray="100 120" stroke-dashoffset="100"/></svg>'
s.raw(line, js=f"on('#n46-ch', {c('shares'):.3f}); tl.fromTo('#n46-l', {{ strokeDashoffset: 100 }}, {{ strokeDashoffset: 0, duration: 1.0, ease: 'power2.in' }}, {c('shares'):.3f});")
s.text("−10%+ in one day", 186, 760, 170, color="red", t=c("ten|10"))
s.source("Sources: Fortune (−12%); Bloomberg via gHacks (−14%), Feb 11 2011 · line illustrative")

s, c = line_scene("There was a problem")
s.kicker("February 2011", 192, 300, c("problem"))
s.text("Now", 186, 370, 240, t=c("problem"))
s.hrule(520, 480, 500, c("months"), h=14, color="#D7261E")
s.text("Late 2011", 1060, 370, 200, t=c("months", off=0.4))
s.kicker("The first Nokia Windows phones", 192, 680, c("windows"))

s, c = line_scene("So Nokia was telling its customers")
s.raw('<div id="n48-a" class="o0" style="position:absolute;left:192px;top:240px;width:700px;height:520px;border-bottom:14px solid #141414"></div>', js=f"on('#n48-a', {c('shelf'):.3f});")
photo_card(s, "p_n95", 330, 270, 260, 470, c("shelf"), rot=0)
s.stamp("No future", 240, 120, 100, c("future"), rot=-6, ink=True, sound=False)
s.raw('<div id="n48-b" class="o0" style="position:absolute;left:1028px;top:240px;width:700px;height:520px;border-bottom:14px solid #141414"></div>', js=f"on('#n48-b', {c('nothing'):.3f});")
s.text("Nothing new to sell", 1030, 820, 110, color="red", t=c("nothing"))

s, c = line_scene("Business writers have a name")
s.text("The Osborne effect", 186, 220, 240, t=c("osborne|osborn"))
s.text("Announce too early,\nsales stop now", 186, 520, 190, color="grey", t=c("announce"))

s, c = line_scene("In the second quarter of twenty eleven")
s.kicker("Q2 2011 · Nokia smartphones vs a year earlier", 192, 160, c("second"))
s.raw('<div id="n50-a" class="o0" style="position:absolute;left:192px;top:300px;width:1500px;height:150px;background:#C9C5BB"></div>'
      '<div id="n50-b" class="o0" style="position:absolute;left:192px;top:500px;width:1000px;height:150px;background:#D7261E;transform-origin:0 50%"></div>',
      js=f"on('#n50-a', {c('second'):.3f}); tl.fromTo('#n50-b', {{ opacity: 1, scaleX: 0 }}, {{ scaleX: 1, duration: 0.7, ease: 'power3.out' }}, {c('third'):.3f});")
s.text("−⅓", 1240, 470, 200, color="red", t=c("third", off=0.5), mode="on")
s.kicker("units −34% · sales −32%", 192, 720, c("third", off=0.3))
s.source("Source: Nokia Q2 2011 interim report")

s, c = line_scene("That same quarter, Apple and Samsung")
s.kicker("Q2 2011 · smartphones shipped (Strategy Analytics)", 192, 140, c("quarter"))
for k, (lab, wd, col, w) in enumerate([("Apple 20.3M", 1400, "#141414", "apple"), ("Samsung 19.2M", 1324, "#141414", "samsung"), ("Nokia 16.7M", 1152, "#D7261E", "nokia")]):
    bid = s.i("bar")
    s.raw(f'<div id="{bid}" class="o0" style="position:absolute;left:192px;top:{260 + k * 220}px;width:{wd}px;height:160px;background:{col};transform-origin:0 50%"></div>',
          js=f"tl.fromTo('#{bid}', {{ opacity: 1, scaleX: 0 }}, {{ scaleX: 1, duration: 0.6, ease: 'power3.out' }}, {c(w):.3f});")
    s.text(lab, 230, 285 + k * 220, 110, color="np", t=c(w, off=0.3), mode="on")
s.source("Source: Strategy Analytics via Business Wire (July 2011)")

# =========================== CHAPTER 5 ===========================
chapter("ch5", "The end of a 14-year reign", ["lumia", "p_lumia", "hq", "hq2", "elop", "p_elop", "iphones", "p_n1100", "p_n3310"], d=3.2)

s, c = line_scene("At the end of two thousand eleven")
s.photos([("lumia", 0)], rate=0.02, clicks=False)
s.raw('<div class="fill" style="background:linear-gradient(0deg,rgba(20,20,20,.88),rgba(20,20,20,0) 60%)"></div>')
s.kicker("Late 2011", 192, 700, c("end"), "np")
s.text("Lumia", 186, 770, 240, color="np", t=c("lumia"))
s.source("Photo: Nokia Lumia · Wikimedia Commons, CC BY-SA 3.0", light=True)

s, c = line_scene("Reviewers liked the design")
s.text("Liked the design", 186, 160, 200, t=c("liked|like"))
s.text("The apps were elsewhere", 186, 460, 170, color="grey", t=c("apps"))
s.text("Buyers had moved on", 186, 700, 170, t=c("moved"))

s, c = line_scene("In the first quarter of twenty twelve")
s.dots(192, 300, 14, 1, 110, 0.1, d=0.01, shape="sq")
rid = s.i("last")
s.raw(f'<div id="{rid}" class="o0" style="position:absolute;left:{192 + 13 * 110}px;top:300px;width:79px;height:79px;background:#D7261E"></div>', js=f"on('#{rid}', {c('samsung'):.3f});")
s.text("Samsung takes No. 1", 186, 480, 220, t=c("samsung"))
s.kicker("Q1 2012 · the end of Nokia's 14-year run", 192, 760, c("fourteen|14"))
s.source("Source: Bloomberg / Strategy Analytics (April 2012)")

s, c = line_scene("By two thousand thirteen, Nokia's share")
ln = '<svg id="n55-ch" class="o0" style="position:absolute;left:192px;top:180px" width="1536" height="620" viewBox="0 0 1536 620"><path id="n55-l" d="M60 80 L 1440 520" stroke="#D7261E" stroke-width="16" fill="none" pathLength="100" stroke-dasharray="100 120" stroke-dashoffset="100"/></svg>'
s.raw(ln, js=f"on('#n55-ch', {c('two|2013'):.3f}); tl.fromTo('#n55-l', {{ strokeDashoffset: 100 }}, {{ strokeDashoffset: 0, duration: 1.0, ease: 'power2.in' }}, {c('fallen'):.3f});")
s.text("38% · 2007", 222, 150, 150, t=c("thirty|38"))
s.text("≈14%", 1380, 720, 160, color="red", t=c("fourteen|14"))
s.kicker("2013", 1390, 900, c("fourteen|14"))
s.source("Sources: Nokia annual reports; Strategy Analytics; Statista")

s, c = line_scene("On September third, twenty thirteen")
s.kicker("September 3, 2013", 192, 150, c("september"))
s.text("Microsoft buys Nokia's phones", 186, 220, 170, t=c("microsoft"))
s.text("€3.79B devices", 186, 460, 150, color="grey", t=c("phone"))
s.text("+ €1.65B patents", 186, 620, 150, color="grey", t=c("patents"))
s.text("= €5.44B", 186, 780, 170, t=c("five|5.44|€5"))
s.source("Source: Microsoft announcement, Sept 3 2013")

s, c = line_scene("Stephen Elop, the man who wrote")
portrait(s, "p_elop", "Stephen Elop", "Wrote the memo", 0.2, pos="50% 25%")
s.text("Back to Microsoft", 186, 220, 110, t=c("microsoft"))
s.source("Source: Microsoft / Nokia (2013–14)")

s, c = line_scene("It didn't work for Microsoft either")
s.kicker("July 2015 · Microsoft", 192, 160, c("july"))
s.count(186, 230, 300, c("seven|$7"), 7.6, "v => '−$' + v.toFixed(1) + 'B'", color="red", d=1.2)
s.text("up to 7,800 jobs cut", 186, 620, 170, t=c("thousand|7,800|job"))
s.source("Source: TechCrunch (July 8 2015)")

# =========================== CHAPTER 6 ===========================
chapter("ch6", "The company that survived", ["p_tower", "hq", "hq2", "mill1894", "rapids", "p_ollila", "ad1936", "nokiariver", "p_tower"], d=3.2)

s, c = line_scene("Here's the part most people miss", hold=0.5)
s.text("Nokia didn't die.", 186, 340, 280, t=c("didn't|die"), mode="on")
s.flash(c("didn't|die", off=-0.05))

s, c = line_scene("It kept the business it had built")
photo_card(s, "p_tower", 1180, 120, 520, 840, c("networks"), rot=1.2, fit="cover")
s.text("The networks\nphones run on", 186, 300, 210, t=c("networks"))
s.source("Photo: cell tower · Wikimedia Commons, CC BY-SA 4.0")

s, c = line_scene("In two thousand sixteen, it bought")
s.photos([("hq2", 0)], rate=0.015, clicks=False)
sh = s.sheet(96, 560, 1728, 424, c("bought"), "bottom")
s.in_sheet(sh, "Nokia buys Alcatel-Lucent", 96, 60, 140, t=c("alcatel"))
s.in_sheet(sh, "≈ €15.6 billion · 2016", 92, 230, 150, t=c("fifteen|15"))
s.source("Source: Nokia 20-F 2016 (SEC) · Photo: Nokia HQ, Wikimedia Commons, CC BY-SA 3.0", light=True)

s, c = line_scene("Today, Nokia builds the mobile networks")
s.text("Today: networks", 186, 220, 240, t=c("networks"))
s.kicker("For operators around the world", 192, 520, c("operators"))

s, c = line_scene("A paper mill became a rubber company")
for k, (w, lab, nth) in enumerate([("paper", "Paper mill", 1), ("rubber", "→ Rubber", 1), ("phone", "→ Phone giant", 1), ("network", "→ Networks", 1)]):
    s.text(lab, 186, 110 + k * 210, 180, color="" if k == 3 else "grey", t=c(w, nth))

s, c = line_scene("Reinventing itself is the one thing", hold=0.4)
s.text("Reinventing itself", 186, 300, 260, t=c("reinventing"))

# =========================== ENDING ===========================
s, c = line_scene("The iPhone didn't kill Nokia's phones")
s.text("Still on top,\nfour years later", 186, 260, 240, t=c("still"))

s, c = line_scene("What finished them was a decision", "ink", punch=True)
s.raw('<div id="n66-plat" class="o0" style="position:absolute;left:192px;top:620px;width:1536px;height:60px;background:#E9E6DF"></div>', js=f"on('#n66-plat', 0.1);")
s.strike(700, 640, 400, c("dead"), 22)
s.text("A decision", 186, 240, 280, color="np", t=c("decision"))

s, c = line_scene("The lesson isn't")
s.text("Change", 186, 260, 300, color="grey", t=c("change", 2))
s.text("Timing", 186, 560, 300, t=c("timing"))

s, c = line_scene("Elop's memo was right")
s.text("The platform was burning", 186, 220, 180, t=c("burning"))
s.text("The announcement\nadded gasoline", 186, 480, 210, color="grey", t=c("gasoline"))

s, c = line_scene("Before you burn the platform", hold=1.0)
s.text("Before you burn the platform", 186, 220, 170, t=c("before"))
s.text("make sure the next one\ncan hold your weight", 186, 480, 210, t=c("next"))

end_card("This is Paper Empire", 'Toys "R" Us', "The toy store every kid dreamed about, and the deal that buried it")
finish()
