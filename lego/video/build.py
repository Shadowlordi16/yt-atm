# Lego: "Saved by Doing Less" (Paper Empire). One block per voice line. Run: python3 build.py
import sys, os; sys.path.insert(0, os.path.abspath("../../kit"))
from build_lib import *
import build_lib; build_lib.GAP = 1.0

PH = "Photo: Wikimedia Commons (credits in description)"
S1 = "Source: History of Lego (Hansen 1982; Wiencek 1987) via Wikipedia"
S2 = "Source: David Robertson, Brick by Brick · Knowledge at Wharton"
S3 = "Source: LEGO Annual Report 2003"
S4 = "Source: AP via NBC News (February 2006)"
S9 = "Source: The Economist, “Unpacking Lego” (2014)"
DIM = '<div class="fill" style="background:rgba(20,20,20,.5)"></div>'
FADE = '<div class="fill" style="background:linear-gradient(0deg,rgba(20,20,20,.9),rgba(20,20,20,0) 62%)"></div>'

# =========================== COLD OPEN ===========================
s, c = line_scene("In two thousand four, the company", "ink")
s.photos([("pile_grey", 0), ("pile2", c("famous", off=-0.2)), ("pile_color", c("running", off=-0.2))], rate=0.03)
s.raw(DIM)
s.kicker("2004", 192, 640, c("2004|two"), "np")
s.text("Running out of money", 186, 700, 190, color="np", t=c("running"))
s.source(S4 + "; The Telegraph (2009)", light=True)

s, c = line_scene("That year alone, Lego lost")
s.kicker("2004 · Lego's loss", 192, 200, c("lego"))
s.count(186, 270, 380, c("lost"), 1.93, "v => 'DKK ' + v.toFixed(2) + 'B'", color="red", d=1.4)
s.text("≈ $300 million", 186, 720, 170, color="grey", t=c("300|three"))
s.source(S4 + "; The Irish Times")


s, c = line_scene("It was the biggest loss")
s.kicker("2004", 192, 260, c("biggest", off=-0.3))
s.text("The biggest loss\nin its history", 186, 320, 240, t=c("biggest"))
s.hrule(192, 860, 900, c("history"))
s.source("Source: The Irish Times")

s, c = line_scene("One of its own executives")
s.quote(192, 170, 1536, 620, "A LEGO EXECUTIVE, LOOKING BACK", "“Almost bankrupt”", "Mads Nipper, to The Telegraph (2009)", c("almost"), qsize=200)
s.source("Source: The Telegraph (2009)")

s, c = line_scene("It had theme parks, video games")
s.photos([("ll_temple", 0), ("sw_deathstar", c("video", off=-0.1)), ("bionicle", c("action", off=-0.1)), ("brick_black", c("brick", off=-0.15))], rate=0.03)
s.raw(FADE)
x = 192
for w, lab in [("theme", "Theme parks"), ("video", "Video games"), ("tv", "TV"), ("action", "Action figures")]:
    s.el(lab, f"left:{x}px;top:150px;background:#141414;padding:14px 22px", "kick np", c(w)); x += len(lab) * 33 + 90
s.text("It forgot the brick", 186, 760, 170, color="np", t=c("forgotten"))
s.source(PH, light=True)

s, c = line_scene("Ten years later, Lego was")
s.kicker("2014", 192, 240, c("ten|10"))
s.text("No. 1", 186, 300, 420, t=c("biggest"), mode="on")
s.kicker("The biggest toy company in the world", 192, 760, c("toy"))
s.source("Source: RTÉ (September 2014)")

s, c = line_scene("This is the story of how Lego", "ink", hold=0.6)
s.raw(f'<div id="g05-crown" class="o0" style="position:absolute;left:192px;top:300px">{CROWN_SVG.format(s=180)}</div>', js="on('#g05-crown', 0.25);")
s.kicker("Paper Empire", 410, 360, 0.3, "np")
s.text("Lego", 186, 500, 340, color="np", t=c("lego"))
s.kicker("Nearly lost everything. Saved by doing less.", 192, 860, c("saved"), "np")
s.click(c("lego"), "impact", 0.4)

# =========================== CHAPTER 1 ===========================
chapter("ch1", "Play well", ["ole_desk", "workshop", "family", "ole_house", "patent2", "pile_color", "p_godt", "brick_black", "house"], d=3.2)

s, c = line_scene("The story starts in nineteen")
s.photos([("ole_house", 0)], rate=0.02)
s.raw(FADE)
s.kicker("1932 · Billund, Denmark", 192, 620, c("1932|nineteen"), "np")
s.text("Ole Kirk Christiansen", 186, 690, 170, color="np", t=c("carpenter", off=0.3))
s.kicker("a carpenter", 192, 880, c("carpenter"), "np")
s.source("Photo: Ole Kirk's House, Billund · Wikimedia Commons, CC BY-SA 4.0 · " + S1[8:], light=True)

s, c = line_scene("He made furniture")
photo_card(s, "workshop", 1120, 110, 600, 380, c("furniture"), rot=-1.2)
s.text("Furniture", 186, 200, 220, color="grey", t=c("furniture"))
s.kicker("The Great Depression", 192, 470, c("depression"))
s.text("Wooden toys", 186, 540, 260, t=c("wooden"))
s.source(S1)

s, c = line_scene("In nineteen thirty-four, he gave")
s.kicker("1934", 192, 180, c("1934|nineteen"))
s.text("Leg godt", 186, 250, 260, t=c("danish"))
s.text("\u2192 Lego", 940, 250, 260, t=c("play", off=-0.3), mode="on")
s.hrule(192, 600, 1536, c("play", off=-0.3))
s.text("“Play well”", 186, 650, 200, color="grey", t=c("play"))
s.source(S1)

s, c = line_scene("In nineteen forty-seven, Lego bought")
s.kicker("1947", 192, 200, c("1947|nineteen"))
s.text("A plastic moulding machine", 186, 260, 170, t=c("machine"))
s.kicker("1949", 192, 560, c("two"))
s.text("Bricks that click together", 186, 620, 170, t=c("bricks"))
s.source(S1)


s, c = line_scene("Lego called them Automatic")
photo_card(s, "pile_color", 1120, 160, 600, 420, 0.1, rot=1.2)
s.kicker("1949", 192, 300, 0.2)
s.text("Automatic\nBinding Bricks", 186, 360, 200, t=c("automatic"))
s.source(S1)

s, c = line_scene("They didn't hold together very well")
photo_card(s, "brick_black", 1100, 200, 620, 500, 0.3, rot=1.5)
s.text("They didn't\nhold", 186, 260, 230, t=c("hold"))
s.kicker("so the company kept working on it", 192, 820, c("working"), "grey")
s.source(PH)

s, c = line_scene("In nineteen fifty-eight, Lego patented")
photo_card(s, "patent2", 1120, 90, 600, 860, c("patented"), rot=-1)
s.kicker("Patent · 1958", 192, 220, c("1958|nineteen"))
s.text("Tubes\nunderneath", 186, 290, 200, t=c("tubes"))
s.text("Lock together.\nStay together.", 186, 690, 120, color="grey", t=c("lock"))
s.source("Image: US patent 3,005,282 (filed 1958) · public domain")

s, c = line_scene("That same year, Ole Kirk Christiansen")
photo_card(s, "p_ole", 1180, 110, 300, 400, 0.1, rot=-1.5, fit="cover")
photo_card(s, "p_godt", 1440, 330, 290, 600, c("son"), rot=1.5, fit="cover")
s.text("Ole Kirk\nChristiansen", 186, 160, 150, t=0.2)
s.kicker("Dies 1958", 192, 470, c("died"), "grey")
s.text("His son, Godtfred,\ntakes over", 186, 600, 140, t=c("son"))
s.source(S1)


s, c = line_scene("A department store buyer")
s.text("Not another toy.", 186, 220, 200, color="grey", t=c("another"))
s.text("A system of play.", 186, 480, 280, t=c("system"))
s.kicker("What a store buyer told Godtfred", 192, 860, c("godtfred|godfred|buyer"), "grey")
s.source(S2)

s, c = line_scene("In nineteen sixty, a fire destroyed")
s.kicker("1960", 192, 200, c("1960|nineteen"))
s.text("Fire", 186, 260, 300, t=c("fire"), mode="on")
s.text("Wooden toys", 186, 560, 150, color="grey", t=c("wooden"))
s.strike(176, 620, 760, c("wooden", off=0.4), 14)
photo_card(s, "brick_black", 1060, 300, 660, 500, c("brick"), rot=-1.5)
s.source(S1)

s, c = line_scene("And for decades, the brick was enough")
s.raw('<svg id="g14-ch" style="position:absolute;left:960px;top:220px" width="760" height="560" viewBox="0 0 760 560">'
      '<polyline id="g14-ln" points="0,540 125,500 250,440 375,370 500,280 625,170 760,30" fill="none" stroke="#141414" stroke-width="12" stroke-dasharray="1200" stroke-dashoffset="1200"/></svg>',
      js=f"tl.fromTo('#g14-ln', {{ strokeDashoffset: 1200 }}, {{ strokeDashoffset: 0, duration: 2.4, ease: 'power1.inOut' }}, {c('1978|nineteen'):.3f});")
s.kicker("1978 → 1993", 192, 260, c("1978|nineteen"))
s.text("14% a year", 186, 320, 260, t=c("14|fourteen"))
s.text("Doubling every\n~5 years", 186, 640, 130, color="grey", t=c("doubling"))
s.source(S2)


s, c = line_scene("Over the years, Lego added")
s.photos([("police2", 0)], rate=0.02)
s.raw(FADE)
x = 192
for w, lab in [("space", "Space"), ("castle", "Castles"), ("pirate", "Pirates"), ("wild|west", "Wild West")]:
    s.el(lab, f"left:{x}px;top:840px;background:#F7F5F0;padding:14px 22px", "kick", c(w)); x += len(lab) * 33 + 90
s.text("Themed sets", 186, 640, 190, color="np", t=c("themed"))
s.source(S2, light=True)

# =========================== CHAPTER 2 ===========================
chapter("ch2", "Too many ideas", ["ll_temple", "sw_deathstar", "bionicle", "ll_windsor", "sw_speeder", "ll_calif", "ll_traffic", "minifig_xmas", "ll_mini"], d=3.2)

s, c = line_scene("Then, in the nineteen nineties")
s.raw('<svg style="position:absolute;left:192px;top:420px" width="1536" height="420" viewBox="0 0 1536 420">'
      '<polyline id="g15-ln" points="0,400 300,260 600,120 1536,120" fill="none" stroke="#141414" stroke-width="12" stroke-dasharray="1800" stroke-dashoffset="1800"/></svg>',
      js=f"tl.fromTo('#g15-ln', {{ strokeDashoffset: 1800 }}, {{ strokeDashoffset: 0, duration: 1.6, ease: 'power1.inOut' }}, 0.2);")
s.kicker("The 1990s", 192, 200, c("1990|nineteen"))
s.text("Growth stops", 186, 260, 200, t=c("stopped"))
s.source(S2)

s, c = line_scene("Lego tripled the number")
s.text("New toys ×3", 186, 220, 280, t=c("tripled"))
s.text("Sales: flat", 186, 560, 280, color="grey", t=c("sales"))
s.source(S2)


s, c = line_scene("Every new product added costs")
s.text("Costs \u2191", 186, 220, 300, t=c("costs"))
s.text("Profits \u2193", 186, 560, 300, color="red", t=c("profits"))
s.source(S2)

s, c = line_scene("And Lego was a fixed-cost")
s.photos([("kladno", 0)], rate=0.02)
s.raw(DIM)
s.text("A fixed-cost business", 186, 320, 200, color="np", t=c("fixed"))
s.kicker("The factories cost the same either way", 192, 600, c("factories"), "np")
s.source(S2 + " \u00b7 photo: Lego factory, Kladno (public domain)", light=True)

s, c = line_scene("Meanwhile, Lego sets were getting")
s.text("Lego \u2191", 186, 220, 300, t=c("expensive"))
s.text("Other toys \u2193", 186, 560, 300, color="grey", t=c("cheaper"))
s.kicker("price", 192, 160, c("expensive"), "grey")
s.source(S2)

s, c = line_scene("In nineteen ninety-eight, Lego lost money")
s.kicker("1998", 192, 200, c("1998|nineteen"))
s.stamp("First loss", 200, 280, 220, c("lost"))
s.dots(1100, 300, 40, 25, 15, c("thousand|1000"), d=1.0, total=1000, shape="sq")
s.text("1,000 jobs", 186, 720, 170, t=c("jobs"))
s.source(S2 + "; The Telegraph (2009)")

s, c = line_scene("Its answer was to look beyond")
photo_card(s, "brick_black", 760, 420, 520, 400, 0.2, rot=0)
s.text("Beyond the brick", 186, 140, 200, t=c("beyond"))
s.source(PH)


s, c = line_scene("One study told Lego")
s.kicker("One study", 192, 220, c("study"))
s.text("Most kids didn't\nlike Lego", 186, 290, 260, t=c("children"))
s.source(S2)

s, c = line_scene("Lego built theme parks")
s.photos([("ll_windsor", 0), ("sw_deathstar", c("star", off=-0.2))], rate=0.03)
s.raw(FADE)
for k, (w, lab) in enumerate([("theme", "Legoland"), ("video", "Games"), ("tv", "TV"), ("star", "Star Wars"), ("harry", "Harry Potter")]):
    s.el(lab, f"left:{192 + (k % 3) * 400}px;top:{620 + (k // 3) * 110}px;background:#141414;padding:14px 22px", "kick np", c(w))
s.source(S2 + "; Blackstone (2005)", light=True)

s, c = line_scene("It made an action figure called Galidor")
s.text("Galidor", 186, 160, 300, t=c("called"))
x = 192
for w, lab in [("electronics", "Electronics"), ("video", "Video game"), ("tv", "TV show"), ("mcdonald", "McDonald's")]:
    s.el(lab, f"left:{x}px;top:520px;border:5px solid #141414;padding:12px 20px", "kick", c(w)); x += len(lab) * 33 + 100
s.text("“A huge, expensive failure”", 186, 700, 140, color="red", t=c("huge"))
s.kicker("David Robertson, author of Brick by Brick", 192, 880, c("author"), "grey")
s.source(S2)

s, c = line_scene("It made sets called Jack Stone")
s.raw('<div id="g21-lg" class="o0" style="position:absolute;left:192px;top:160px;width:900px;height:270px;background:#F7F5F0;box-shadow:0 14px 30px rgba(0,0,0,.2)"><img src="assets/img/logo_jackstone.png" style="width:100%;height:100%;object-fit:contain" alt=""></div>', js=f"on('#g21-lg', {c('jack'):.3f});"); s.click(c("jack"))
s.kicker("For kids who didn't like Lego", 192, 520, c("didn't"))
s.count(186, 590, 300, c("10|ten"), 10, "v => Math.round(v) + ' min'", d=0.8)
s.kicker("to build", 192, 880, c("minutes"), "grey")
s.source(S2)

s, c = line_scene("Every new idea needed new pieces")
s.dots(1120, 160, 40, 46, 14, c("pieces"), d=1.6, shape="sq")
s.kicker("Different pieces, early 2000s", 192, 260, c("early|2000"))
s.count(186, 320, 260, c("12|twelve"), 12900, INT, d=1.4)
s.source(S9)


s, c = line_scene("Robertson put it simply")
s.quote(192, 170, 1536, 620, "DAVID ROBERTSON, BRICK BY BRICK", "\u201cThey lost control of the innovation\u201d", "Knowledge at Wharton interview", c("lost"), qsize=170)
s.source(S2)

s, c = line_scene("The movie sets sold well")
s.photos([("sw_speeder", 0)], rate=0.02)
s.raw(DIM)
for k, y in enumerate(["1999", "2001", "2002"]):
    s.el(y, f"left:{192 + k * 300}px;top:760px;background:#F7F5F0;padding:14px 22px", "kick", c("movie", 1, off=k * 0.25))
s.text("Only in movie years", 186, 580, 150, color="np", t=c("only"))
s.source(S2, light=True)


s, c = line_scene("Robertson called the licensed")
s.kicker("Robertson, on the movie sets", 192, 150, c("robertson"), "grey")
s.text("\u201cA thick layer of cosmetics", 186, 220, 170, t=c("thick"))
s.text("that hid a pretty ugly", 186, 420, 170, t=c("hid|hit"))
s.text("business underneath\u201d", 186, 620, 170, t=c("business"))
s.source(S2)

s, c = line_scene("In two thousand three, there wasn't")
s.raw('<svg style="position:absolute;left:960px;top:200px" width="760" height="680" viewBox="0 0 760 680">'
      '<polyline id="g24-a" points="0,120 380,80" fill="none" stroke="#141414" stroke-width="12"/>'
      '<polyline id="g24-b" points="380,80 760,640" fill="none" stroke="#D7261E" stroke-width="12" stroke-dasharray="800" stroke-dashoffset="800"/></svg>',
      js=f"tl.fromTo('#g24-b', {{ strokeDashoffset: 800 }}, {{ strokeDashoffset: 0, duration: 0.6, ease: 'power3.in' }}, {c('cliff', off=-0.3):.3f});")
s.kicker("2003", 192, 260, c("2003|two"))
s.text("No movie", 186, 320, 260, t=c("wasn't"))
s.text("Off a cliff", 186, 620, 200, color="grey", t=c("cliff"))
s.source(S2)

s, c = line_scene("Lego's sales fell twenty-six percent")
s.kicker("2003 · sales", 192, 160, c("sales"))
s.text("DKK 11.4B → 8.4B", 186, 220, 200, t=c("11|eleven"))
s.text("−26%", 186, 440, 280, color="red", t=c("26|twenty"))
s.kicker("Loss: DKK 1.4B", 192, 800, c("lost"))
s.source(S3)

s, c = line_scene("And the next year was worse")
s.kicker("2004", 192, 200, c("2004|two"))
s.stamp("Loss DKK 1.93B", 200, 300, 220, c("lost"))
s.text("Worse", 186, 680, 180, color="grey", t=c("worse"))
s.source(S4)

# =========================== CHAPTER 3 ===========================
chapter("ch3", "The outsider", ["p_knud", "hq", "kladno", "police1", "pile_grey", "p_kjeld", "ll_temple", "police2", "brick_black"], d=3.2)

s, c = line_scene("The family that owned Lego")
photo_card(s, "family", 960, 200, 760, 520, 0.2, rot=1.2)
s.kicker("The founding family", 192, 440, c("family"), "grey")
s.text("A choice", 186, 180, 260, t=c("choice"))

s, c = line_scene("In late two thousand four, the head")
portrait(s, "p_kjeld", "Kjeld Kirk Kristiansen", "Grandson of the founder", c("head"), pos="50% 25%", until=c("outsider", off=-0.4))
s.kicker("Late 2004", 192, 300, c("2004|late"))
s.text("An outsider", 186, 380, 260, t=c("outsider"))
s.source("Source: IMD case study, The LEGO Group (B)")

s, c = line_scene("Jørgen Vig Knudstorp was thirty-five")
portrait(s, "p_knud", "Jørgen Vig Knudstorp", "Age 35 · ex-McKinsey", 0.1, pos="50% 25%")
s.kicker("Joined Lego 2001", 192, 860, c("joined"), "grey")
s.source("Sources: Knudstorp (Wikipedia); IMD case study")

s, c = line_scene("His plan was simple")
s.text("Stop doing everything.", 186, 220, 200, t=c("stop"))
s.text("The brick.", 186, 500, 340, t=c("brick"), mode="on")
s.source(S9)

s, c = line_scene("He cut the number of different")
s.dots(1120, 180, 40, 46, 14, 0.1, d=0.4, shape="sq")
s.raw('<div id="g31-w" class="o0" style="position:absolute;left:1110px;top:170px;width:580px;height:0;background:#E9E6DF"></div>',
      js=f"tl.fromTo('#g31-w', {{ opacity: 1, height: 0 }}, {{ height: 305, duration: 0.9, ease: 'power2.inOut' }}, {c('7|seven'):.3f});")
s.text("12,900", 186, 200, 220, color="grey", t=0.2)
s.strike(176, 300, 560, c("7|seven", off=-0.4), 14)
s.text("7,000", 186, 460, 340, t=c("7|seven"))
s.kicker("different pieces", 192, 840, c("7|seven", off=0.4))
s.source(S9)

s, c = line_scene("Fewer pieces meant fewer moulds")
s.text("Fewer moulds", 186, 240, 250, t=c("molds|moulds"))
s.text("Fewer parts in stock", 186, 560, 200, color="grey", t=c("parts"))

s, c = line_scene("Designers were asked to work")
s.photos([("police2", 0)], rate=0.02)
s.raw(FADE)
s.text("Inside the brick system", 186, 640, 170, color="np", t=c("inside"))
s.kicker("The same parts, many sets", 192, 860, c("reused"), "np")
s.source(S2, light=True)

s, c = line_scene("Then he sold the theme parks")
s.photos([("ll_windsor", 0), ("ll_calif", c("four|4", off=-0.2))], rate=0.025)
sh = s.sheet(96, 520, 1728, 400, c("blackstone"), "bottom")
s.in_sheet(sh, "4 Legoland parks → Blackstone", 96, 50, 130, t=c("blackstone"))
s.in_sheet(sh, "€375M · Lego keeps 30%", 96, 220, 130, t=c("€375|375|three"))
s.source("Source: Blackstone press release (July 2005)", light=True)


s, c = line_scene("The parks were in Denmark")
s.photos([("ll_temple", 0), ("ll_windsor", c("england", off=-0.2)), ("ll_calif", c("california", off=-0.2))], rate=0.03)
s.raw(FADE)
x = 192
for w, lab in [("denmark", "Denmark"), ("england", "England"), ("germany", "Germany"), ("california", "California")]:
    s.el(lab, f"left:{x}px;top:820px;background:#F7F5F0;padding:14px 22px", "kick", c(w)); x += len(lab) * 33 + 90
s.source("Source: Blackstone press release (July 2005)", light=True)

s, c = line_scene("Lego closed a factory in Switzerland")
s.photos([("kladno", c("czech", off=-0.3))], rate=0.02)
s.raw('<div id="g42-bk" class="fill" style="background:#E9E6DF"></div>', js=f"off('#g42-bk', {c('czech', off=-0.3):.3f});")
sw = s.text("Switzerland", 186, 300, 240, color="grey", t=c("switzerland"))
s.js.append(f"off('#{sw}', {c('czech', off=-0.3):.3f});")
s.el("Kladno, Czech Republic", "left:192px;top:820px;background:#141414;padding:14px 22px", "kick np", c("czech"))
s.source(S4 + " · photo: Lego factory, Kladno (public domain)", light=True)

s, c = line_scene("And the products went back to basics")
s.photos([("police1", 0), ("police2", c("fire", off=-0.2))], rate=0.025)
s.raw(FADE)
s.text("Back to basics", 186, 640, 190, color="np", t=c("basics"))
s.kicker("Police stations · fire trucks", 192, 860, c("police"), "np")
s.source(S2, light=True)

s, c = line_scene("It worked fast")
s.kicker("2005", 192, 220, c("2005|two"))
s.text("Profit", 186, 280, 240, t=c("profit"))
s.count(186, 520, 260, c("$505|505|five"), 505, "v => 'DKK ' + Math.round(v) + 'M'", d=1.2)
s.text("Sales +12%", 1180, 560, 170, color="grey", t=c("12|twelve"))
s.source(S4)

# =========================== CHAPTER 4 ===========================
chapter("ch4", "The biggest toy company", ["friends", "store_london", "house", "mattel", "store_glasgow", "ll_windsor", "house2", "store_booragoon", "hq"], d=3.2)

s, c = line_scene("Lego kept growing")
photo_card(s, "friends", 1200, 160, 520, 400, c("friends"), rot=1.2)
s.text("Lego Friends", 186, 220, 220, t=c("friends"))
s.text("Criticised", 186, 520, 160, color="grey", t=c("criticized|criticised"))
s.text("Sold anyway", 186, 700, 160, t=c("anyway"))
s.source(S2)

s, c = line_scene("In February twenty fourteen")
s.photos([("store_london", 0)], rate=0.02)
s.raw(DIM)
s.kicker("February 2014", 192, 360, c("february"), "np")
s.text("The Lego Movie", 186, 420, 260, color="np", t=c("movie"))
s.source("Source: RTÉ (September 2014)", light=True)


s, c = line_scene("Robertson's explanation")
s.photos([("house2", 0)], rate=0.02)
s.raw(DIM)
s.text("Build a world.", 186, 300, 240, color="np", t=c("build"))
s.text("Play out a story.", 186, 560, 240, color="np", t=c("story"))
s.source(S2, light=True)

s, c = line_scene("That year, in the first half")
photo_card(s, "mattel", 1180, 150, 540, 360, c("mattel|mattle"), rot=-1.2)
s.kicker("First half of 2014", 192, 160, c("first"))
s.text("Sales +11%", 186, 220, 200, t=c("11|eleven"))
s.text("DKK 11.5B", 186, 420, 200, t=c("billion"))
s.text("Passes Mattel", 186, 640, 200, t=c("mattel|mattle"))
s.source("Source: RTÉ (September 2014)")

s, c = line_scene("Ten years after nearly going under", hold=0.4)
s.text("2004", 186, 300, 300, color="grey", t=0.15)
s.text("→ 2014", 760, 300, 300, t=c("after"))
s.kicker("from almost bankrupt to No. 1", 192, 700, c("under"))

s, c = line_scene("And the theme parks?")
s.photos([("ll_temple", 0)], rate=0.02)
s.raw(FADE)
s.kicker("2019", 192, 600, c("2019|twenty"), "np")
s.text("KIRKBI + partners → Merlin", 186, 660, 140, color="np", t=c("merlin"))
s.text("£6B deal", 186, 820, 120, color="np", t=c("£6|6|six"))
s.source("Source: Fortune (June 2019)", light=True)


s, c = line_scene("That family company, KIRKBI")
s.kicker("KIRKBI \u00b7 the family's company", 192, 240, c("kirkbi|family"))
s.count(186, 310, 380, c("seventy|75"), 75, "v => Math.round(v) + '%'", d=1.0)
s.kicker("of Lego", 192, 740, c("lego", off=0.2))
s.source("Source: Fortune (June 2019)")

s, c = line_scene("The parks Lego sold to survive")
s.text("Sold to survive.", 186, 240, 220, color="grey", t=c("sold"))
s.text("Bought back.", 186, 520, 300, t=c("back"))

s, c = line_scene("Knudstorp stayed in charge")
portrait(s, "p_knud", "Knudstorp", "CEO 2004–2017", 0.1, pos="50% 25%")
s.source("Source: Knudstorp (Wikipedia)")

s, c = line_scene("And in twenty twenty-five")
s.photos([("house", 0)], rate=0.02)
s.raw(DIM)
s.kicker("2025 · record revenue", 192, 300, c("2025|twenty"), "np")
s.count(186, 370, 300, c("83|eighty"), 83.5, "v => 'DKK ' + v.toFixed(1) + 'B'", color="np", d=1.4)
s.source("Source: The LEGO Group (March 2026)", light=True)


s, c = line_scene("Revenue grew twelve percent")
s.kicker("2025", 192, 180, 0.2)
s.text("Revenue +12%", 186, 240, 220, t=c("12|twelve"))
s.kicker("Operating profit", 192, 540, c("operating"))
s.count(186, 600, 260, c("22|twenty"), 22.0, "v => 'DKK ' + v.toFixed(1) + 'B'", d=1.2)
s.source("Source: The LEGO Group (March 2026)")

s, c = line_scene("Its profit that year was")
s.kicker("2025 profit", 192, 160, c("profit"))
s.count(186, 220, 260, c("$16|16|sixteen"), 16.7, "v => 'DKK ' + v.toFixed(1) + 'B'", d=1.2)
s.kicker("2004 loss", 192, 560, c("lost"))
s.text("DKK 1.93B", 186, 620, 200, color="red", t=c("lost"))
s.text("8×", 1240, 260, 360, t=c("eight|8"), mode="on")
s.source("Sources: The LEGO Group (2026); AP (2006)")

# =========================== ENDING ===========================
s, c = line_scene("The patents on the Lego brick")
photo_card(s, "pebe", 1120, 160, 600, 600, c("other"), rot=-1)
s.text("Patent expired", 186, 220, 220, t=c("ran"))
s.kicker("Bricks that fit, for less", 192, 520, c("fit"), "grey")
s.source(S2 + " · photo: PEBE vs Lego")

s, c = line_scene("But Lego didn't come back")
s.photos([("brick_black", 0)], rate=0.02)
s.raw(FADE)
s.text("Not something new", 186, 600, 150, color="np", t=c("inventing"))
s.text("What it already was", 186, 780, 150, color="np", t=c("remembering"))
s.source(PH, light=True)

s, c = line_scene("When it tried to be everything")
s.text("Everything", 186, 220, 260, color="grey", t=c("everything"))
s.text("Nothing", 186, 540, 300, color="red", t=c("nothing"))

s, c = line_scene("Sometimes the way to save", hold=1.0, punch=True)
s.text("Do less.", 186, 220, 300, t=c("less"))
s.text("Do it well.", 186, 540, 300, t=c("well"))
s.kicker("Leg godt · play well", 192, 880, c("well", off=0.5), "grey")

end_card("This is Paper Empire", "BlackBerry", "The phone every business leader carried, and why its keyboard became a trap")
finish()
