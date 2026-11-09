# BlackBerry: "The keyboard was the trap" (Paper Empire). One block per voice line. Run: python3 build.py
import sys, os; sys.path.insert(0, os.path.abspath("../../kit"))
from build_lib import *
import build_lib; build_lib.GAP = 0.9

PH = "Photo: Wikimedia Commons (credits in description)"
S2  = "Source: RIM corporate history; Reuters timeline"
S3  = "Source: RIM Q4 & fiscal 2011 results, filed with the SEC (22 Mar 2011)"
S4  = "Source: comScore via TechCrunch (Jan 2022); NPD via PocketGamer (May 2009)"
S5  = "Source: RIM Q3 fiscal 2013 filing (Dec 2012); The Verge interview (Jul 2012)"
S6  = "Source: RIM Q3 fiscal 2013 filing; press reviews of the Storm (2008)"
S7  = "Source: RIM Q3 fiscal 2012 filing: $485M pre-tax PlayBook inventory provision"
S8  = "Source: NYT (13 Oct 2011); RIM Q3 fiscal 2012 filing"
S9  = "Source: Reuters / Globe and Mail (Jan 2012)"
S10 = "Source: press coverage of the BlackBerry 10 launch (30 Jan 2013)"
S11 = "Source: BlackBerry Q2 fiscal 2014 release, 6-K filed 20 Sep 2013"
S12 = "Source: CBC, Reuters (4 Nov 2013); BlackBerry 6-K (Sep-Nov 2013)"
S13 = "Source: BlackBerry 6-K (4 Nov 2013)"
S14 = "Source: BlackBerry release (28 Sep 2016); TCL deal (15 Dec 2016); TechCrunch"
S16 = "Source: BlackBerry 10-K fiscal 2026 (audited)"
S18 = "Source: RIM Q3 fiscal 2013 6-K, MD&A"
S19 = "Source: QNX share purchase agreement, EX-10.1 filed by Harman (Apr 2010)"
S20 = "Source: The Globe and Mail investigation (27 Sep 2013); McNish and Silcoff, Losing the Signal"
S21 = "Source: The Globe and Mail investigation (27 Sep 2013)"
DIM = '<div class="fill" style="background:rgba(20,20,20,.55)"></div>'
FADE = '<div class="fill" style="background:linear-gradient(0deg,rgba(20,20,20,.92),rgba(20,20,20,0) 62%)"></div>'

# =========================== COLD OPEN ===========================
s, c = line_scene("In twenty eleven, Research", "ink")
s.photos([("bold9900", 0), ("phones_row", c("history", off=-0.2)), ("hq", c("revenue", off=-0.3))], rate=0.035)
s.raw(FADE)
s.kicker("Fiscal 2011", 192, 200, c("2011|twenty"), "np")
s.count(186, 270, 330, c("revenue|nineteen|20"), 19.9, "v => '$' + v.toFixed(1) + ' billion'", color="np", d=1.4)
s.kicker("Revenue, a company record", 192, 660, c("revenue"), "np")
s.source(S3, light=True)

s, c = line_scene("Profit: three point four")
s.kicker("Fiscal 2011 · net income", 192, 200, c("profit"))
s.count(186, 270, 360, c("$3|profit"), 3.4, "v => '$' + v.toFixed(1) + ' billion'", d=1.4)
s.text("One of the most profitable\ntech companies on earth", 186, 700, 110, color="grey", t=c("profitable"))
s.source(S3)

s, c = line_scene("Four years after the iPhone")
photo_card(s, "iphone", 1210, 130, 560, 420, c("iphone"), rot=1.4)
s.kicker("Fiscal 2011", 192, 200, c("four"))
s.text("52.3 million\ndevices", 186, 260, 200, t=c("blackberry"))
s.text("up 43% in one year", 186, 640, 130, color="grey", t=c("forty|43"))
s.source(S3)

s, c = line_scene("The company everyone says")
s.text("KILLED?", 186, 300, 300, t=c("killed"), mode="on")
s.strike(176, 340, 700, c("killed", off=0.55), 26)
s.kicker("at its peak", 192, 700, c("peak"), "grey")
s.source(S3)

s, c = line_scene("Then, in two years", "ink", punch=True)
s.photos([("bold9900_side", 0)], rate=0.02)
s.raw(DIM)
s.text("LOST\nALMOST\nALL OF IT", 186, 160, 200, color="np", t=c("lost"))
s.source(S3 + "; BlackBerry 6-K (Sep 2013)", light=True)

s, c = line_scene("This is how the keyboard", "ink", hold=0.6)
s.raw(f'<div id="g05-crown" class="o0" style="position:absolute;left:192px;top:300px">{CROWN_SVG.format(s=180)}</div>', js="on('#g05-crown', 0.25);")
s.kicker("Paper Empire", 410, 360, 0.3, "np")
s.text("BlackBerry", 186, 500, 320, color="np", t=c("blackberry|keyboard"))
s.kicker("Built by a keyboard. Trapped by it.", 192, 860, c("trapped"), "np")
s.click(c("blackberry|keyboard"), "impact", 0.4)

# =========================== CHAPTER 1 ===========================
chapter("ch1", "A keyboard you could type on",
        ["hq", "p_lazaridis", "p_balsillie", "curve", "bold9900", "crackberry", "phones_row", "storm", "iphone"], d=3.0)

s, c = line_scene("Research In Motion started")
s.photos([("hq", 0)], rate=0.02)
s.raw(FADE)
s.kicker("1984 · Waterloo, Ontario", 192, 620, c("1984|nineteen"), "np")
s.text("Research In Motion", 186, 690, 150, color="np", t=c("research"))
s.source(S3, light=True)

s, c = line_scene("Mike Lazaridis and Douglas")
photo_card(s, "p_lazaridis", 1210, 120, 380, 500, c("lazaridis|Mike"), rot=1.2, fit="cover")
photo_card(s, "p_balsillie", 1420, 520, 300, 400, c("balsillie|Jim"), rot=-1.4, fit="cover")
s.text("Mike Lazaridis", 186, 220, 150, t=c("lazaridis|Mike"))
s.text("Douglas Fregin", 186, 430, 150, color="grey", t=c("fregin|Douglas"))
s.text("Jim Balsillie\njoined in 1992", 186, 660, 130, t=c("balsillie|Jim"))
s.source(S20)

s, c = line_scene("In nineteen ninety-nine")
photo_card(s, "curve", 1100, 150, 640, 520, c("1999|nineteen"), rot=-1.4)
s.kicker("1999", 192, 220, c("1999|nineteen"))
s.text("A two-way\npager", 186, 280, 210, t=c("pager"))
s.text("with a keyboard", 186, 640, 130, color="grey", t=c("keyboard"))
s.source(S2)

s, c = line_scene("The pitch was simple")
photo_card(s, "bold9900", 1180, 130, 560, 700, 0.15, rot=1.2)
s.text("PUSH\nEMAIL", 186, 260, 260, t=c("email"))
s.text("It arrives by itself.", 186, 780, 120, color="grey", t=c("arrives"))
s.source(S2)

s, c = line_scene("They called it push email")
s.stamp("PUSH EMAIL", 186, 260, 250, c("push"), rot=-4, ink=True)
s.text("The first notification", 186, 620, 130, t=c("notification"))
s.source(S2)

s, c = line_scene("You could answer on a real keyboard")
s.photos([("bold9900_side", 0)], rate=0.03)
s.raw(FADE)
s.text("Thumbs.", 186, 260, 300, color="np", t=c("thumbs"), mode="on")
s.kicker("A keyboard you could actually use", 192, 700, c("real"), "np")
s.source(PH, light=True)

s, c = line_scene("That one advantage walked")
s.photos([("phones_row", 0)], rate=0.02)
s.raw(DIM)
s.text("The company\nphone", 186, 240, 200, color="np", t=c("office"))
s.source(PH, light=True)

s, c = line_scene("By the late two thousands")
s.tiles(["bold9900", "curve", "curve2010", "storm", "storm2", "q5", "phones_row", "crackberry", "smartphones_mix"], 0.05)
s.raw('<div style="position:absolute;left:0;top:0;width:1536px;height:1080px;background:linear-gradient(90deg,rgba(20,20,20,.82),rgba(20,20,20,0) 55%)"></div>')
s.text("The default\nphone of\nbusiness", 186, 330, 150, color="np", t=c("default"))
s.source(PH, light=True)

s, c = line_scene("It was secure enough")
s.photos([("hq", 0)], rate=0.02)
s.raw(DIM)
s.text("Governments\nrelied on it", 186, 240, 190, color="np", t=c("governments"))
s.kicker("The U.S. Department of Defense", 192, 800, c("united"), "np")
s.source(S18, light=True)

s, c = line_scene("People had a name")
s.text("CrackBerry", 186, 260, 300, t=c("crackberry"), mode="on")
s.kicker("What people called it", 192, 680, c("called"))
s.source("Source: contemporary press coverage of BlackBerry use")

s, c = line_scene("That is not a company", "ink", punch=True)
s.text("A licence\nto print\nmoney.", 186, 140, 210, color="np", t=c("licence|license"))
s.source(S3, light=True)

# =========================== CHAPTER 2 ===========================
chapter("ch2", "The screen stays small",
        ["iphone", "bold9900", "iphone_3g", "storm", "playbook", "q5", "curve", "smartphones_mix", "bold9900_side"], d=3.0)

s, c = line_scene("Then in two thousand seven")
photo_card(s, "iphone", 1100, 120, 700, 520, c("iphone"), rot=1.2)
s.kicker("2007", 192, 220, c("2007|seven"))
s.text("One sheet\nof glass", 186, 280, 220, t=c("glass"))
s.text("No keyboard", 186, 660, 140, color="grey", t=c("keyboard"))
s.source(S6)

s, c = line_scene("The obvious assumption")
s.text("iPHONE 2007", 186, 240, 150, color="grey", t=c("obvious|iphone"))
s.hrule(192, 410, 700, c("obvious", off=0.4))
s.text("BLACKBERRY\nKEPT GROWING", 186, 460, 190, t=c("otherwise"), mode="on")
s.source(S3)

s, c = line_scene("For years BlackBerry outsold")
s.text("52.3M", 186, 240, 260, t=c("outsold|years"))
s.kicker("BlackBerry devices sold · fiscal 2011", 192, 560, c("blackberry"))
s.text("More than Apple shipped\nin the same year", 186, 640, 120, color="grey", t=c("apple"))
s.source(S3)

s, c = line_scene("And RIM saw it coming")
portrait(s, "p_lazaridis", "Mike Lazaridis", "Co-founder, RIM", c("lazaridis|Mike"))
s.text("He opened one.", 186, 200, 170, t=c("opened"))
s.source(S20)

s, c = line_scene("According to the Globe")
s.quote(192, 170, 1536, 600, "ACCORDING TO THE GLOBE AND MAIL'S INVESTIGATION",
        "They've put a Mac in this thing.", "Mike Lazaridis, on opening an iPhone", c("mac|Mac"), qsize=120)
s.source(S20)

s, c = line_scene("He understood it was a computer")
s.text("A COMPUTER", 186, 260, 170, t=c("computer"))
s.text("without\na keyboard", 186, 470, 150, color="grey", t=c("type|keyboard"))
s.hrule(192, 800, 900, c("judged"))
s.kicker("He judged business would not want it", 192, 860, c("business"), "grey")
s.source(S20)

s, c = line_scene("The whole BlackBerry ran")
s.kicker("Memory, side by side", 192, 200, c("whole"))
s.text("32 MB", 186, 270, 240, t=c("thirty|32"))
s.text("700 MB", 186, 560, 240, color="grey", t=c("seven|700"))
s.kicker("the whole BlackBerry / the iPhone OS alone", 192, 840, c("operating"), "grey")
s.source(S21)

s, c = line_scene("A computer needs the whole front")
s.raw('<svg style="position:absolute;left:186px;top:240px" width="1540" height="620" viewBox="0 0 1540 620">'
      '<rect x="0" y="0" width="600" height="620" fill="#E9E6DF" stroke="#141414" stroke-width="8"/>'
      '<rect id="g24-scr" x="0" y="0" width="600" height="370" fill="#141414"/>'
      '<rect x="0" y="370" width="600" height="250" fill="#E9E6DF" stroke="#141414" stroke-width="8"/>'
      '<text x="300" y="500" font-family="Inter" font-size="34" fill="#141414" text-anchor="middle">KEYBOARD</text>'
      '<rect x="760" y="0" width="600" height="620" fill="#E9E6DF" stroke="#141414" stroke-width="8"/>'
      '<rect id="g24-full" x="760" y="0" width="600" height="620" fill="#141414"/>'
      '</svg>',
      js=f"tl.fromTo('#g24-scr', {{ scaleY: 0, transformOrigin: '50% 100%' }}, {{ scaleY: 1, duration: 0.5, ease: 'power2.inOut' }}, {c('computer', off=-0.2):.3f}); "
         f"tl.fromTo('#g24-full', {{ scaleY: 0, transformOrigin: '50% 100%' }}, {{ scaleY: 1, duration: 0.5, ease: 'power2.inOut' }}, {c('keyboard'):.3f});")
s.kicker("SCREEN AREA", 192, 150, c("screen"))
s.source(S6)

s, c = line_scene("RIM could not have both")
s.kicker("THE TRADE", 192, 200, c("both"))
s.text("KEYBOARD", 186, 280, 170, t=c("keyboard"))
s.hrule(192, 470, 700, c("keyboard", off=0.3))
s.text("SCREEN", 186, 520, 170, color="grey", t=c("screen"))
s.text("one or the other", 186, 800, 120, t=c("both"))
s.source(S6)

s, c = line_scene("Web pages, maps, video")
s.photos([("smartphones_mix", 0)], rate=0.02)
s.raw(DIM)
x = 192
for w, lab in [("web", "Web"), ("maps", "Maps"), ("video", "Video"), ("photographs", "Photos")]:
    s.el(lab, f"left:{x}px;top:200px;background:#141414;padding:14px 22px", "kick np", c(w)); x += len(lab) * 34 + 90
s.text("A worse place\nto look at anything", 186, 640, 170, color="np", t=c("worse"))
s.source(PH, light=True)

s, c = line_scene("That mattered more every year")
s.kicker("What people wanted next", 192, 220, c("software"))
s.text("APPS", 186, 290, 380, t=c("app"), mode="on")
s.text("They lived in the app store", 186, 720, 110, color="grey", t=c("store"))
s.source(S6)

s, c = line_scene("Developers build for the biggest")
s.kicker("SCREEN", 192, 200, c("biggest"))
s.text("\u2192 APPS", 186, 270, 190, t=c("audience"))
s.kicker("AUDIENCE", 192, 560, c("audience"))
s.text("\u2192 DEVELOPERS", 186, 630, 190, color="grey", t=c("build|developers"))
s.stamp("NEITHER", 186, 800, 130, c("neither"))
s.source(S6)

s, c = line_scene("RIM tried. In two thousand eight")
photo_card(s, "storm", 1120, 140, 620, 520, c("storm"), rot=-1.4)
s.kicker("2008", 192, 220, c("2008|eight"))
s.text("The Storm", 186, 280, 200, t=c("storm"))
s.text("sold, and was hated", 186, 600, 120, color="grey", t=c("hated"))
s.source(S6)

s, c = line_scene("In twenty ten it announced a tablet")
photo_card(s, "playbook", 1150, 150, 600, 440, c("tablet"), rot=1.2)
s.kicker("2010 to 2011 · the PlayBook", 192, 220, c("2010|ten"))
s.text("Late.\nHalf finished.\nFlopped.", 186, 280, 150, t=c("flopped"))
s.source(S7)

s, c = line_scene("RIM took a provision")
s.kicker("PLAYBOOK", 192, 200, c("playbook"))
s.count(186, 260, 360, c("provision|485"), 485, "v => '$' + Math.round(v) + ' million'", color="red", d=1.4)
s.kicker("UNSOLD STOCK, WRITTEN OFF", 192, 700, c("stock"))
s.source(S7)

s, c = line_scene("To build the PlayBook")
photo_card(s, "playbook2", 1160, 180, 580, 420, c("qnx|QNX"), rot=-1.2)
s.kicker("QNX · BOUGHT IN 2010", 192, 220, c("qnx|QNX"))
s.text("An operating\nsystem RIM\nrented, then owned.", 186, 300, 150, t=c("company|bought"))
s.text("bought, not built", 186, 740, 130, color="grey", t=c("built"))
s.source(S19)

# =========================== CHAPTER 3 ===========================
chapter("ch3", "The trap closes",
        ["curve", "curve2010", "bold9900", "q5", "storm", "iphone_3g", "phones_row", "hq", "smartphones_mix"], d=3.0)

s, c = line_scene("The rest of the world")
s.kicker("January 2010 · comScore", 192, 200, c("january|January"))
s.count(186, 270, 380, c("43|forty"), 43, "v => Math.round(v) + '%'", d=1.4)
s.kicker("SHARE OF U.S. SMARTPHONES", 192, 700, c("america"))
s.source(S4)

s, c = line_scene("Almost twenty-two million people")
s.dots(186, 240, 44, 22, 15, c("million"), d=1.0, total=968)
s.text("22 million U.S. users", 186, 700, 150, t=c("22|twenty"))
s.source(S4)

s, c = line_scene("Two years later that had collapsed")
s.count(186, 240, 340, c("9|nine"), 9, "v => Math.round(v) + ' million'", color="red", d=1.2)
s.kicker("U.S. users, two years after the peak", 192, 640, c("collapsed"))
s.source(S4)

s, c = line_scene("Even so, the company was still growing")
s.count(186, 240, 380, c("eighty|80"), 80, "v => Math.round(v) + ' million'", d=1.4)
s.kicker("users worldwide · 2012", 192, 700, c("2012|worldwide"))
s.source(S5)

s, c = line_scene("Its own chief executive")
s.quote(192, 170, 1536, 620, "THORSTEN HEINS, CEO · JULY 2012",
        "We have roughly eighty million users today, and Nokia doesn't have that.",
        "Interview with The Verge", c("roughly"), qsize=100)
s.source(S5)

s, c = line_scene("But being big is not the same")
s.text("Bigger", 186, 240, 220, t=c("big"))
s.text("and being left", 186, 540, 220, color="grey", t=c("leaving"))
s.hrule(192, 800, 900, c("leaving"))
s.source("Source: comScore via TechCrunch (Jan 2022)")

s, c = line_scene("In October twenty eleven")
s.photos([("q5", 0), ("bold9900_side", c("failed"))], rate=0.03)
s.raw(FADE)
s.kicker("October 2011", 192, 200, c("october|October"), "np")
s.text("The network\nwent down", 186, 270, 190, color="np", t=c("failed"))
s.kicker("email and messages, five continents", 192, 800, c("five"), "np")
s.source(S8, light=True)

s, c = line_scene("In early twenty twelve")
portrait(s, "p_balsillie", "Jim Balsillie", "co-CEO, resigned 2012", c("balsillie|two|ran"))
s.text("Out in\none afternoon", 186, 200, 170, t=c("afternoon"))
s.kicker("Thorsten Heins took over", 192, 800, c("heins|Heins|Thorsten"))
s.source(S9)

s, c = line_scene("Heins put everything on one bet")
photo_card(s, "q5", 1150, 170, 600, 520, c("operating"), rot=1.2)
s.kicker("BlackBerry 10", 192, 220, c("blackberry|BlackBerry"))
s.text("Everything\non one\nsystem", 186, 280, 170, t=c("bet"))
s.source(S10)

s, c = line_scene("By then the judgement")
s.kicker("According to the Globe and Mail's investigation", 192, 220, c("written"))
s.text("Two years\ntoo late.", 186, 290, 250, t=c("late"), mode="on")
s.source(S20)

s, c = line_scene("In September twenty thirteen", "ink")
s.count(186, 240, 360, c("billion"), 1.0, "v => '$' + v.toFixed(1) + ' billion'", color="red", d=1.4)
s.kicker("operating loss, September 2013", 192, 660, c("loss"), "np")
s.source(S11, light=True)

s, c = line_scene("It cut four thousand five hundred")
s.count(186, 240, 340, c("500|4500|thousand"), 4500, INT, color="red", d=1.4)
s.kicker("jobs cut", 192, 640, c("jobs"))
s.text("About 40% of everyone who worked there", 186, 740, 120, color="grey", t=c("forty|40"))
s.source(S11)

s, c = line_scene("Then came a rescue")
sh = s.sheet(880, 180, 840, 460, c("fairfax|Fairfax"), "right")
s.in_sheet(sh, "OFFER TO BUY", 60, 60, 40, cls="kick", t=c("fairfax|Fairfax"))
s.in_sheet(sh, "$9.00", 60, 130, 130, t=c("$9|offered", off=0.15))
s.in_sheet(sh, "per share", 60, 270, 60, cls="", t=c("share"))
s.in_sheet(sh, "about $4.7 billion", 60, 350, 60, cls="", t=c("$4|4"))
s.kicker("THE OFFER", 192, 220, c("rescue"))
s.text("$9 a share", 186, 290, 190, t=c("$9|offered"))
s.text("$4.7 billion", 186, 530, 190, t=c("$4|4"))
s.text("Fairfax, to take it private", 186, 780, 120, color="grey", t=c("fairfax|Fairfax"))
s.source(S12)

s, c = line_scene("Six weeks later the deal")
s.kicker("Six weeks later", 192, 200, c("weeks"))
s.text("$1 billion\ninstead", 186, 270, 220, t=c("billion"))
s.text("a cash injection, and still independent", 186, 700, 120, color="grey", t=c("independent"))
s.source(S12)

s, c = line_scene("And the man behind Fairfax")
s.kicker("THE BUYER'S OWN TIMELINE", 192, 220, c("August|august"))
s.text("AUG 2013  quits the board", 186, 300, 120, t=c("quit|board"))
s.text("SEP 2013  makes the offer", 186, 460, 120, t=c("offer|made"))
s.text("NOV 2013  walks away", 186, 620, 120, color="grey", t=c("room|away"))
s.source(S12)

s, c = line_scene("In November twenty thirteen")
s.kicker("November 2013", 192, 220, c("november|November"))
s.text("John Chen", 186, 290, 280, t=c("chen|Chen"))
s.text("Not to win. To keep it alive.", 186, 680, 130, color="grey", t=c("alive"))
s.source(S13)

# =========================== CHAPTER 4 ===========================
chapter("ch4", "The keyboard goes out the door",
        ["bold9900", "curve", "q5", "playbook", "phones_row", "hq", "crackberry", "storm2", "bold9900_side"], d=3.0)

s, c = line_scene("Chen did the thing")
s.photos([("bold9900", 0)], rate=0.02)
s.raw(DIM)
s.text("He stopped\ndefending\nthe phone.", 186, 200, 190, color="np", t=c("stopped"))
s.source(S13, light=True)

s, c = line_scene("The company would keep")
s.photos([("hq", 0)], rate=0.02)
s.raw(FADE)
x = 192
for w, lab in [("security", "Security"), ("software", "Software"), ("cars", "Systems in cars")]:
    s.el(lab, f"left:{x}px;top:240px;background:#141414;padding:14px 22px", "kick np", c(w)); x += len(lab) * 34 + 90
s.text("What it kept", 186, 700, 180, color="np", t=c("keep"))
s.source(S14 + "; " + S19, light=True)

s, c = line_scene("The phones were handed")
s.text("TCL", 186, 240, 300, t=c("tcl|TCL"))
s.text("Then OnwardMobility", 186, 600, 170, color="grey", t=c("onward|Onward"))
s.kicker("The name, licensed out", 192, 800, c("handed"))
s.source(S14)

s, c = line_scene("OnwardMobility never shipped")
s.text("Zero phones.", 186, 260, 280, t=c("never"), mode="on")
s.kicker("The startup shut down in 2022", 192, 700, c("shut"))
s.source(S14)

s, c = line_scene("The last hardware was made")
s.kicker("LAST HARDWARE", 192, 220, c("hardware"))
s.text("August 2020", 186, 290, 200, t=c("2020|august"))
s.kicker("LAST SERVICE", 192, 600, c("service"))
s.text("January 2022", 186, 670, 200, t=c("2022|january"))
s.source(S14)

s, c = line_scene("BlackBerry is still a company")
s.kicker("BlackBerry today", 192, 220, c("still"))
s.text("Software", 186, 290, 200, t=c("software"))
s.text("about 3,000 people", 186, 540, 150, color="grey", t=c("3,000|3|three"))
s.text("No devices segment.", 186, 740, 130, t=c("phone"))
s.source(S16)

s, c = line_scene("The phone that every business leader")
s.photos([("crackberry", 0)], rate=0.02)
s.raw(DIM)
s.text("Eleven letters on a phone\nnobody makes.", 186, 280, 140, color="np", t=c("logo"))
s.source(S14, light=True)

# =========================== ENDING ===========================
s, c = line_scene("So here is the real reason")
s.text("MISSED IT?", 186, 260, 240, color="grey", t=c("missed"))
s.strike(176, 320, 780, c("missed", off=0.5), 18)
s.text("It saw the iPhone\nin 2007.", 186, 470, 190, t=c("saw"))
s.source(S20)

s, c = line_scene("It is that the shift")
s.text("The shift was\nagainst its\nbest product.", 186, 180, 170, t=c("shift"))
s.text("The keyboard was the whole company.", 186, 780, 120, color="grey", t=c("keyboard"))
s.source(S20)

s, c = line_scene("And a company will defend", punch=True)
s.text("THE KEYBOARD", 186, 300, 190, t=c("defend"))
s.strike(176, 500, 1100, c("reason", off=0.2), 20)
s.kicker("defended right up until it could not move", 192, 700, c("move"), "grey")
s.source(S20)

s, c = line_scene("The keyboard was not a mistake", hold=0.5)
s.text("A decision\nso good,\nit was forgotten\nto be a decision.", 186, 170, 150, t=c("decision"))
s.source(S20)

s, c = line_scene("Every company has one of those", hold=1.0)
s.kicker("EVERY COMPANY HAS ONE", 192, 240, c("every|company"))
s.text("Ask what it costs.", 186, 330, 220, t=c("cost"))
s.hrule(192, 700, 760, c("cost", off=0.3))
s.source(S20)

end_card("This is Paper Empire", "Sears", "It was the Amazon of 1900, and it lost to the idea it invented")

finish()
