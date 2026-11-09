"""Paper Empire scene kit for HyperFrames (look: ../MOTION.md).

A Scene is one sub-composition. Devices add markup + CSS + timeline code to it.
Times are scene-local seconds. Sound cues are collected per scene (scene-local) and
placed on the root timeline by the builder.
"""
import json, os, html as H

INK, PAPER, RED, GREY, SHADE = "#141414", "#E9E6DF", "#D7261E", "#6B6963", "#C9C5BB"
FPS = 30
F = 1 / FPS

BASE_CSS = """
#root{position:absolute;inset:0;overflow:hidden;background:#E9E6DF;font-family:Inter,sans-serif;color:#141414}
#root .fill{position:absolute;left:0;top:0;width:1920px;height:1080px}
#root .paper{position:absolute;left:0;top:0;width:1920px;height:1080px;object-fit:cover}
#root .ph{position:absolute;left:0;top:0;width:1920px;height:1080px;object-fit:cover;opacity:0}
#root .lg{font-family:'League Gothic',sans-serif;text-transform:uppercase;line-height:.88;font-weight:400;font-variant-numeric:tabular-nums;white-space:nowrap}
#root .kick{font-family:Inter,sans-serif;font-weight:900;font-size:46px;letter-spacing:.02em;text-transform:uppercase;white-space:nowrap}
#root .body{font-family:Inter,sans-serif;font-weight:700;font-size:46px;white-space:nowrap}
#root .src{position:absolute;left:192px;bottom:72px;font:400 28px Inter,sans-serif;color:#6B6963;white-space:nowrap}
#root .src.np{color:#E9E6DF;text-shadow:0 2px 6px rgba(0,0,0,.9),0 0 18px rgba(0,0,0,.75)}
#root .red{color:#D7261E}#root .grey{color:#6B6963}#root .np{color:#E9E6DF}#root .ink{color:#141414}
#root .rule{position:absolute;height:8px;background:#141414;transform-origin:left center}
#root .sheet{position:absolute;overflow:hidden;background:#E9E6DF;box-shadow:0 18px 40px rgba(0,0,0,.35)}
#root .band{position:absolute;background:#141414;padding:26px 40px 8px}
#root .o0{opacity:0}
#root .stamp{position:absolute;padding:26px 44px 6px;border:12px solid #D7261E;color:#D7261E;opacity:0}
#root .stamp.inkst{border-color:#141414;color:#141414}
#root .card{position:absolute;background:#F7F5F0;box-shadow:0 14px 30px rgba(0,0,0,.2);opacity:0}
#root .flash{position:absolute;left:0;top:0;width:1920px;height:1080px;background:#F7F5F0;opacity:0}
"""

JS_HEAD = """
    const tl = gsap.timeline({ paused: true });
    const on = (s, t) => tl.fromTo(s, { opacity: 0 }, { opacity: 1, duration: 0.001 }, t);
    const off = (s, t) => tl.fromTo(s, { opacity: 1 }, { opacity: 0, duration: 0.001, immediateRender: false }, t);
    const wipe = (s, t, d = 0.28) => { tl.fromTo(s, { opacity: 0 }, { opacity: 1, duration: 0.001 }, t);
      if (document.querySelector(s + ' > .wi')) tl.fromTo(s + ' > .wi', { xPercent: -102 }, { xPercent: 0, duration: d, ease: 'power3.out' }, t); };
    const rule = (s, t, d = 0.45) => tl.fromTo(s, { scaleX: 0 }, { scaleX: 1, duration: d, ease: 'power2.inOut' }, t);
    const push = (s, t, d, a = 1, b = 1.06) => tl.fromTo(s, { scale: a }, { scale: b, duration: d, ease: 'none' }, t);
    const slam = (s, t) => { tl.fromTo(s, { opacity: 1, scale: 1.35 }, { scale: 1, duration: 0.12, ease: 'power4.out' }, t); };
    const shake = (s, t) => tl.fromTo(s, { x: 0 }, { keyframes: [{ x: 7, duration: .033 }, { x: -6, duration: .033 }, { x: 3, duration: .033 }, { x: 0, duration: .033 }] }, t);
    const count = (s, t, to, fmt, d = 1.4) => { const el = document.querySelector(s); const o = { v: 0 };
      tl.fromTo(s, { opacity: 0 }, { opacity: 1, duration: 0.001 }, t);
      tl.fromTo(o, { v: 0 }, { v: to, duration: d, ease: 'power2.out', onUpdate: () => { el.textContent = fmt(o.v); } }, t); };
    const fmtInt = v => Math.round(v).toLocaleString('en-US');
"""


class Scene:
    def __init__(self, sid, dur, ground="paper"):
        self.sid, self.dur = sid, round(dur, 3)
        self.css, self.html, self.js, self.sfx = [], [], [], []
        self.n = 0
        if ground == "paper":
            self.html.append('<img class="paper" src="assets/paper.jpg" alt="">')
        elif ground == "ink":
            self.html.append('<div class="fill" style="background:#141414"></div>')

    # ---------- basics ----------
    def i(self, name=None):
        self.n += 1
        return f"{self.sid}-{name or 'e'}{self.n}"

    def el(self, inner, style, cls="", t=None, mode="on", d=0.28, parent=None, eid=None):
        eid = eid or self.i()
        if mode != "on":   # wipe: text slides out from behind its own left edge (fast-capture friendly)
            inner = f'<span class="wi" style="display:inline-block">{inner}</span>'
            style = style + ";overflow:hidden;padding-bottom:.12em"
        markup = f'<div id="{eid}" class="{cls} o0" style="position:absolute;{style}">{inner}</div>'
        (parent.append(markup) if isinstance(parent, list) else self.html.append(markup))
        if t is not None:
            if mode == "on":
                self.js.append(f"on('#{eid}', {t:.3f});")
            else:
                self.js.append(f"wipe('#{eid}', {t:.3f}, {d});")
        return eid

    def text(self, s, x, y, size, cls="lg", color="", t=0.2, mode="wipe", extra="", **kw):
        st = f"left:{x}px;top:{y}px;font-size:{size}px;{extra}"
        return self.el(H.escape(s).replace("\n", "<br>"), st, f"{cls} {color}", t, mode, **kw)

    def kicker(self, s, x=192, y=150, t=0.2, color=""):
        return self.el(H.escape(s), f"left:{x}px;top:{y}px", f"kick {color}", t, "on")

    def first(self, beats):
        """Opening beat(s) so a scene is never a bare photo: beats = [(text, x, y, size, color), ...]
        Each lands in the first half-second, before the voice names anything."""
        for k, (txt, x, y, size, col) in enumerate(beats):
            self.text(txt, x, y, size, color=col, t=0.06 + 0.10 * k)

    def source(self, s, light=False):
        self.html.append(f'<div class="src{" np" if light else ""}">{H.escape(s)}</div>')

    def click(self, t, kind="click", vol=0.32):
        self.sfx.append((kind, round(t, 3), vol))

    def flash(self, t):
        eid = self.i("fl")
        self.html.append(f'<div id="{eid}" class="flash"></div>')
        self.js.append(f"on('#{eid}', {t:.3f}); off('#{eid}', {t + F:.3f});")

    # ---------- photos ----------
    def photos(self, items, end=None, rate=0.05, clicks=True):
        """items: [(img, t, pos)] full-bleed cuts. Each pushes ~rate scale/s for its window."""
        end = self.dur if end is None else end
        for k, it in enumerate(items):
            img, t = it[0], it[1]
            pos = it[2] if len(it) > 2 else "50% 50%"
            t2 = items[k + 1][1] if k + 1 < len(items) else end
            eid = self.i("ph")
            self.html.append(f'<img id="{eid}" class="ph" src="assets/img/{img}.jpg" style="object-position:{pos};transform-origin:{pos}" alt="">')
            self.js.append(f"on('#{eid}', {t:.3f}); push('#{eid}', {t:.3f}, {t2 - t:.3f}, 1, {1 + rate * (t2 - t):.4f});")
            if k + 1 < len(items):
                self.js.append(f"off('#{eid}', {t2:.3f});")
            if clicks and t > 0.01:
                self.click(t)

    def tiles(self, imgs, t0, hold_last=True, step=2):
        """3x3 tile-flash reveal: one pane per `step` frames, white 1 frame then the picture, a click each."""
        cell_w, cell_h = 640, 360
        order = [4, 0, 8, 2, 6, 1, 7, 3, 5]
        for k, cell in enumerate(order[:len(imgs)]):
            cx, cy = (cell % 3) * cell_w, (cell // 3) * cell_h
            t = t0 + k * step * F
            wid, pid = self.i("tw"), self.i("tp")
            self.html.append(
                f'<div id="{pid}" class="o0" style="position:absolute;left:{cx}px;top:{cy}px;width:{cell_w}px;height:{cell_h}px;overflow:hidden">'
                f'<img src="assets/img/{imgs[k]}.jpg" style="width:100%;height:100%;object-fit:cover" alt=""></div>'
                f'<div id="{wid}" class="o0" style="position:absolute;left:{cx}px;top:{cy}px;width:{cell_w}px;height:{cell_h}px;background:#F7F5F0"></div>')
            self.js.append(f"on('#{pid}', {t + F:.3f}); on('#{wid}', {t:.3f}); off('#{wid}', {t + F:.3f});")
            self.click(t, vol=0.16)
        lines = '<div class="fill" style="background:linear-gradient(#141414,#141414) 640px 0/6px 1080px no-repeat,linear-gradient(#141414,#141414) 1277px 0/6px 1080px no-repeat,linear-gradient(#141414,#141414) 0 357px/1920px 6px no-repeat,linear-gradient(#141414,#141414) 0 717px/1920px 6px no-repeat"></div>'
        self.html.append(lines)
        return t0 + len(imgs) * step * F

    # ---------- print devices ----------
    def sheet(self, x, y, w, h, t, frm="right"):
        eid = self.i("sh")
        self.html.append(f'<div id="{eid}" class="sheet" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><img class="paper" src="assets/paper.jpg" alt="" style="width:{w}px;height:{h}px"><div class="sheetin"></div></div>')
        prop = "xPercent: 110" if frm == "right" else ("xPercent: -110" if frm == "left" else "yPercent: 130")
        zero = prop.split(":")[0] + ": 0"
        self.js.append(f"tl.fromTo('#{eid}', {{ {prop} }}, {{ {zero}, duration: 0.5, ease: 'expo.out' }}, {t:.3f});")
        return eid

    def in_sheet(self, sheet_id, s, x, y, size, cls="lg", color="", t=0.0, mode="wipe"):
        """Text inside a sheet: absolute coords relative to the sheet."""
        eid = self.i()
        inner = H.escape(s).replace("\n", "<br>")
        if mode == "wipe": inner = f'<span class="wi" style="display:inline-block">{inner}</span>'
        span = f'<div id="{eid}" class="{cls} {color} o0" style="position:absolute;left:{x}px;top:{y}px;font-size:{size}px;overflow:hidden;padding-bottom:.12em">{inner}</div>'
        self.html[-1] = self.html[-1] if False else self.html[-1]
        # insert into the sheet markup
        for k in range(len(self.html) - 1, -1, -1):
            if f'id="{sheet_id}"' in self.html[k]:
                self.html[k] = self.html[k].replace('<div class="sheetin"></div>', span + '<div class="sheetin"></div>')
                break
        self.js.append(f"{'wipe' if mode == 'wipe' else 'on'}('#{eid}', {t:.3f}{', 0.28' if mode == 'wipe' else ''});")
        return eid

    def stamp(self, s, x, y, size, t, rot=-6, ink=False, sound=True):
        eid = self.i("st")
        self.html.append(f'<div id="{eid}" class="stamp{" inkst" if ink else ""}"style="left:{x}px;top:{y}px"><div class="lg" style="font-size:{size}px">{H.escape(s)}</div></div>'.replace('"style', '" style'))
        self.js.append(f"tl.fromTo('#{eid}', {{ opacity: 1, scale: 1.35, rotation: {rot} }}, {{ scale: 1, rotation: {rot}, duration: 0.12, ease: 'power4.out' }}, {t:.3f}); shake('#{eid}', {t + 0.12:.3f});")
        if sound:
            self.sfx.append(("impact", round(t, 3), 0.5))
        return eid

    def strike(self, x, y, w, t, h=20):
        eid = self.i("x")
        self.html.append(f'<div id="{eid}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:#D7261E;transform-origin:left center;transform:scaleX(0)"></div>')
        self.js.append(f"rule('#{eid}', {t:.3f}, 0.4);")
        return eid

    def hrule(self, x, y, w, t, h=8, color=INK):
        eid = self.i("r")
        self.html.append(f'<div id="{eid}" class="rule" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{color};transform:scaleX(0)"></div>')
        self.js.append(f"rule('#{eid}', {t:.3f});")
        return eid

    def count(self, x, y, size, t, to, fmt_js, color="", d=1.4, start_text="0"):
        eid = self.i("n")
        self.html.append(f'<div id="{eid}" class="lg {color} o0" style="position:absolute;left:{x}px;top:{y}px;font-size:{size}px">{H.escape(start_text)}</div>')
        self.js.append(f"count('#{eid}', {t:.3f}, {to}, {fmt_js}, {d});")
        self.click(t + d - 0.05, "pop", 0.3)
        return eid

    def dots(self, x, y, cols, rows, cell, t, color=INK, d=0.8, total=None, shape="dot"):
        """A grid of cols*rows marks drawn with a CSS pattern, revealed row by row (wipe down).
        If total is given, the last row is cut so exactly `total` marks show."""
        eid = self.i("dg")
        if shape == "sq":   # real DOM squares (small counts), revealed one by one
            n = total or cols * rows
            sq = "".join(f'<div class="{eid}-c" style="position:absolute;left:{(k % cols) * cell}px;top:{(k // cols) * cell}px;width:{cell * 0.72:.1f}px;height:{cell * 0.72:.1f}px;background:{color};opacity:0"></div>' for k in range(n))
            self.html.append(f'<div id="{eid}" style="position:absolute;left:{x}px;top:{y}px;width:{cols * cell}px;height:{rows * cell}px">{sq}</div>')
            self.js.append(f"tl.fromTo('#root .{eid}-c', {{ opacity: 0 }}, {{ opacity: 1, duration: 0.001, stagger: {d / max(n, 1):.5f} }}, {t:.3f});")
            return eid
        r = cell * 0.36
        if shape == "dot":
            bg = f"radial-gradient(circle at 50% 50%, {color} {r}px, transparent {r + 0.8}px)"
        else:
            bg = f"linear-gradient({color},{color}) 50% 50%/{cell*0.66}px {cell*0.66}px no-repeat"
        w, h = cols * cell, rows * cell
        full_rows, rem = (divmod(total, cols) if total else (rows, 0))
        clip = f"polygon(0 0,{w}px 0,{w}px {full_rows*cell}px,{rem*cell}px {full_rows*cell}px,{rem*cell}px {(full_rows+1)*cell}px,0 {(full_rows+1)*cell}px)" if total else "none"
        self.html.append(f'<div id="{eid}" class="o0" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};background-size:{cell}px {cell}px;clip-path:{clip}"></div>'
                         f'<div id="{eid}c" class="o0" style="position:absolute;left:{x - 2}px;top:{y - 2}px;width:{w + 4}px;height:{h + 4}px;background:#E9E6DF;transform-origin:50% 100%"></div>')
        self.js.append(f"tl.fromTo('#{eid}', {{ opacity: 0 }}, {{ opacity: 1, duration: 0.001 }}, {t:.3f}); tl.fromTo('#{eid}c', {{ opacity: 1, scaleY: 1 }}, {{ scaleY: 0, duration: {d}, ease: 'power1.inOut' }}, {t:.3f});")
        return eid

    def quote(self, x, y, w, h, label, quote, attrib, t, qsize=96):
        eid = self.i("q")
        self.html.append(
            f'<div id="{eid}" class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
            f'<div style="position:absolute;left:52px;top:46px;font:900 28px Inter;letter-spacing:.04em;color:#6B6963">{H.escape(label)}</div>'
            f'<div class="lg" style="position:absolute;left:52px;top:104px;width:{w-104}px;white-space:normal;font-size:{qsize}px;line-height:.94">{H.escape(quote)}</div>'
            f'<div style="position:absolute;left:52px;bottom:44px;width:{w-104}px;font:400 30px Inter;line-height:1.3">{H.escape(attrib)}</div></div>')
        self.js.append(f"tl.fromTo('#{eid}', {{ opacity: 1, y: 60, rotation: -2.2 }}, {{ y: 0, rotation: -1.1, duration: 0.45, ease: 'expo.out' }}, {t:.3f});")
        return eid

    def raw(self, html, css="", js=""):
        self.html.append(html)
        if css: self.css.append(css)
        if js: self.js.append(js)

    # ---------- output ----------
    def write(self, outdir):
        doc = ("<template>\n  <style>" + BASE_CSS + "\n".join(self.css) + "</style>\n"
               f'  <div id="root" data-composition-id="{self.sid}" data-width="1920" data-height="1080">\n    '
               + "\n    ".join(self.html) +
               "\n  </div>\n  <script>\n    (function () {" + JS_HEAD + "\n    " + "\n    ".join(self.js) +
               f"\n    tl.to({{}}, {{ duration: {self.dur} }}, 0);\n    window.__timelines[\"{self.sid}\"] = tl;\n    }})();\n  </script>\n</template>\n")
        open(os.path.join(outdir, f"{self.sid}.html"), "w").write(doc)


CROWN_SVG = """<svg viewBox="0 0 200 200" width="{s}" height="{s}"><circle cx="100" cy="100" r="100" fill="#141414"/>
<polygon class="cf" points="38,138 38,72 70,104 70,138" fill="#E9E6DF"/><polygon class="cf" points="70,138 70,104 100,52 100,138" fill="#C9C5BB"/>
<polygon class="cf" points="100,138 100,52 130,104 130,138" fill="#E9E6DF"/><polygon class="cf" points="130,138 130,104 162,72 162,138" fill="#C9C5BB"/>
<polygon class="cr" points="162,72 146,88 162,100" fill="#D7261E"/><rect class="cb" x="38" y="137.5" width="124" height="16.5" fill="#E9E6DF"/></svg>"""
