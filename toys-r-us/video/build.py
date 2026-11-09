# Toys "R" Us: "Amazon Didn't Kill It" (Paper Empire). One block per voice line. Run: python3 build.py
# Written before the voice was recorded: after recording, run words.py and fix any cue the build reports.
import sys, os; sys.path.insert(0, os.path.abspath("../../kit"))
from build_lib import *
import build_lib; build_lib.GAP = 0.85

PH = "Photo: Wikimedia Commons (credits in description)"

# =========================== COLD OPEN ===========================
s, c = line_scene("In March twenty eighteen, every", "ink")
s.photos([("closing1", 0), ("closing3", c("america|close", off=-0.6))], rate=0.03)
s.raw('<div class="fill" style="background:rgba(20,20,20,.45)"></div>')
s.kicker("March 2018", 192, 300, c("march"), "np")
s.stamp("Closing", 200, 380, 240, c("close"))
s.source("Photos: Toys \"R\" Us store closing · Wikimedia Commons, CC BY 2.0", light=True)

s, c = line_scene("Seven hundred and thirty-five stores")
s.dots(192, 160, 35, 21, 30, c("seven|735"), d=1.0, total=735, shape="sq")
s.text("735 stores", 1300, 220, 150, t=c("stores"))
s.count(1300, 620, 150, c("thirty|33"), 33000, INT, d=1.2)
s.kicker("jobs", 1306, 790, c("jobs"))
s.source("Source: CBS News (2018)")

s, c = line_scene("The headlines had an easy answer")
s.kicker("The headlines", 192, 200, c("headlines"), "grey")
s.text("Amazon killed\nToys \"R\" Us", 186, 270, 260, t=c("amazon"))

s, c = line_scene("But Toys R Us didn't ignore Amazon")
s.text("Amazon killed Toys \"R\" Us", 186, 120, 130, color="grey", t=0.05, mode="on")
s.strike(176, 175, 1200, c("didn't|ignore"), 16)
s.text("2000 · partners", 186, 380, 200, t=c("two|2000"))
s.text("Then it sued Amazon, and won", 186, 640, 150, t=c("sued"))
s.source("Sources: CNN Money (2004); NBC News (2006)")

s, c = line_scene("What really buried Toys R Us", "ink", hold=0.6)
s.kicker("2005 · a deal in a boardroom", 192, 220, c("boardroom"), "np")
s.count(186, 300, 330, c("four|400|$400"), 400, money("$", "M"), color="red", d=1.4)
s.text("a year, just in interest", 186, 700, 150, color="np", t=c("interest"))
s.source("Source: Private Equity Stakeholder Project; bankruptcy coverage (2017)", light=True)

s, c = line_scene("This is the story of the store", "ink", hold=0.6)
s.raw(f'<div id="t05-crown" class="o0" style="position:absolute;left:192px;top:300px">{CROWN_SVG.format(s=180)}</div>', js="on('#t05-crown', 0.25);")
s.kicker("Paper Empire", 410, 360, 0.3, "np")
s.text("Toys \"R\" Us", 186, 520, 300, color="np", t=c("store"))
s.kicker("The store every kid dreamed about, and the debt that buried it", 192, 840, c("debt|death"), "np")
s.click(c("store"), "impact", 0.4)

# =========================== CHAPTER 1 ===========================
chapter("ch1", "A supermarket for toys", ["store_denver", "times2005", "p_geoffrey1965", "ferris", "p_store_dfw", "times_outside", "store_denver", "p_times_b", "ferris"], d=3.2)

s, c = line_scene("The story starts with a young man")
s.kicker("Born 1923 · Washington, D.C.", 192, 260, c("washington|born"))
s.text("Charles Lazarus", 186, 330, 300, t=c("charles"))
s.source("Source: AP obituary (2018)")

s, c = line_scene("After the Second World War")
s.kicker("1948", 192, 260, c("nineteen|1948"))
s.text("A store for baby furniture", 186, 330, 200, t=c("furniture"))

s, c = line_scene("It was the start of the baby boom")
s.kicker("The baby boom", 192, 200, c("boom"))
s.text("“Do you sell toys?”", 186, 280, 260, t=c("toys"))

s, c = line_scene("Lazarus had a simple idea")
s.text("Not a corner of the store.", 186, 220, 170, color="grey", t=c("corner"))
s.text("The whole store.", 186, 480, 300, t=c("whole"))

s, c = line_scene("In nineteen fifty-seven, he opened")
s.kicker("1957 · the first Toys \"R\" Us", 192, 200, c("nineteen|1957"))
rid = s.i("R")
s.raw(f'<div id="{rid}" class="lg o0" style="position:absolute;left:186px;top:300px;font-size:520px">R</div>',
      js=f"tl.fromTo('#{rid}', {{ opacity: 1, scaleX: 1 }}, {{ scaleX: -1, duration: 0.5, ease: 'power3.inOut' }}, {c('backwards'):.3f});")
s.text("Backwards, like\na child wrote it", 700, 360, 140, t=c("child"))
s.source("Source: AP obituary of Charles Lazarus (2018)")

s, c = line_scene("The idea was a supermarket for toys")
photo_card(s, "p_store_dfw", 1180, 120, 520, 840, c("supermarket"), rot=-1.2)
for k, (w, lab) in enumerate([("huge", "Huge stores"), ("every", "Every toy"), ("low", "Low prices")]):
    s.text(lab, 186, 180 + k * 240, 190, t=c(w))
s.source(PH)

s, c = line_scene("It worked. For decades")
s.photos([("store_denver", 0), ("times2005", c("birthdays", off=-0.3))], rate=0.03)
s.raw('<div class="fill" style="background:linear-gradient(0deg,rgba(20,20,20,.85),rgba(20,20,20,0) 60%)"></div>')
s.text("Birthdays and holidays", 186, 760, 160, color="np", t=c("birthdays"))
s.source(PH, light=True)

s, c = line_scene("Its mascot, a giraffe named Geoffrey")
photo_card(s, "p_geoffrey1965", 1180, 110, 520, 860, c("geoffrey|jeffrey"), rot=1.2)
s.text("Geoffrey", 186, 300, 300, t=c("geoffrey|jeffrey"))
s.kicker("the giraffe", 192, 620, c("giraffe"))
s.source("Image: Geoffrey the Giraffe advert, 1965 · public domain")

s, c = line_scene("In nineteen eighty-two, it got a jingle")
s.kicker("1982 · the jingle", 192, 160, c("nineteen|1982"))
s.text("“I'm a Toys \"R\" Us kid”", 186, 240, 200, t=c("i'm|toys", off=-0.1) if False else c("line"))
s.text("Linda Kaplan Thaler", 186, 560, 140, color="grey", t=c("linda"))
s.text("James Patterson", 186, 720, 140, color="grey", t=c("james"))
s.source("Source: CNBC (2018)")

s, c = line_scene("It even went global")
s.kicker("December 1991", 192, 280, c("december"))
s.text("Japan", 186, 350, 400, t=c("japan"), mode="on")
s.source("Source: UPI (1992)")

s, c = line_scene("A few weeks later, in January")
s.kicker("January 1992 · Kashihara, Japan", 192, 180, c("january"))
s.text("The President of the\nUnited States opens\na Toys \"R\" Us", 186, 250, 170, t=c("president"))
s.kicker("Toured by Charles Lazarus himself", 192, 820, c("tour"), "grey")
s.source("Source: UPI (January 7 1992)")

s, c = line_scene("A toy store, opened with a president", hold=0.4)
s.text("That big.", 186, 320, 380, t=c("big"), mode="on")

s, c = line_scene("Lazarus stepped down")
s.kicker("1994", 192, 300, c("nineteen|1994"))
s.text("Lazarus steps down", 186, 370, 240, t=c("stepped"))

# =========================== CHAPTER 2 ===========================
chapter("ch2", "The Amazon deal", ["p_amazon_tower", "store_denver", "times_outside", "p_store_dfw", "closing2", "p_times_b", "store_denver", "times2005", "p_amazon_tower"], d=3.2)

s, c = line_scene("By then, Toys R Us had a new kind")
s.text("Not toy stores", 186, 220, 200, color="grey", t=c("not"))
s.text("Giant discount stores", 186, 480, 220, t=c("discount"))

s, c = line_scene("Walmart and Target sold toys too")
s.text("Walmart", 186, 200, 240, t=c("walmart"))
s.text("Target", 186, 460, 240, t=c("target"))
s.kicker("Toys: just one more aisle", 192, 760, c("aisle"))

s, c = line_scene("Then came the internet.", hold=0.4)
s.raw('<div id="t21-b" class="o0" style="position:absolute;left:260px;top:180px;width:1400px;height:720px;border:12px solid #141414"><div style="position:absolute;left:0;top:0;width:100%;height:70px;background:#141414"></div></div>', js=f"on('#t21-b', {c('internet'):.3f});")
s.text("The internet", 330, 420, 240, t=c("internet"))

s, c = line_scene("In two thousand, Toys R Us made a ten-year")
sh = s.sheet(96, 200, 1728, 640, c("deal"), "bottom")
s.in_sheet(sh, "Toys \"R\" Us + Amazon", 96, 70, 170, t=c("amazon"))
s.in_sheet(sh, "2000 · 10 years", 96, 290, 130, t=c("ten|10"))
s.in_sheet(sh, "Exclusive online seller", 96, 440, 130, t=c("exclusive"))
s.source("Source: CNN Money (2004)")

s, c = line_scene("In other words, the company")
photo_card(s, "p_amazon_tower", 1200, 120, 480, 840, c("blame"), rot=-1.2)
s.text("Amazon ran its\nwebsite", 186, 300, 190, t=c("running|website"))
s.source("Photo: Amazon's Day 1 tower, Seattle · Wikimedia Commons, CC BY-SA 4.0")

s, c = line_scene("It didn't last.")
s.stamp("Exclusive?", 200, 260, 220, c("exclusive"), ink=True)
s.text("Other sellers, same toys", 186, 640, 170, t=c("other"))
s.source("Source: NBC News (2006)")

s, c = line_scene("In two thousand four, Toys R Us sued")
s.text("2004 · sued", 186, 220, 220, t=c("sued"))
s.text("2006 · court: Amazon breached", 186, 500, 170, t=c("breached"))
s.source("Sources: CNN Money (2004); NBC News (2006)")

s, c = line_scene("In two thousand nine, Amazon agreed")
s.kicker("2009", 192, 260, c("two|2009"))
s.count(186, 330, 330, c("fifty|51|$51"), 51, money("$", "M"), d=1.2)
s.stamp("Settled", 1100, 420, 160, c("settle"), rot=-5, ink=True)
s.source("Source: ABC News (2009)")

s, c = line_scene("By then, Toys R Us had lost years")
s.text("Lost years online", 186, 220, 230, color="grey", t=c("lost"))
s.text("But that's not\nwhat sank it", 186, 500, 230, t=c("sink"))

# =========================== CHAPTER 3 ===========================
chapter("ch3", "The buyout", ["times2005", "ferris", "store_denver", "p_store_dfw", "times_outside", "closing4", "p_times_b", "closing2", "ferris"], d=3.2)

s, c = line_scene("In two thousand five, three investment firms")
s.kicker("2005 · the buyers", 192, 160, c("two|2005"))
for k, (w, lab) in enumerate([("kkr|k", "KKR"), ("bain", "Bain Capital"), ("vornado", "Vornado")]):
    s.text(lab, 186, 240 + k * 220, 200, t=c(w))
s.source("Source: Business Insider (2017)")

s, c = line_scene("The price was about six point six")
s.count(186, 300, 420, c("six|$6"), 6.6, "v => '$' + v.toFixed(1) + 'B'", d=1.3)

s, c = line_scene("But they didn't pay most of it themselves")
s.raw('<div id="t30-a" class="o0" style="position:absolute;left:192px;top:340px;width:300px;height:200px;background:#141414"></div>'
      '<div id="t30-b" class="o0" style="position:absolute;left:492px;top:340px;width:1236px;height:200px;background:#D7261E;transform-origin:0 50%"></div>',
      js=f"on('#t30-a', {c('one|$1'):.3f}); tl.fromTo('#t30-b', {{ opacity: 1, scaleX: 0 }}, {{ scaleX: 1, duration: 0.8, ease: 'power2.out' }}, {c('borrowed'):.3f});")
s.text("≈$1.3B own money", 186, 200, 120, t=c("one|$1"))
s.text("The rest: borrowed", 700, 580, 140, color="red", t=c("borrowed"))
s.source("Source: Business Insider (2017)")

s, c = line_scene("This is called a leveraged buyout")
s.text("A leveraged buyout", 186, 160, 200, t=c("leveraged"))
s.text("The debt belonged\nto Toys \"R\" Us", 186, 460, 220, color="red", t=c("belonged"))

s, c = line_scene("Think of it like buying a house")
house = ('<svg id="t32-h" class="o0" style="position:absolute;left:1100px;top:180px" width="600" height="640" viewBox="0 0 600 640">'
         '<path d="M40 280 L300 60 L560 280 L560 620 L40 620 Z" fill="none" stroke="#141414" stroke-width="14"/>'
         '<rect x="80" y="520" width="90" height="80" fill="#141414"/><rect id="t32-m" x="190" y="320" width="330" height="280" fill="#D7261E" opacity="0"/></svg>')
s.raw(house, js=f"on('#t32-h', {c('house'):.3f}); on('#t32-m', {c('mortgage'):.3f});")
s.text("Small deposit", 186, 260, 180, t=c("deposit"))
s.text("Giant mortgage", 186, 500, 180, color="red", t=c("mortgage"))
s.kicker("…and the house pays the mortgage", 192, 860, c("pay"))

s, c = line_scene("Overnight, the toy store owed")
s.text("Billions it never\nborrowed for itself", 186, 260, 230, t=c("billions"))

s, c = line_scene("And that debt came with interest")
s.kicker("At the bankruptcy · servicing the debt", 192, 180, c("bankruptcy"))
s.count(186, 260, 360, c("four|400|$400"), 400, money("$", "M"), color="red", d=1.3)
s.text("every year", 186, 690, 170, t=c("year"))
s.source("Source: Private Equity Stakeholder Project; bankruptcy coverage")

s, c = line_scene("Four hundred million dollars, every year")
for k, (w, lab) in enumerate([("stores", "Stores"), ("website", "Website"), ("prices", "Lower prices")]):
    s.text(lab, 186, 180 + k * 240, 200, color="grey", t=c(w))
    s.strike(176, 280 + k * 240, 600, c(w, off=0.3), 16)

s, c = line_scene("Meanwhile, the owners did fine")
s.quote(960, 150, 760, 680, "ESTIMATE · PRIVATE EQUITY STAKEHOLDER PROJECT", "≈$464M in fees and interest", "Collected by KKR, Bain Capital and Vornado from Toys \"R\" Us (an advocacy group's estimate)", c("estimated"), qsize=130)
s.text("The owners\ndid fine", 186, 300, 190, t=c("fine"))
s.source("Source: Private Equity Stakeholder Project")

s, c = line_scene("The plan had been to fix the company")
s.text("Fix it, sell it", 186, 220, 220, color="grey", t=c("sell"))
s.strike(176, 320, 700, c("never", off=-0.2), 18)
s.text("It never happened", 186, 520, 220, t=c("never"))

s, c = line_scene("In twenty ten, the owners filed")
s.kicker("2010 · stock market listing", 192, 200, c("twenty|2010"))
s.text("$800M IPO", 186, 270, 280, t=c("eight|800|$800"))
s.stamp("Withdrawn · 2013", 200, 640, 170, c("withdrew"), rot=-5, ink=True)
s.source("Source: Fortune (March 2013)")

s, c = line_scene("In November two thousand one")
s.photos([("ferris", 0), ("times2005", c("december"))], rate=0.03)
s.raw('<div class="fill" style="background:linear-gradient(0deg,rgba(20,20,20,.85),rgba(20,20,20,0) 60%)"></div>')
s.kicker("Times Square · 2001–2015", 192, 680, c("times"), "np")
s.text("A Ferris wheel inside", 186, 750, 170, color="np", t=c("ferris"))
s.stamp("Closed", 1200, 200, 170, c("closed"))
s.source("Sources: CBS New York; CNN Money (Dec 2015) · " + PH, light=True)

# =========================== CHAPTER 4 ===========================
chapter("ch4", "The last Christmas", ["closing1", "closing2", "closing3", "closing4", "closing5", "babies_abandoned", "closing1", "closing3", "closing5"], d=3.2)

s, c = line_scene("As shopping moved online")
s.text("The brand: yes", 186, 220, 230, t=c("brand"))
s.text("Money to spare: no", 186, 500, 230, color="red", t=c("money"))

s, c = line_scene("In September twenty seventeen, reports")
s.quote(192, 160, 1536, 600, "SEPTEMBER 2017", "Toys \"R\" Us weighs bankruptcy", "Headline as reported (Wall Street Journal); rebuilt for illustration", c("reports"), qsize=130)

s, c = line_scene("Toy makers began refusing")
s.stamp("Cash up front", 200, 220, 220, c("cash"), ink=True)
s.kicker("Right before Christmas", 192, 640, c("christmas"))
s.source("Sources: Wall Street Journal; Reuters (Sept 2017)")

s, c = line_scene("Without toys on the shelves", "ink")
s.photos([("closing2", 0), ("closing4", c("christmas"))], rate=0.03)
s.raw('<div class="fill" style="background:rgba(20,20,20,.35)"></div>')
s.text("Nothing", 186, 760, 200, color="np", t=c("nothing"))
s.source("Photos: Toys \"R\" Us closing · Wikimedia Commons, CC BY 2.0", light=True)

s, c = line_scene("On September eighteenth")
s.kicker("September 18, 2017", 192, 180, c("september"))
s.stamp("Chapter 11", 200, 280, 260, c("chapter|11"))
s.text("$5B+ in debt", 186, 700, 180, color="red", t=c("five|$5"))
s.source("Sources: CBS News; court filing, E.D. Virginia")

s, c = line_scene("It hoped the holiday season")
s.kicker("December 2017", 192, 300, c("holiday"))
s.text("Buy it time", 186, 370, 300, t=c("time"))

s, c = line_scene("It didn't. In March twenty eighteen")
s.photos([("closing5", 0)], rate=0.025, clicks=False)
s.raw('<div class="fill" style="background:rgba(20,20,20,.5)"></div>')
s.kicker("March 2018", 192, 300, c("march"), "np")
s.text("Every US store", 186, 370, 280, color="np", t=c("all|every"))
s.source(PH, light=True)

s, c = line_scene("Seven hundred and thirty-five stores. About")
d1 = s.dots(192, 120, 49, 15, 30, 0.1, d=0.01, total=735, shape="sq")
s.js.append(f"tl.fromTo('#root .{d1}-c', {{ backgroundColor: '#141414' }}, {{ backgroundColor: '#C9C5BB', duration: 0.001, stagger: 0.004, immediateRender: false }}, {c('seven|735'):.3f});")
s.text("33,000 people", 186, 640, 170, t=c("thirty|33"))
s.kicker("out of work", 192, 820, c("work"))
s.source("Source: CBS News (2018)")

s, c = line_scene("One week later, Charles Lazarus", "ink", hold=0.8)
s.text("Charles Lazarus", 186, 360, 220, color="np", t=c("charles"))
s.kicker("1923–2018", 192, 600, c("ninety|94"), "np")
s.source("Source: AP obituary (March 2018)", light=True)

s, c = line_scene("At first, the workers were told")
s.stamp("No severance", 200, 300, 230, c("severance"), ink=True)
s.source("Source: CBS News; BuzzFeed News (2018)")

s, c = line_scene("After months of protests")
s.text("KKR $10M", 186, 200, 200, t=c("kkr|k"))
s.text("+ Bain $10M", 186, 420, 200, t=c("bain"))
s.text("= $20M fund", 186, 640, 220, t=c("twenty|20|$20"))
s.source("Source: CBS News (2018)")

s, c = line_scene("The fund was run by Kenneth")
s.text("Kenneth Feinberg", 186, 300, 240, t=c("kenneth"))
s.kicker("Also ran the 9/11 victims' fund", 192, 580, c("september"))

s, c = line_scene("Advocates said the workers")
s.text("Still owed\ntens of millions", 186, 260, 240, color="grey", t=c("owed"))
s.kicker("Advocates' estimate", 192, 760, c("advocates"))

# =========================== CHAPTER 5 ===========================
chapter("ch5", "The giraffe comes back", ["macys1", "macys2", "p_geoffrey1965", "geoffrey_mascot", "macys1", "store_denver", "macys2", "p_store_dfw", "times2005"], d=3.2)

s, c = line_scene("The stores were gone")
photo_card(s, "p_geoffrey1965", 1180, 110, 520, 860, c("name"), rot=-1.2)
s.text("The stores: gone", 186, 220, 170, color="grey", t=c("gone"))
s.text("The name: still\nworth something", 186, 460, 170, t=c("worth"))

s, c = line_scene("In twenty twenty-one, a brand company")
s.text("WHP Global", 186, 220, 240, t=c("whp|global"))
s.text("+ Macy's", 186, 480, 240, t=c("macy"))
s.source("Source: Fashion United (Aug 2021)")

s, c = line_scene("From twenty twenty-two, Toys R Us shops")
s.photos([("macys1", 0), ("macys2", c("geoffrey|walls", off=-0.4))], rate=0.025)
s.raw('<div class="fill" style="background:linear-gradient(0deg,rgba(20,20,20,.85),rgba(20,20,20,0) 60%)"></div>')
s.kicker("2022 · inside Macy's", 192, 680, c("macy"), "np")
s.text("400+ stores", 186, 750, 180, color="np", t=c("four|400"))
s.source("Photos: Toys \"R\" Us shops in Macy's · Wikimedia Commons, CC BY-SA 4.0 / CC BY 4.0", light=True)

s, c = line_scene("The brand survived.")
s.text("The brand survived.", 186, 220, 240, t=c("brand"))
s.text("The company didn't.", 186, 500, 240, color="red", t=c("company"))

# =========================== ENDING ===========================
s, c = line_scene("It's easy to say Amazon killed")
s.text("Amazon killed it", 186, 260, 260, color="grey", t=c("amazon"))
s.kicker("a simple story", 192, 600, c("simple"), "grey")

s, c = line_scene("But Toys R Us was still selling")
s.text("Still selling\nbillions of dollars of toys", 186, 160, 170, t=c("billions"))
s.raw('<div id="t58-d" class="o0" style="position:absolute;left:192px;top:640px;width:1536px;height:200px;background:#D7261E;transform-origin:0 50%"></div>',
      js=f"tl.fromTo('#t58-d', {{ opacity: 1, scaleX: 0 }}, {{ scaleX: 1, duration: 0.9, ease: 'power2.inOut' }}, {c('debt'):.3f});")
s.text("The debt", 230, 680, 140, color="np", t=c("debt", off=0.5), mode="on")

s, c = line_scene("Every dollar that went to interest")
s.text("Interest", 186, 240, 260, color="red", t=c("interest"))
s.text("Not the future", 186, 520, 260, color="grey", t=c("future"))

s, c = line_scene("Sometimes a company isn't beaten", hold=1.0, punch=True)
s.text("Not beaten by competitors", 186, 220, 170, color="grey", t=c("beaten"))
s.text("Buried by the people\nwho bought it", 186, 460, 220, t=c("buried"))

end_card("This is Paper Empire", "Lego", "The toy company that almost went bankrupt, and saved itself by doing less")
finish()
