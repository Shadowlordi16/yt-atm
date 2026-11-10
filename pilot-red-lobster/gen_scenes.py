# Generates every scene in compositions/ for the Red Lobster pilot (RED INK look, see ../MOTION.md).
# Scene times: W(t) = 0.25 + the word's time in that scene's voice line (assets/vo/sNN.words.json).
import os

BASE = """
  <style>
    #root{position:absolute;inset:0;overflow:hidden;background:#E9E6DF;font-family:Inter,sans-serif;color:#141414}
    #root .paper{position:absolute;left:0;top:0;width:1920px;height:1080px;object-fit:cover}
    #root .photo{position:absolute;left:0;top:0;width:2112px;height:1188px;object-fit:cover}
    #root .lg{font-family:'League Gothic',sans-serif;text-transform:uppercase;line-height:.88;font-weight:400;font-variant-numeric:tabular-nums;white-space:nowrap}
    #root .kick{font-family:Inter,sans-serif;font-weight:900;font-size:48px;letter-spacing:.02em;text-transform:uppercase;white-space:nowrap}
    #root .body{font-family:Inter,sans-serif;font-weight:700;font-size:48px;white-space:nowrap}
    #root .src{position:absolute;left:192px;bottom:84px;font:400 28px Inter,sans-serif;color:#6B6963;white-space:nowrap}
    #root .red{color:#D7261E}
    #root .grey{color:#6B6963}
    #root .np{color:#E9E6DF}
    #root .src.np{text-shadow:0 2px 6px rgba(0,0,0,.85),0 0 18px rgba(0,0,0,.7)}
    #root .rule{position:absolute;height:8px;background:#141414;transform-origin:left center}
    #root .sheet{position:absolute;overflow:hidden;background:#E9E6DF;box-shadow:0 18px 40px rgba(0,0,0,.35)}
    @@CSS@@
  </style>"""

SCRIPT_HEAD = """
    const tl = gsap.timeline({ paused: true });
    const W = (t) => 0.25 + t;
    const show = (sel, t) => tl.fromTo(sel, { opacity: 0 }, { opacity: 1, duration: 0.01 }, t);
    const wipe = (sel, t, d = 0.28) => tl.fromTo(sel, { clipPath: 'inset(-10% 100% -10% 0)', opacity: 1 }, { clipPath: 'inset(-10% 0% -10% 0)', duration: d, ease: 'power3.out' }, t);
    const rule = (sel, t, d = 0.45) => tl.fromTo(sel, { scaleX: 0 }, { scaleX: 1, duration: d, ease: 'power2.inOut' }, t);
    const shake = (sel, t) => tl.fromTo(sel, { x: 0 }, { keyframes: [{ x: 6, duration: .033 }, { x: -5, duration: .033 }, { x: 3, duration: .033 }, { x: 0, duration: .033 }] }, t);
    const count = (sel, t, to, fmt, d = 1.4) => { const el = document.querySelector(sel); const o = { v: 0 };
      tl.fromTo(sel, { opacity: 0 }, { opacity: 1, duration: 0.01 }, t);
      tl.fromTo(o, { v: 0 }, { v: to, duration: d, ease: 'power2.out', onUpdate: () => { el.textContent = fmt(o.v); } }, t); };
"""

def scene(id, dur, css, markup, script):
    html = ("<template>" + BASE.replace("@@CSS@@", css) +
        f'\n  <div id="root" data-composition-id="{id}" data-width="1920" data-height="1080">\n{markup}\n  </div>\n'
        "  <script>\n    (function () {" + SCRIPT_HEAD + script +
        f"\n    tl.to({{}}, {{ duration: {dur} }}, 0);\n    window.__timelines[\"{id}\"] = tl;\n    }})();\n  </script>\n</template>\n")
    open(f"compositions/{id}.html", "w").write(html)

P = '<img class="paper" src="assets/paper.jpg" alt="">'
SHEET_P = '<img src="assets/paper.jpg" alt="" style="position:absolute;left:0;top:0;width:100%;height:100%;object-fit:cover">'
CC = "Photo: Harrison Keely / Wikimedia Commons, CC BY 4.0"

# s01: the hook, on the real sign
scene("s01", 6.3, """
    #s01-photo{left:0;top:0;width:1920px;height:1080px;transform-origin:25% 30%}
    #s01-sheet{left:1230px;top:0;width:690px;height:1080px}
    #s01-k{position:absolute;left:76px;top:150px;opacity:0}
    #s01-h{position:absolute;left:72px;top:236px;font-size:200px;opacity:0}
    #s01-n{position:absolute;left:68px;top:610px;font-size:290px;opacity:0}
    #s01-e{position:absolute;left:76px;top:900px;opacity:0}
    #s01-c{left:96px;opacity:.85}
""", f"""
    <img id="s01-photo" class="photo" src="assets/photos/sign.jpg" alt="Red Lobster sign, Chattanooga">
    <div id="s01-sheet" class="sheet">{SHEET_P}
      <div id="s01-k" class="kick grey">2023 · a new deal</div>
      <div id="s01-h" class="lg">Endless<br>shrimp</div>
      <div id="s01-n" class="lg">$20</div>
      <div id="s01-e" class="kick">All you can eat</div>
    </div>
    <div id="s01-c" class="src np">{CC}</div>
""", """
    tl.fromTo('#s01-photo', { scale: 1 }, { scale: 1.06, duration: 6.3, ease: 'none' }, 0);
    tl.fromTo('#s01-sheet', { xPercent: 100 }, { xPercent: 0, duration: 0.5, ease: 'expo.out' }, 2.6);
    tl.fromTo('#s01-photo', { x: 0 }, { x: -390, duration: 0.5, ease: 'expo.out' }, 2.6);
    show('#s01-k', 2.95);
    wipe('#s01-h', 0.3 + 2.80);
    show('#s01-n', 0.3 + 3.52);
    wipe('#s01-e', 0.3 + 4.56);
""")

# s02: $11M in one quarter
scene("s02", 6.8, """
    #s02-k{position:absolute;left:192px;top:150px;opacity:0}
    #s02-n{position:absolute;left:180px;top:240px;font-size:360px;opacity:0}
    #s02-r{left:192px;top:640px;width:1536px}
    #s02-b{position:absolute;left:192px;top:700px;font-size:180px;opacity:0}
""", f"""{P}
    <div id="s02-k" class="kick">Endless shrimp · one quarter</div>
    <div id="s02-n" class="lg red">−$0 million</div>
    <div id="s02-r" class="rule"></div>
    <div id="s02-b" class="lg">A year later: bankrupt</div>
    <div class="src">Source: Red Lobster Chapter 11 filing, via Yahoo Finance</div>
""", """
    show('#s02-k', W(0.32));
    count('#s02-n', W(1.76), 11, v => '−$' + Math.round(v) + ' million', 1.3);
    rule('#s02-r', W(3.76));
    wipe('#s02-b', W(5.44), 0.3);
""")

# s03: the myth, struck through
scene("s03", 5.6, """
    #s03-a{position:absolute;left:180px;top:150px;font-size:300px;opacity:0}
    #s03-x{position:absolute;left:170px;top:262px;width:1300px;height:22px;background:#D7261E;transform-origin:left center}
    #s03-b{position:absolute;left:186px;top:500px;font-size:250px;opacity:0}
    #s03-c{position:absolute;left:192px;top:760px;font-size:160px;opacity:0}
""", f"""{P}
    <div id="s03-a" class="lg">The shrimp did it</div>
    <div id="s03-x"></div>
    <div id="s03-b" class="lg">The last bite</div>
    <div id="s03-c" class="lg grey">Not the first</div>
""", """
    show('#s03-a', W(0.72));
    rule('#s03-x', W(2.08), 0.4);
    tl.fromTo('#s03-a', { color: '#141414' }, { color: '#6B6963', duration: 0.01 }, W(2.48));
    wipe('#s03-b', W(3.20));
    wipe('#s03-c', W(4.16));
""")

# s04: the 2014 deal
scene("s04", 9.1, """
    #s04-photo{left:-96px;top:-54px}
    #s04-yr{position:absolute;left:96px;top:96px;background:#141414;padding:30px 44px 6px;opacity:0}
    #s04-yr .lg{font-size:250px}
    #s04-sheet{left:96px;top:540px;width:1728px;height:444px}
    #s04-from{position:absolute;left:96px;top:64px;font-size:140px;opacity:0}
    #s04-r{left:470px;top:126px;width:300px}
    #s04-to{position:absolute;left:820px;top:64px;font-size:140px;opacity:0}
    #s04-amt{position:absolute;left:92px;top:220px;font-size:180px;opacity:0}
    #s04-src{position:absolute;right:56px;bottom:36px;font:400 28px Inter,sans-serif;color:#6B6963;opacity:0}
    #s04-c{left:1060px;top:470px;bottom:auto;opacity:.85}
""", f"""
    <img id="s04-photo" class="photo" src="assets/photos/exterior.jpg" alt="Red Lobster restaurant exterior">
    <div id="s04-yr"><div class="lg np">2014</div></div>
    <div id="s04-sheet" class="sheet">{SHEET_P}
      <div id="s04-from" class="lg">Darden</div>
      <div id="s04-r" class="rule"></div>
      <div id="s04-to" class="lg">Golden Gate Capital</div>
      <div id="s04-amt" class="lg">$2.1 billion</div>
      <div id="s04-src">Source: Darden Restaurants SEC filing, 2014</div>
    </div>
""", """
    tl.fromTo('#s04-photo', { scale: 1 }, { scale: 1.06, duration: 9.1, ease: 'none' }, 0);
    show('#s04-yr', W(1.52));
    tl.fromTo('#s04-sheet', { yPercent: 130 }, { yPercent: 0, duration: 0.5, ease: 'expo.out' }, W(2.4));
    show('#s04-from', W(2.72));
    rule('#s04-r', W(3.44), 0.5);
    wipe('#s04-to', W(4.72), 0.35);
    show('#s04-amt', W(6.48));
    show('#s04-src', W(6.48));
""")

# s05: ~500 buildings sold, then rented back
scene("s05", 8.4, """
    #s05-k{position:absolute;left:192px;top:150px;opacity:0}
    #s05-n{position:absolute;left:180px;top:230px;font-size:330px;opacity:0}
    #s05-l{position:absolute;left:192px;top:540px;font-size:110px;opacity:0}
    #s05-s{position:absolute;left:192px;top:670px;font-size:110px;opacity:0}
    #s05-rb{position:absolute;left:192px;top:800px;font-size:110px;opacity:0}
    #s05-grid{position:absolute;left:880px;top:150px;width:850px;height:700px;display:grid;grid-template-columns:repeat(25,28px);grid-auto-rows:28px;gap:7px 6px}
    #s05-grid svg{width:28px;height:28px;opacity:0}
""", f"""{P}
    <div id="s05-k" class="kick">The sale-leaseback</div>
    <div id="s05-n" class="lg">≈500</div>
    <div id="s05-l" class="lg">restaurant buildings</div>
    <div id="s05-s" class="lg">sold for $1.5 billion</div>
    <div id="s05-rb" class="lg red">then rented back</div>
    <div id="s05-grid" data-layout-ignore></div>
    <div class="src">Source: American Realty Capital Properties SEC filing, 2014</div>
""", """
    const g = document.getElementById('s05-grid');
    for (let i = 0; i < 500; i++) g.insertAdjacentHTML('beforeend', '<svg viewBox="0 0 28 28"><path d="M3 13 L14 4 L25 13 L25 26 L3 26 Z" fill="#141414"/></svg>');
    const houses = g.querySelectorAll('svg'), roofs = g.querySelectorAll('path');
    show('#s05-k', W(0.24));
    show('#s05-n', W(1.68));
    tl.fromTo(houses, { opacity: 0 }, { opacity: 1, duration: 0.01, stagger: 0.0016 }, W(1.68));
    wipe('#s05-l', W(2.32));
    wipe('#s05-s', W(3.60));
    tl.fromTo(roofs, { fill: '#141414' }, { fill: '#6B6963', duration: 0.01, stagger: 0.0012 }, W(3.60));
    wipe('#s05-rb', W(6.48));
    tl.fromTo(roofs, { fill: '#6B6963' }, { fill: '#D7261E', duration: 0.01, stagger: 0.0012, immediateRender: false }, W(6.80));
""")

# s06: rent on buildings it used to own, rising each year
bars = "".join(f'<div class="s06-bar" style="left:{i*58}px;height:{int(150*1.02**i)+150}px"></div>' for i in range(11))
scene("s06", 7.0, """
    #s06-photo{left:-96px;top:-54px}
    #s06-sheet{left:96px;top:420px;width:1728px;height:564px}
    #s06-h{position:absolute;left:96px;top:80px;font-size:140px;opacity:0}
    #s06-sub{position:absolute;left:96px;top:370px;opacity:0}
    #s06-ch{position:absolute;left:1060px;top:84px;width:620px;height:340px}
    #s06-ch .s06-bar{position:absolute;bottom:0;width:44px;background:#141414;transform-origin:bottom center}
    #s06-l0{position:absolute;left:1060px;top:440px;font:700 32px Inter,sans-serif}
    #s06-l1{position:absolute;left:1616px;top:440px;font:700 32px Inter,sans-serif}
    #s06-src{position:absolute;left:96px;bottom:36px;font:400 28px Inter,sans-serif;color:#6B6963;opacity:0}
""", f"""
    <img id="s06-photo" class="photo" src="assets/photos/front.jpg" alt="Red Lobster restaurant front">
    <div id="s06-sheet" class="sheet">{SHEET_P}
      <div id="s06-h" class="lg">Rent on restaurants<br>it used to own</div>
      <div id="s06-sub" class="kick">Up about 2% every year</div>
      <div id="s06-ch">{bars}</div>
      <div id="s06-l0" class="grey">2014</div><div id="s06-l1" class="grey">2024</div>
      <div id="s06-src">Source: Red Lobster Chapter 11 filing, via Yahoo Finance · bars show a 2% yearly rise</div>
    </div>
""", """
    tl.fromTo('#s06-photo', { scale: 1 }, { scale: 1.06, duration: 7.0, ease: 'none' }, 0);
    tl.fromTo('#s06-sheet', { yPercent: 130 }, { yPercent: 0, duration: 0.5, ease: 'expo.out' }, W(0.7));
    wipe('#s06-h', W(1.44), 0.35);
    tl.fromTo('#s06-ch .s06-bar', { scaleY: 0 }, { scaleY: 1, duration: 0.3, ease: 'power3.out', stagger: 0.09 }, W(4.16));
    wipe('#s06-sub', W(4.88));
    show('#s06-src', W(4.88));
""")

# s07: $190M a year in rent
scene("s07", 5.9, """
    #s07-k{position:absolute;left:192px;top:150px;opacity:0}
    #s07-n{position:absolute;left:176px;top:230px;font-size:520px;opacity:0}
    #s07-l{position:absolute;left:192px;top:740px;font-size:130px;opacity:0}
""", f"""{P}
    <div id="s07-k" class="kick">Rent · the year before it filed</div>
    <div id="s07-n" class="lg red">$0M+</div>
    <div id="s07-l" class="lg">in a single year</div>
    <div class="src">Source: Red Lobster Chapter 11 filing, via Yahoo Finance</div>
""", """
    show('#s07-k', W(0.24));
    count('#s07-n', W(3.10), 190, v => '$' + Math.round(v) + 'M+', 1.3);
    wipe('#s07-l', W(4.60), 0.35);
""")

# s08: Thai Union, and the filing's allegation
scene("s08", 10.6, """
    #s08-k{position:absolute;left:192px;top:150px;opacity:0}
    #s08-n{position:absolute;left:180px;top:230px;font-size:240px;opacity:0}
    #s08-o1{position:absolute;left:192px;top:480px;opacity:0}
    #s08-o2{position:absolute;left:192px;top:550px;opacity:0}
    #s08-card{position:absolute;left:1060px;top:130px;width:670px;height:500px;background:#F7F5F0;box-shadow:0 14px 30px rgba(0,0,0,.18);opacity:0}
    #s08-card .t{position:absolute;left:56px;top:52px;font:900 30px Inter,sans-serif;letter-spacing:.04em;color:#6B6963}
    #s08-card .q{position:absolute;left:56px;top:110px;width:560px;font-family:'League Gothic',sans-serif;font-size:104px;line-height:.92;text-transform:uppercase}
    #s08-card .a{position:absolute;left:56px;top:320px;width:560px;font:400 32px Inter,sans-serif;line-height:1.3}
    #s08-p{position:absolute;left:192px;top:800px;font-size:150px;opacity:0}
""", f"""{P}
    <div id="s08-k" class="kick grey">The shrimp supplier</div>
    <div id="s08-n" class="lg">Thai Union</div>
    <div id="s08-o1" class="body">2016 · bought a $575M stake</div>
    <div id="s08-o2" class="body">2020 · became a co-owner</div>
    <div id="s08-card"><div class="t">CHAPTER 11 FILING · ALLEGATION</div>
      <div class="q">“At the direction of Thai Union”</div>
      <div class="a">How the filing says the interim CEO was installed. He made $20 Endless Shrimp permanent in May 2023.</div></div>
    <div id="s08-p" class="lg">Endless shrimp → permanent</div>
    <div class="src">Source: Red Lobster Chapter 11 filing, via Yahoo Finance</div>
""", """
    show('#s08-k', W(0.40));
    wipe('#s08-n', W(1.68), 0.3);
    show('#s08-o1', W(2.80));
    show('#s08-o2', W(3.36));
    tl.fromTo('#s08-card', { opacity: 1, y: 70, rotation: -2.4 }, { y: 0, rotation: -1.2, duration: 0.45, ease: 'expo.out' }, W(5.04));
    wipe('#s08-p', W(8.64), 0.35);
""")

# s09: Thai Union's answer; guests down 30%
scene("s09", 7.8, """
    #s09-m{position:absolute;left:192px;top:150px;padding:24px 32px 8px;border:6px solid #6B6963;opacity:0}
    #s09-m .lg{font-size:110px;color:#6B6963}
    #s09-k{position:absolute;left:192px;top:440px;opacity:0}
    #s09-n{position:absolute;left:180px;top:520px;font-size:380px;opacity:0}
    #s09-c{position:absolute;left:1180px;top:150px;width:560px;height:760px}
    #s09-b0,#s09-b1{position:absolute;bottom:60px;width:230px;height:640px;transform-origin:bottom center}
    #s09-b0{left:0;background:#6B6963}
    #s09-b1{left:300px;background:#141414}
    #s09-l0,#s09-l1{position:absolute;bottom:0;font:700 36px Inter,sans-serif;color:#141414}
    #s09-l0{left:0}
    #s09-l1{left:300px}
""", f"""{P}
    <div id="s09-m"><div class="lg">Thai Union: “meritless”</div></div>
    <div id="s09-k" class="kick">Guests since 2019</div>
    <div id="s09-n" class="lg red">−30%</div>
    <div id="s09-c"><div id="s09-b0"></div><div id="s09-b1"></div><div id="s09-l0">2019</div><div id="s09-l1">2024</div></div>
    <div class="src">Source: CEO Jonathan Tibus, court declaration, May 2024 (via Dallas Morning News)</div>
""", """
    tl.fromTo('#s09-m', { opacity: 1, scale: 1.35 }, { scale: 1, duration: 0.12, ease: 'power4.out' }, W(1.36));
    shake('#s09-m', W(1.36) + 0.12);
    show('#s09-k', W(3.20));
    tl.fromTo('#s09-b0', { scaleY: 0 }, { scaleY: 1, duration: 0.4, ease: 'power3.out' }, W(3.20));
    tl.fromTo('#s09-b1', { scaleY: 0 }, { scaleY: 1, duration: 0.4, ease: 'power3.out' }, W(3.40));
    tl.fromTo('#s09-b1', { scaleY: 1, backgroundColor: '#141414' }, { scaleY: 0.7, backgroundColor: '#D7261E', duration: 0.6, ease: 'power2.inOut', immediateRender: false }, W(5.04));
    show('#s09-n', W(5.04));
""")

# s10: 99 closed, then Chapter 11
scene("s10", 8.4, """
    #s10-photo{left:-96px;top:-54px}
    #s10-k{position:absolute;left:192px;top:140px;opacity:0}
    #s10-n{position:absolute;left:176px;top:210px;font-size:540px;opacity:0}
    #s10-l{position:absolute;left:192px;top:720px;font-size:150px;opacity:0}
    #s10-wrap{position:absolute;left:0;top:0;width:1920px;height:1080px}
    #s10-st{position:absolute;left:1000px;top:360px;padding:30px 46px 6px;border:12px solid #D7261E;opacity:0}
    #s10-st .lg{font-size:200px;color:#D7261E}
    #s10-c{opacity:.8}
""", f"""
    <img id="s10-photo" class="photo" src="assets/photos/dining.jpg" alt="Red Lobster dining room">
    <div id="s10-k" class="kick np">May 2024</div>
    <div id="s10-n" class="lg np">99</div>
    <div id="s10-l" class="lg np">restaurants closed</div>
    <div id="s10-wrap"><div id="s10-st"><div class="lg">Chapter 11</div></div></div>
    <div id="s10-c" class="src np">Sources: CoStar; Dallas Morning News · {CC}</div>
""", """
    tl.fromTo('#s10-photo', { scale: 1 }, { scale: 1.06, duration: 8.4, ease: 'none' }, 0);
    show('#s10-k', W(0.16));
    show('#s10-n', W(1.60));
    wipe('#s10-l', W(2.32), 0.3);
    tl.fromTo('#s10-st', { opacity: 1, scale: 1.35, rotation: -7 }, { scale: 1, rotation: -7, duration: 0.12, ease: 'power4.out' }, W(7.04));
    shake('#s10-wrap', W(7.04) + 0.12);
""")

# s11: the one line
scene("s11", 5.9, """
    #s11-a{position:absolute;left:192px;top:130px;font-size:130px;opacity:0}
    #s11-b{position:absolute;left:186px;top:320px;font-size:190px;opacity:0}
    #s11-c{position:absolute;left:186px;top:680px;font-size:240px;opacity:0}
""", f"""{P}
    <div id="s11-a" class="lg">Endless shrimp got the headlines</div>
    <div id="s11-b" class="lg">A 10-year-old<br>real estate deal</div>
    <div id="s11-c" class="lg red">did the damage</div>
""", """
    wipe('#s11-a', W(0.0), 0.35);
    tl.fromTo('#s11-a', { color: '#141414' }, { color: '#6B6963', duration: 0.01 }, W(2.24));
    wipe('#s11-b', W(2.48), 0.35);
    show('#s11-c', W(4.48));
""")

# s12: end card
scene("s12", 4.2, """
    #s12-w{position:absolute;left:0;top:230px;width:1920px;text-align:center;font-size:420px}
    #s12-w span{opacity:0}
    #s12-r{left:560px;top:640px;width:800px}
    #s12-t{position:absolute;left:0;top:690px;width:1920px;text-align:center;opacity:0}
""", f"""{P}
    <div id="s12-w" class="lg"><span id="s12-red" class="red">Red</span> <span id="s12-ink">Ink</span></div>
    <div id="s12-r" class="rule"></div>
    <div id="s12-t" class="kick">How big companies fall</div>
""", """
    show('#s12-red', 0.25);
    show('#s12-ink', 0.55);
    rule('#s12-r', 0.85, 0.5);
    show('#s12-t', 1.3);
""")
print("scenes written")
