# Builds every scene + index.html for "Blockbuster: They Saw It Coming" (Paper Empire).
# One scene per voice line; chapter cards between chapters. Cue times come from the
# per-line Whisper word timings, so every graphic lands on the word that names it.
import json, os, re, subprocess, sys
sys.path.insert(0, os.path.abspath("../../kit"))
from kit import Scene, CROWN_SVG, F

LEAD = 0.2          # voice starts this far into its scene
GAP = 0.7           # silence after each line
os.makedirs("compositions", exist_ok=True)
lines = [l.split("|", 1) for l in open("../lines.txt").read().strip().splitlines()]
TEXT = {k: v for k, v in lines}
IDS = [k for k, _ in lines]

def dur(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout)

def L(prefix):
    for k, v in lines:
        if v.startswith(prefix): return k
    raise KeyError(prefix)

class Cue:
    def __init__(self, lid):
        self.lid = lid
        self.words = json.load(open(f"assets/vo/{lid}.words.json"))
        self.vo = dur(f"assets/vo/{lid}.wav")
    def __call__(self, word, nth=1, off=0.0):
        hits = []
        for w in [re.sub(r"[^\w$.%-]", "", q) for q in word.lower().split("|")]:
            hits = [x for x in self.words if re.sub(r"[^\w$.%-]", "", x["text"].lower()).startswith(w)]
            if len(hits) >= nth: break
        if len(hits) < nth:
            raise KeyError(f"{self.lid}: '{word}' #{nth} not in: " + " ".join(x["text"] for x in self.words))
        return round(LEAD + hits[nth - 1]["start"] + off, 3)
    def end(self, off=0.0):
        return round(LEAD + self.vo + off, 3)

timeline = []   # (scene, vo_id or None)
def line_scene(prefix, ground="paper", hold=0.0):
    lid = L(prefix); c = Cue(lid)
    s = Scene(lid.lower(), LEAD + c.vo + GAP + hold, ground)
    timeline.append((s, lid))
    return s, c

def card_scene(sid, d, ground="ink"):
    s = Scene(sid, d, ground); timeline.append((s, None)); return s

INT = "v => Math.round(v).toLocaleString('en-US')"
def money(prefix="$", suffix=""):
    return f"v => '{prefix}' + Math.round(v).toLocaleString('en-US') + '{suffix}'"

def chapter(sid, title, imgs, d=2.6):
    s = card_scene(sid, d, "ink")
    tend = s.tiles(imgs, 0.05)
    s.raw(f'<div id="{sid}-band" class="o0" style="position:absolute;left:0;top:380px;width:1920px;height:320px;background:#141414"></div>')
    s.js.append(f"on('#{sid}-band', {tend + 0.15:.3f});")
    s.text(title, 192, 432, 230, color="np", t=tend + 0.2, d=0.35)
    s.click(tend + 0.15, "impact", 0.35)
    return s

def portrait(s, img, name, role, t, pos="50% 22%", side="right", until=None):
    x = 860 if side == "right" else 0
    s.raw(f'<div id="{s.sid}-pw" class="o0" style="position:absolute;left:{x}px;top:0;width:1060px;height:1080px;overflow:hidden">'
          f'<img id="{s.sid}-pi" src="assets/img/{img}.jpg" style="width:1060px;height:1080px;object-fit:cover;object-position:{pos}" alt=""></div>',
          js=f"on('#{s.sid}-pw', {t:.3f}); push('#{s.sid}-pi', {t:.3f}, {s.dur - t:.3f}, 1, 1.05);")
    tx = 192 if side == "right" else 1150
    k = s.kicker(role, tx, 600, t + 0.15, "grey")
    n = s.text(name, tx - 6, 660, 170, t=t + 0.1)
    s.click(t)
    if until is not None:
        s.js.append(f"off('#{s.sid}-pw', {until:.3f}); off('#{k}', {until:.3f}); off('#{n}', {until:.3f});")

CC = "Photo: Wikimedia Commons (credits in description)"

# =========================== COLD OPEN ===========================
s, c = line_scene("In the year two thousand", "ink")
s.photos([("dallas", 0)], rate=0.012)
s.raw('<div class="fill" style="background:linear-gradient(90deg,rgba(20,20,20,.82) 0%,rgba(20,20,20,.55) 45%,rgba(20,20,20,0) 75%)"></div>')
s.kicker("Dallas · 2000", 192, 330, c("dallas"), "np")
s.text("Sell the company", 186, 400, 210, color="np", t=c("sell"))
s.text("$50 million", 186, 600, 300, color="np", t=c("fifty"), mode="on")
s.click(c("fifty"), "pop", 0.3)
s.source(CC, light=True)

s, c = line_scene("The company was called Netflix")
s.raw('<img id="l01-logo" class="o0" src="assets/img/nflogo.png" style="position:absolute;left:192px;top:200px;width:760px" alt="">', js=f"on('#l01-logo', {c('netflix'):.3f});")
s.click(c("netflix"))
s.raw(f'<div id="l01-env" class="o0" style="position:absolute;left:1060px;top:150px;width:700px;height:430px;overflow:hidden;box-shadow:0 14px 30px rgba(0,0,0,.25)"><img src="assets/img/nfenv.jpg" style="width:100%;height:100%;object-fit:cover" alt=""></div>',
      js=f"tl.fromTo('#l01-env', {{ opacity: 1, x: 300, rotation: 4 }}, {{ x: 0, rotation: 2, duration: 0.5, ease: 'expo.out' }}, {c('mailed'):.3f});")
s.click(c("mailed"))
s.kicker("DVDs by mail · 1999–2000", 1060, 610, c("dvds"))
s.text("Losing money fast", 186, 700, 200, color="red", t=c("losing"))
s.source("Source: Marc Randolph, That Will Never Work (2019) · envelope: Wikimedia Commons, CC BY 2.5")

s, c = line_scene("The buyer was Blockbuster", "ink")
t1 = s.tiles(["st0", "st4", "st6", "st10", "st5", "st11", "st7", "st9", "st8"], c("blockbuster"))
s.raw(f'<div id="l02-band" class="o0" style="position:absolute;left:0;top:740px;width:1920px;height:240px;background:#141414"></div>', js=f"on('#l02-band', {c('biggest'):.3f});")
s.text("The biggest video chain on Earth", 192, 776, 160, color="np", t=c("biggest"))
s.raw(f'<div id="l02-q" class="o0 fill" style="background:#E9E6DF"><img class="paper" src="assets/paper.jpg" alt=""></div>', js=f"on('#l02-q', {c('by'):.3f});")
s.click(c("by"))
portrait(s, "antioco", "John Antioco", "Blockbuster CEO", c("by") + 0.001, pos="50% 18%")
s.text("“Trying not\nto laugh”", 186, 160, 150, t=c("laugh", off=-0.4))
s.kicker("— Marc Randolph's account", 192, 440, c("laugh"), "grey")
s.source("Photo: John F Antioco, Wikimedia Commons, CC BY-SA 4.0")

s, c = line_scene("Blockbuster said no.", "ink", hold=0.8)
s.text("No.", 640, 160, 760, color="np", t=c("no"), mode="on")
s.click(c("no"), "impact", 0.55)

s, c = line_scene("Today, Netflix has")
s.kicker("Netflix · paid memberships · end of 2024", 192, 170, c("netflix"))
s.count(186, 250, 260, c("three|300"), 301630000, INT, d=1.6)
s.raw(f'<div id="l04-half" class="o0" style="position:absolute;left:0;top:560px;width:1920px;height:520px;overflow:hidden"><img id="l04-bend" src="assets/img/bd7.jpg" style="width:1920px;height:1080px;object-fit:cover;object-position:50% 45%;margin-top:-280px" alt=""></div>',
      js=f"on('#l04-half', {c('blockbuster'):.3f}); push('#l04-bend', {c('blockbuster'):.3f}, 4, 1, 1.05);")
s.click(c("blockbuster"))
s.raw(f'<div id="l04-one" class="o0" style="position:absolute;left:192px;top:600px;background:#141414;padding:30px 60px 0"><div class="lg np" style="font-size:380px">1</div></div>', js=f"on('#l04-one', {c('one'):.3f});")
s.el("Store left: Bend, Oregon", "left:560px;top:880px;background:#141414;padding:14px 22px", "kick np", c("bend"))
s.el("Sources: Netflix Q4 2024 letter (SEC); The Last Blockbuster, Bend OR · Photo: Wikimedia Commons, CC0", "left:192px;bottom:72px", "src np", c("blockbuster"))

s, c = line_scene("That's the story everyone tells")
s.kicker("The story everyone tells", 192, 220, c("story"), "grey")
s.text("The dinosaur that\nlaughed at the future", 186, 300, 230, t=c("dinosaur"))

s, c = line_scene("But it isn't what happened")
s.text("The dinosaur that\nlaughed at the future", 186, 120, 150, color="grey", t=0.0, mode="on")
s.strike(170, 178, 1130, c("isn't"), 18)
s.strike(170, 310, 1300, c("isn't", off=0.15), 18)
s.text("Saw the future", 186, 420, 180, t=c("saw"))
s.text("Built it", 186, 600, 180, t=c("built"))
s.text("Was winning", 186, 780, 180, color="", t=c("winning"))

s, c = line_scene("And then it pushed out", hold=0.6)
portrait(s, "antioco", "John Antioco", "The man who built it", 0.05, pos="50% 18%")
s.stamp("Pushed out", 200, 220, 150, c("pushed"))

s, c = line_scene("This is how Blockbuster lost", "ink", hold=0.6)
s.raw(f'<div id="l08-crown" class="o0" style="position:absolute;left:192px;top:300px">{CROWN_SVG.format(s=180)}</div>', js=f"on('#l08-crown', 0.25);")
s.kicker("Paper Empire", 410, 360, 0.3, "np")
s.text("Blockbuster", 186, 520, 300, color="np", t=c("blockbuster"))
s.kicker("How it lost a war it was winning", 192, 820, c("lost"), "np")
s.click(c("blockbuster"), "impact", 0.4)

# =========================== CHAPTER 1 ===========================
chapter("ch1", "A store every 24 hours", ["st10", "vhs0", "st3", "st0", "st2", "st5", "st11", "st1", "st4"])

s, c = line_scene("October nineteenth")
s.stamp("Oct 19, 1985", 192, 160, 200, c("october"), rot=-3, ink=True)
s.kicker("Dallas, Texas", 200, 470, c("dallas"))
s.raw(f'<div id="l09-tape" class="o0" style="position:absolute;left:1000px;top:150px;width:740px;height:740px;overflow:hidden;box-shadow:0 14px 30px rgba(0,0,0,.25)"><img src="assets/img/vhs0.jpg" style="width:100%;height:100%;object-fit:cover" alt=""></div>',
      js=f"tl.fromTo('#l09-tape', {{ opacity: 1, y: 80, rotation: -3 }}, {{ y: 0, rotation: -1.5, duration: 0.5, ease: 'expo.out' }}, {c('david'):.3f});")
s.text("David Cook opens\na video store", 186, 560, 140, t=c("david"))
s.source("Source: Blockbuster history (AP, via Wikipedia) · Photo: Wikimedia Commons, CC BY-SA 4.0")

s, c = line_scene("Video stores back then")
s.photos([("st1", 0, "50% 60%"), ("st3", c("cook's"))], rate=0.03)
s.raw('<div class="fill" style="background:linear-gradient(0deg,rgba(20,20,20,.85) 0%,rgba(20,20,20,0) 55%)"></div>')
s.kicker("Small · dark · run by movie fans", 192, 600, c("small"), "np")
s.count(186, 650, 300, c("ten|10,000"), 10000, INT, color="np", d=1.3)
s.kicker("tapes on day one: 8,000 VHS + 2,000 Beta", 760, 890, c("tapes"), "np")
s.source("Source: Blockbuster history (via Wikipedia) · Photos: Wikimedia Commons, CC BY 2.0", light=True)

s, c = line_scene("Two years later")
s.kicker("Waste Management founder", 192, 170, c("waste"), "grey")
s.text("Wayne Huizenga", 186, 230, 230, t=c("wayne"))
s.kicker("1987 · Blockbuster stores", 192, 520, c("1987|nineteen"))
s.dots(192, 590, 19, 1, 76, c("stores", off=0.1), d=0.6, shape="sq")
s.text("19", 1700, 520, 200, t=c("stores"), mode="on")

s, c = line_scene("Under Huizenga")
s.kicker("A new store roughly every 24 hours", 192, 140, c("new"))
s.dots(192, 220, 60, 9, 76/2.6, c("new"), d=c("hours") - c("new") + 0.6, shape="sq")
s.text("+1 a day", 1300, 600, 220, color="", t=c("hours"))
s.click(c("new"), "train", 0.3)
s.source("Source: Blockbuster history (via Wikipedia) · grid is illustrative of the pace")

s, c = line_scene("It grew by buying")
s.text("Erol's", 186, 160, 260, t=c("eral's|erol's"))
s.kicker("1990 · 250+ stores", 192, 420, c("250|two"))
s.stamp("Acquired", 980, 200, 170, c("eral's|erol's", off=0.5), rot=-5, ink=True)
s.text("1993: hundreds more", 186, 600, 170, t=c("ninety-three") if any("ninety-three" in w["text"].lower() for w in c.words) else c("added", off=-0.6))
s.kicker("music and video stores", 192, 790, c("music"))
s.stamp("Acquired", 1240, 790, 120, c("music", off=0.3), rot=-4, ink=True)
s.source("Source: Blockbuster history (via Wikipedia)")

s, c = line_scene("In nineteen ninety-four, the media giant")
s.photos([("viacom", 0)], rate=0.012)
sh = s.sheet(96, 560, 1728, 424, c("viacom"), "bottom")
s.in_sheet(sh, "Viacom", 96, 60, 150, t=c("viacom"))
s.in_sheet(sh, "buys", 470, 110, 60, cls="kick", t=c("boug"), mode="on")
s.in_sheet(sh, "Blockbuster", 690, 60, 150, t=c("boug"))
s.in_sheet(sh, "$8.4 billion · 1994", 92, 230, 150, t=c("eight"))
s.click(c("eight"), "pop", 0.3)
s.source("Photo: Viacom HQ, Wikimedia Commons, CC BY 2.0 · Source: Blockbuster history (via Wikipedia)", light=True)

s, c = line_scene("And by two thousand four")
s.kicker("2004 · stores in the US + 25 countries", 192, 120, c("nine"))
s.dots(192, 200, 120, 75, 8.6, c("nine"), d=1.6)
s.text("≈9,000 stores", 186, 860, 120, t=c("stores"))
s.count(1300, 300, 240, c("six"), 6.1, "v => '$' + v.toFixed(1) + 'B'", d=1.2)
s.kicker("revenue, 2004", 1306, 540, c("revenue"))
s.source("Sources: Blockbuster 424B3 prospectus (2004) and 10-K FY2004, SEC")

s, c = line_scene("Friday night in America", "ink", hold=0.6)
s.photos([("st10", 0), ("st11", c("you")), ("st0", c("blockbuster", off=0.1))], rate=0.03)
s.kicker("Friday night", 192, 150, c("friday"), "np")
s.source(CC, light=True)

# =========================== CHAPTER 2 ===========================
chapter("ch2", "The money machine", ["vhs0", "bbcard", "st2", "st3", "vhs1", "st4", "st1", "st9", "st10"])

s, c = line_scene("But inside the business")
for k in range(9):
    s.hrule(192, 300 + k * 70, 1536, c("inside") + k * 0.05, h=3, color="#6B6963")
s.text("The number nobody\nput on the posters", 186, 330, 200, t=c("number"))

s, c = line_scene("Late fees. In two thousand")
s.text("Late fees", 186, 120, 260, t=c("late"), mode="on")
s.click(c("late"), "impact", 0.35)
s.count(186, 400, 230, c("eight"), 800, money("$", " million"), color="red", d=1.4)
s.kicker("in 2000, by Blockbuster's count", 192, 720, c("blockbuster's"))
grid = "".join(f'<div class="l18-c" style="position:absolute;left:{(k%10)*58}px;top:{(k//10)*58}px;width:50px;height:50px;background:#141414"></div>' for k in range(100))
s.raw(f'<div id="l18-g" class="o0" style="position:absolute;left:1240px;top:200px;width:580px;height:580px;transform:scale(.85);transform-origin:0 0">{grid}</div>',
      js=f"on('#l18-g', {c('sixteen', off=-0.3):.3f}); tl.fromTo('#l18-g .l18-c:nth-child(-n+16)', {{ backgroundColor: '#141414' }}, {{ backgroundColor: '#D7261E', duration: 0.001, stagger: 0.04 }}, {c('sixteen'):.3f});")
s.text("16% of revenue", 1240, 740, 100, t=c("percent"))
s.source("Source: Associated Press, via Quartz")

s, c = line_scene("Think about what that means")
coins = "".join(f'<div class="l19-c" style="position:absolute;left:{k*250}px;top:0;width:200px;height:200px;border-radius:50%;background:#141414;opacity:0"></div>' for k in range(6))
s.raw(f'<div style="position:absolute;left:250px;top:340px;width:1500px;height:200px">{coins}</div>',
      js=f"tl.fromTo('#root .l19-c', {{ opacity: 0 }}, {{ opacity: 1, duration: 0.001, stagger: 0.12 }}, {c('one'):.3f}); tl.fromTo('#root .l19-c:last-child', {{ backgroundColor: '#141414' }}, {{ backgroundColor: '#D7261E', duration: 0.001, immediateRender: false }}, {c('six'):.3f});")
for k in range(6): s.click(c("one") + k * 0.12, vol=0.2)
s.text("$1 in every $6", 186, 120, 170, t=c("one"))
s.text("came from customers' mistakes", 186, 640, 140, t=c("mistake", off=-0.5))

s, c = line_scene("Blockbuster's customers hated")
s.photos([("vhs0", 0, "50% 50%")], end=c("reed"), rate=0.03)
bk = s.kicker("“Be kind, rewind”", 192, 150, c("hated"), "np")
s.js.append(f"off('#{bk}', {c('reed'):.3f});")
s.raw('<div id="l20-p" class="o0 fill" style="background:#E9E6DF"><img class="paper" src="assets/paper.jpg" alt=""></div>', js=f"on('#l20-p', {c('reed'):.3f});")
portrait(s, "hast1", "Reed Hastings", "Software engineer · 1997", c("reed"), pos="50% 30%")
s.text("No late fees.\nEver.", 186, 160, 170, color="", t=c("no"))
s.source("Photo: Reed Hastings, Wikimedia Commons, CC BY 2.0")

s, c = line_scene("Netflix had no stores")
s.photos([("nfenv", 0)], rate=0.02, clicks=False)
s.raw('<div class="fill" style="background:rgba(233,230,223,.88)"></div>')
s.text("No stores", 186, 160, 220, t=c("no"))
s.text("DVDs by mail", 186, 400, 220, t=c("mailed"))
s.text("Keep them as long as you want", 186, 640, 150, t=c("kept"))

s, c = line_scene("To Blockbuster, this looked tiny")
s.raw(f'<div id="l22-bb" class="o0" style="position:absolute;left:192px;top:140px;width:800px;height:800px;background:#141414"></div>', js=f"tl.fromTo('#l22-bb', {{ opacity: 1, scale: 0 }}, {{ scale: 1, duration: 0.5, ease: 'expo.out', transformOrigin: '0% 100%' }}, {c('$5|five'):.3f});")
s.text("Blockbuster · $5B", 230, 820, 110, color="np", t=c("$5|five", off=0.4))
s.raw(f'<div id="l22-nf" class="o0" style="position:absolute;left:1180px;top:860px;width:80px;height:80px;background:#141414"></div>', js=f"on('#l22-nf', {c('50|fifty'):.3f});")
s.text("Netflix · $50M", 1300, 850, 110, t=c("50|fifty"))
s.text("100×", 1180, 160, 340, t=c("hundred"))
s.source("Source: Reed Hastings (Marketplace interview, 2020)")

s, c = line_scene("So when Netflix came to Dallas", "ink")
s.photos([("dallas", 0)], rate=0.02, clicks=False)
s.raw('<div class="fill" style="background:rgba(20,20,20,.55)"></div>')
s.text("$50 million?", 186, 240, 300, color="np", t=c("fifty"), mode="on")
s.text("It looked like a joke", 186, 600, 200, color="np", t=c("joke", off=-0.6))

s, c = line_scene("And Blockbuster had a bigger fight")
s.photos([("st8", 0), ("cl3", c("other"))], rate=0.03)
s.raw('<div class="fill" style="background:linear-gradient(0deg,rgba(20,20,20,.8),rgba(20,20,20,0) 60%)"></div>')
s.text("Watching the other video chains", 186, 780, 150, color="np", t=c("watching", 2))
s.source(CC, light=True)

# =========================== CHAPTER 3 ===========================
chapter("ch3", "The counterattack", ["st4", "bbcard", "st6", "st0", "vhs1", "st10", "st5", "st7", "st11"])

s, c = line_scene("Here's the part most people")
s.text("Blockbuster didn't\nstay asleep", 186, 260, 260, t=c("blockbuster"))
s.flash(c("blockbuster", off=-0.05))

s, c = line_scene("The CEO was John Antioco")
portrait(s, "antioco", "John Antioco", "CEO since 1997", 0.15, pos="50% 18%", until=c("august"))
s.raw(f'<div id="l26-cov" class="o0 fill" style="background:#E9E6DF"><img class="paper" src="assets/paper.jpg" alt=""></div>', js=f"on('#l26-cov', {c('august'):.3f});")
s.click(c("august"))
s.kicker("August 2004", 192, 180, c("august"))
s.text("Blockbuster Online", 186, 250, 240, t=c("online"))
s.raw(f'<div id="l26-price" class="o0" style="position:absolute;left:192px;top:560px;border:8px solid #141414;padding:30px 50px 8px"><div class="lg" style="font-size:200px">$19.99<span style="font-size:90px"> / month</span></div></div>', js=f"on('#l26-price', {c('$1999|nineteen'):.3f});")
s.kicker("DVDs by mail · up to 3 at a time", 192, 900, c("$1999|nineteen", off=0.6))
s.source("Source: Blockbuster history (via Wikipedia)")

s, c = line_scene("Then Antioco went after")
s.kicker("January 2005", 192, 200, c("january"))
lf_a, lf_b = s.i("lfa"), s.i("lfb")
s.raw(f'<div id="{lf_a}" class="lg o0" data-layout-allow-overlap style="position:absolute;left:186px;top:290px;font-size:420px;clip-path:inset(0 52% 0 0)">Late fees</div>'
      f'<div id="{lf_b}" class="lg o0" data-layout-allow-overlap style="position:absolute;left:186px;top:290px;font-size:420px;clip-path:inset(0 0 0 48%)">Late fees</div>',
      js=f"on('#{lf_a}', {c('money'):.3f}); on('#{lf_b}', {c('money'):.3f}); tl.fromTo('#{lf_a}', {{ x: 0, rotation: 0 }}, {{ x: -80, y: 60, rotation: -6, duration: 0.5, ease: 'expo.out' }}, {c('killed'):.3f}); tl.fromTo('#{lf_b}', {{ x: 0, rotation: 0 }}, {{ x: 90, y: 30, rotation: 5, duration: 0.5, ease: 'expo.out' }}, {c('killed'):.3f});")
s.click(c("killed"), "impact", 0.4)
s.text("Killed", 186, 800, 160, color="red", t=c("killed", off=0.2), mode="on")

s, c = line_scene("Ending late fees cost")
for k, (lab, word, nth) in enumerate([("End late fees", "$200|two", 1), ("Build online", "$200|two", 2)]):
    t = c(word, nth)
    bid = s.i("bar")
    s.raw(f'<div id="{bid}" class="o0" style="position:absolute;left:{192 + k*780}px;top:300px;width:600px;height:420px;background:#D7261E;transform-origin:50% 100%"></div>', js=f"tl.fromTo('#{bid}', {{ opacity: 1, scaleY: 0 }}, {{ scaleY: 1, duration: 0.45, ease: 'power3.out' }}, {t:.3f});")
    s.text("$200M", 192 + k*780 + 30, 330, 200, color="np", t=t + 0.3, mode="on")
    s.kicker(lab, 192 + k*780, 760, t)
s.source("Source: John Antioco, Harvard Business Review (2011), as summarised by HuffPost")

s, c = line_scene("It wasn't smooth")
s.kicker("The fine print", 192, 150, c("fine"))
s.text("Keep it too long, you bought it", 186, 220, 140, t=c("keep"))
sq = "".join(f'<div class="l29-s" style="position:absolute;left:{(k%10)*96}px;top:{(k//10)*96}px;width:84px;height:84px;background:#C9C5BB"></div>' for k in range(50))
s.raw(f'<div id="l29-g" class="o0" style="position:absolute;left:192px;top:440px;width:960px;height:480px">{sq}</div>',
      js=f"on('#l29-g', {c('more'):.3f}); tl.fromTo('#root .l29-s:nth-child(-n+40)', {{ backgroundColor: '#C9C5BB' }}, {{ backgroundColor: '#141414', duration: 0.001, stagger: 0.025 }}, {c('forty'):.3f});")
s.text("40+ states\nsued", 1240, 440, 140, t=c("sued"))
s.stamp("Settled", 1240, 740, 130, c("settled"), rot=-5, ink=True)
s.source("Source: Associated Press reports, 2005 (via Wikipedia)")

s, c = line_scene("Antioco even went after")
s.kicker("December 2004 · hostile bid", 192, 200, c("december"))
s.text("Hollywood Video", 186, 280, 300, t=c("hollywood"))
s.stamp("Withdrawn", 900, 640, 180, c("walked"), rot=-6, ink=True)
s.source("Source: Blockbuster history (via Wikipedia)")

s, c = line_scene("But in late two thousand six", "ink")
s.photos([("bbcard", 0)], rate=0.03, clicks=False)
s.raw('<div class="fill" style="background:rgba(20,20,20,.6)"></div>')
s.kicker("Late 2006", 192, 300, c("late"), "np")
s.text("Total Access", 186, 380, 360, color="np", t=c("total"), mode="on")
s.click(c("total"), "impact", 0.4)
s.source("Photo: Blockbuster membership card, Wikimedia Commons, public domain", light=True)

s, c = line_scene("Rent online.")
for k, (word, lab) in enumerate([("rent", "Rent online"), ("return", "Return it to any store"), ("walk", "Walk out with a free movie")]):
    s.text(lab, 186, 160 + k * 260, 180, t=c(word))
    s.click(c(word))

s, c = line_scene("Netflix couldn't match that", hold=0.4)
s.raw('<img id="l33-logo" class="o0" src="assets/img/nflogo.png" style="position:absolute;left:192px;top:200px;width:700px" alt="">', js=f"on('#l33-logo', {c('netflix'):.3f});")
s.text("No stores", 186, 600, 300, t=c("no"))
s.strike(176, 720, 1020, c("stores", off=0.2), 24)

s, c = line_scene("By the end of two thousand six")
s.kicker("Total Access customers · end of 2006", 192, 200, c("total"))
s.count(186, 290, 420, c("two"), 2200000, INT, d=1.5)
s.source("Source: Blockbuster results (via Wikipedia)")

s, c = line_scene("Three months earlier")
s.raw(f'''<svg id="l35-ch" class="o0" style="position:absolute;left:192px;top:200px" width="1536" height="640" viewBox="0 0 1536 640">
<line x1="0" y1="600" x2="1536" y2="600" stroke="#6B6963" stroke-width="4"/>
<path id="l35-p" d="M 160 420 L 1280 140" stroke="#141414" stroke-width="16" fill="none" pathLength="100" stroke-dasharray="100 120" stroke-dashoffset="100"/>
<circle id="l35-a" cx="160" cy="420" r="24" fill="#141414"/><circle id="l35-b" cx="1280" cy="140" r="24" fill="#141414" opacity="0"/></svg>''',
      js=f"on('#l35-ch', {c('three'):.3f}); tl.fromTo('#l35-p', {{ strokeDashoffset: 100 }}, {{ strokeDashoffset: 0, duration: 0.9, ease: 'power2.inOut' }}, {c('growing', off=-0.3):.3f}); on('#l35-b', {c('growing', off=0.6):.3f});")
s.text("1.5M", 300, 650, 150, t=c("1.5|one"), mode="on")
s.kicker("Q3 2006", 306, 790, c("1.5|one"))
s.text("2.2M", 1420, 290, 150, t=c("growing", off=0.6), mode="on")
s.kicker("End of 2006", 1426, 430, c("growing", off=0.6))
s.source("Source: Blockbuster results (via Wikipedia)")

s, c = line_scene("For the first time, the giant")
s.text("The giant was\ncatching the startup", 186, 260, 260, t=c("giant"))

# =========================== CHAPTER 4 ===========================
chapter("ch4", "The fight inside", ["icahn", "antioco", "st4", "st9", "bbcard", "st0", "viacom", "st3", "st6"])

s, c = line_scene("But the money had to come")
s.text("The money had to\ncome from somewhere", 186, 200, 200, t=c("money"))
s.raw('<div id="l37-p" class="o0 fill" style="background:#E9E6DF"><img class="paper" src="assets/paper.jpg" alt=""></div>', js=f"on('#l37-p', {c('carl'):.3f});")
portrait(s, "icahn", "Carl Icahn", "Activist investor", c("carl"), pos="50% 25%")
s.source("Photo: Carl Icahn, 1980s, Wikimedia Commons, CC0")

s, c = line_scene("In May two thousand five, Icahn")
s.kicker("May 2005 · proxy fight", 192, 170, c("may"))
s.text("Icahn wins board seats", 186, 240, 200, t=c("won"))
s.kicker("He said Antioco was overpaid. Antioco's pay for 2004:", 192, 560, c("accused"), "grey")
s.count(186, 630, 260, c("$51.6|fifty"), 51.6, "v => '$' + v.toFixed(1) + ' million'", d=1.3)
s.source("Source: Blockbuster history (via Wikipedia)")

s, c = line_scene("Profits were being spent")
rope = s.i("rope")
s.raw(f'<div style="position:absolute;left:192px;top:520px;width:1536px;height:14px;background:#141414" id="{rope}"></div>')
s.text("The future", 186, 300, 200, t=c("future"))
s.text("Cash now", 1290, 300, 200, color="red", t=c("now", off=-0.4))
s.js.append(f"tl.fromTo('#{rope}', {{ x: 0 }}, {{ x: 140, duration: 0.8, ease: 'power2.inOut' }}, {c('board'):.3f});")

s, c = line_scene("In July two thousand seven, after")
portrait(s, "antioco", "John Antioco", "CEO, 1997–2007", 0.05, pos="50% 18%")
s.kicker("A fight over his bonus", 192, 150, c("fight"))
s.stamp("Out · July 2007", 200, 250, 112, c("left"))
s.text("$24.7M severance", 186, 850, 100, t=c("$4.7|twenty"))
s.source("Source: Blockbuster history (via Wikipedia)")

s, c = line_scene("The new CEO, Jim Keyes")
s.photos([("seven", 0), ("st4", c("total"))], rate=0.03)
s.raw('<div class="fill" style="background:linear-gradient(90deg,rgba(20,20,20,.92),rgba(20,20,20,.55) 70%)"></div>')
s.kicker("New CEO, July 2007 · ex-7-Eleven", 192, 200, c("jim"), "np")
s.text("Jim Keyes", 186, 270, 240, color="np", t=c("jim"))
s.text("Total Access prices: up", 186, 560, 150, color="np", t=c("prices"))
s.text("Money back to the stores", 186, 760, 150, color="np", t=c("stores"))
s.kicker("— in Antioco's telling", 192, 920, c("telling"), "np")
s.source("Sources: NBC News (2007); Motley Fool (Dec 2007); J. Antioco, HBR (2011)", light=True)

s, c = line_scene("Meanwhile, in January")
s.kicker("Netflix · January 16, 2007", 192, 180, c("january"))
s.raw(f'<div id="l42-btn" class="o0" style="position:absolute;left:192px;top:300px;border:10px solid #141414;padding:40px 70px 14px"><div class="lg" style="font-size:300px">▶ Watch now</div></div>', js=f"tl.fromTo('#l42-btn', {{ opacity: 1, scale: 0.9 }}, {{ scale: 1, duration: 0.35, ease: 'expo.out' }}, {c('watch'):.3f});")
s.click(c("watch"))
s.text("Instantly, online", 186, 760, 160, t=c("instantly"))
s.source("Source: Netflix press release, Jan 16 2007")

s, c = line_scene("It came free with a subscription")
s.kicker("Watch Now, 2007", 192, 150, c("free"))
s.text("Free with a plan", 186, 220, 170, t=c("free"))
s.text("A few hours a month", 186, 430, 170, t=c("few"))
s.text("Windows PCs only", 186, 640, 170, t=c("windows"))
s.text("Didn't look like much", 1000, 860, 110, color="grey", t=c("didn't"))
s.source("Source: Netflix press release and coverage, Jan 2007")

s, c = line_scene("Blockbuster had caught up")
s.text("DVDs by mail", 186, 200, 200, color="grey", t=c("dvds"))
s.strike(180, 300, 760, c("race"), 16)
s.text("The race moved", 186, 440, 300, t=c("moved"))

s, c = line_scene("Carl Icahn would later")
s.quote(960, 180, 760, 620, "AS REPORTED, 2011", "His worst investment ever", "Carl Icahn on Blockbuster, as reported in coverage of Antioco's 2011 HBR essay", c("worst"), qsize=130)
s.text("Icahn", 186, 300, 300, t=c("carl"))
s.source("Source: VideoNuze summary of HBR exchange (2011)")

s, c = line_scene("Antioco has said he believes")
s.kicker("Antioco's estimate", 192, 170, c("antioko|antioco"), "grey")
s.text("≈10 million", 186, 240, 300, color="grey", t=c("10|ten"))
s.text("subscribers, if online had kept going", 186, 560, 120, color="grey", t=c("subscribers"))
s.source("Source: John Antioco, as summarised by VideoNuze (2011) · an estimate, not a result")

# =========================== CHAPTER 5 ===========================
chapter("ch5", "The fall", ["cl3", "cl0", "cl1", "st9", "cl4", "st7", "dish", "bd0", "st8"])

s, c = line_scene("At the start of twenty ten")
s.kicker("January 2010 · stores", 192, 120, c("start"))
s.dots(192, 190, 130, 50, 11.8, c("6,500|sixty"), d=1.2)
s.text("6,500+", 1450, 880, 120, t=c("6,500|sixty"), mode="on")
s.source("Source: Blockbuster history (via Wikipedia)")

s, c = line_scene("On September twenty-third", "ink")
s.photos([("cl3", 0)], rate=0.02, clicks=False)
s.raw('<div class="fill" style="background:rgba(20,20,20,.5)"></div>')
s.kicker("September 23, 2010", 192, 160, c("september"), "np")
s.stamp("Chapter 11", 520, 340, 260, c("bankruptcy"))
s.text("~$900M in debt", 186, 790, 150, color="np", t=c("$90|$900|nine"))
s.source("Source: Blockbuster history (via Wikipedia) · Photo: Wikimedia Commons, public domain", light=True)

s, c = line_scene("By late October")
s.kicker("Late October 2010 · stores left", 192, 120, c("late"))
s.dots(192, 190, 130, 50, 11.8, 0.0, d=0.01, color="#C9C5BB")
d6 = s.dots(192, 190, 130, 50, 11.8, 0.0, d=0.01, total=6500)
s.dots(192, 190, 130, 50, 11.8, c("three"), d=0.01, total=3425, color="#141414")
s.js.append(f"tl.fromTo('#{d6}', {{ opacity: 1 }}, {{ opacity: 0, duration: 0.6, immediateRender: false }}, {c('three'):.3f});")
s.text("3,425", 1450, 880, 120, t=c("three"), mode="on")

s, c = line_scene("In twenty eleven, the satellite")
s.photos([("dish", 0)], rate=0.02, clicks=False)
sh = s.sheet(96, 560, 1728, 424, c("dish"), "bottom")
s.in_sheet(sh, "Dish buys what's left", 96, 60, 150, t=c("dish"))
s.in_sheet(sh, "≈$320 million · 2011", 92, 230, 150, t=c("three"))
s.source("Photo: Dish HQ, Wikimedia Commons, CC BY-SA 3.0", light=True)

s, c = line_scene("After adjustments")
cash = s.text("≈$228M in cash", 186, 180, 220, t=c("$228|two"))
s.js.append(f"off('#{cash}', {c('icon|icahn', off=-0.2):.3f});")
s.raw('<div id="l52-p" class="o0" style="position:absolute;left:0;top:0;width:1920px;height:1080px"></div>', js=f"on('#l52-p', {c('one'):.3f});")
portrait(s, "icahn", "Carl Icahn", "Another bidder", c("icon|icahn", off=-0.2), pos="50% 25%")
s.stamp("Bidder", 200, 820, 96, c("icon|icahn", off=0.3), rot=-4, ink=True)
s.el("Source: TechCrunch / Fox Business (April 2011)", "left:1150px;bottom:72px", "src np", 0.2)

s, c = line_scene("Seventeen years earlier")
s.raw(f'''<svg id="l53-ch" class="o0" style="position:absolute;left:192px;top:180px" width="1536" height="680" viewBox="0 0 1536 680">
<path id="l53-p" d="M 40 200 L 1180 640" stroke="#D7261E" stroke-width="18" fill="none" pathLength="100" stroke-dasharray="100 120" stroke-dashoffset="100"/></svg>''',
      js=f"on('#l53-ch', {c('seventeen'):.3f}); tl.fromTo('#l53-p', {{ strokeDashoffset: 100 }}, {{ strokeDashoffset: 0, duration: 1.0, ease: 'power2.in' }}, {c('blockbuster', off=-0.4):.3f});")
s.text("$8.4B · 1994", 222, 170, 150, t=c("eight"))
s.text("$320M", 1400, 740, 130, color="red", t=c("blockbuster"))
s.kicker("2011", 1406, 880, c("blockbuster"))

s, c = line_scene("Dish said it would keep")
s.kicker("Stores Dish planned to keep, 2011", 192, 150, c("dish"))
s.dots(192, 230, 50, 10, 30, c("five"), d=0.6)
s.text("≈500", 1450, 600, 200, t=c("five"), mode="on")
s.source("Source: Dish statement, April 2011 (via Wikipedia)")

s, c = line_scene("In November twenty thirteen")
s.photos([("cl0", 0), ("cl1", c("close")), ("cl4", c("company"))], rate=0.03)
s.raw('<div class="fill" style="background:linear-gradient(0deg,rgba(20,20,20,.85),rgba(20,20,20,0) 60%)"></div>')
s.kicker("November 2013", 192, 640, c("november"), "np")
s.text("The last 300 company stores close", 186, 710, 150, color="np", t=c("close"))
s.source(CC, light=True)

s, c = line_scene("And by twenty twenty, one franchise", hold=0.4)
s.photos([("bd0", 0, "50% 50%"), ("bd7", c("last", off=-0.2))], rate=0.02)
s.raw('<div class="fill" style="background:linear-gradient(0deg,rgba(20,20,20,.8),rgba(20,20,20,0) 55%)"></div>')
s.kicker("Bend, Oregon", 192, 700, c("bend"), "np")
s.text("The last Blockbuster on Earth", 186, 770, 160, color="np", t=c("last"))
s.source("Photos: Wikimedia Commons, CC BY-SA 4.0 / CC0", light=True)

s, c = line_scene("That same year")
s.photos([("bd2", 0), ("bd9", c("called"))], rate=0.025)
s.raw('<div class="fill" style="background:rgba(20,20,20,.45)"></div>')
s.kicker("2020 · a documentary", 192, 300, c("documentary"), "np")
s.text("“The Last Blockbuster”", 186, 380, 220, color="np", t=c("last"))
s.source(CC, light=True)

# =========================== ENDING ===========================
s, c = line_scene("Blockbuster is remembered")
s.text("The company that\nlaughed at Netflix", 186, 260, 260, color="grey", t=c("company"))

s, c = line_scene("But the real lesson is harder")
for k, (w, lab, nth) in enumerate([("saw", "Saw it coming", 1), ("killed", "Killed its cash cow", 1), ("built", "Built what Netflix couldn't", 1), ("millions", "Had millions of customers", 1)]):
    s.text(lab, 186, 110 + k * 225, 190, t=c(w, nth))
    s.click(c(w, nth))

s, c = line_scene("What it couldn't survive")
s.text("Its own boardroom", 186, 220, 230, t=c("own"))
s.text("Money back first", 186, 600, 220, color="red", t=c("money"))

s, c = line_scene("Empires rarely fall", hold=1.0)
s.text("Empires rarely fall because\nthey can't see the future", 186, 170, 160, color="grey", t=c("empires"))
s.text("They fall because the future", 186, 530, 160, t=c("they", 2))
s.text("costs money today", 186, 700, 240, color="red", t=c("costs"))

s, c = line_scene("This is Paper Empire", "ink", hold=2.6)
s.raw(f'<div id="l61-crown" style="position:absolute;left:810px;top:150px">{CROWN_SVG.format(s=300)}</div>',
      js="tl.fromTo('#l61-crown .cf', { y: 80, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: 'expo.out', stagger: 0.08 }, 0.2); tl.fromTo('#l61-crown .cb', { scaleX: 0 }, { scaleX: 1, transformOrigin: '50% 50%', duration: 0.4, ease: 'power2.inOut' }, 0.5); tl.fromTo('#l61-crown .cr', { opacity: 0 }, { opacity: 1, duration: 0.001 }, 1.0);")
s.click(1.0, "impact", 0.35)
s.text("Paper Empire", 0, 500, 200, color="np", t=0.6, extra="width:1920px;text-align:center")
s.el("Next: Kodak", "left:0;top:720px;width:1920px;text-align:center", "kick np", c("next"))
s.raw(f'<div id="l61-k" class="o0" style="position:absolute;left:0;top:780px;width:1920px;text-align:center;font:400 40px Inter;color:#E9E6DF">How a camera company invented the digital camera, then let it destroy them</div>', js=f"on('#l61-k', {c('camera'):.3f});")

# =========================== WRITE ===========================
for sc, _ in timeline:
    sc.write("compositions")
t = 0.0; hosts, vos, cues = [], [], []
for sc, lid in timeline:
    hosts.append(f'      <div id="{sc.sid}" data-composition-id="{sc.sid}" data-composition-src="compositions/{sc.sid}.html" data-start="{t:.3f}" data-duration="{sc.dur}" data-track-index="1" data-track-kind="graphics" data-width="1920" data-height="1080"></div>')
    if lid:
        vos.append(f'      <audio id="vo-{lid}" class="clip" src="assets/vo/{lid}.wav" data-start="{t + LEAD:.3f}" data-duration="{dur(f"assets/vo/{lid}.wav") - 0.01:.3f}" data-track-index="2" data-volume="1"></audio>')
    for kind, st, vol in sc.sfx:
        cues.append((kind, round(t + st, 3), vol))
    t += sc.dur
TOTAL = round(t, 3)
json.dump({"total": TOTAL, "cues": cues, "scenes": [(sc.sid, lid) for sc, lid in timeline]}, open("timeline.json", "w"), indent=1)
open("index.html", "w").write(f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>* {{ margin: 0; padding: 0; box-sizing: border-box; }} html, body {{ margin: 0; width: 1920px; height: 1080px; overflow: hidden; background: #141414; }}</style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1920" data-height="1080">
{chr(10).join(hosts)}
{chr(10).join(vos)}
      <audio id="mix-fx" class="clip" src="assets/audio/bed_fx.wav" data-start="0" data-duration="{TOTAL}" data-track-index="3" data-volume="1"></audio>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
''')
print("scenes", len(timeline), "total", TOTAL, "s =", round(TOTAL / 60, 2), "min; sfx cues", len(cues))
