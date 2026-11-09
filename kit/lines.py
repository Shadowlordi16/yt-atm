"""Stage 3a: SCRIPT.md -> lines.txt (one voice line per '> ' line, source tags removed).
usage (in the video folder): python3 ../kit/lines.py"""
import re
s = open("SCRIPT.md").read()
lines = [re.sub(r"\s+", " ", re.sub(r"\s*\[S[\w\]\[S]*\]", "", l[2:])).strip() for l in s.splitlines() if l.startswith("> ")]
open("lines.txt", "w").write("\n".join(f"L{i:02d}|{l}" for i, l in enumerate(lines)) + "\n")
w = sum(len(l.split()) for l in lines)
print(f"{len(lines)} lines, {w} words, about {w / 1126 * 8.19:.1f} min")
if w < 1100: print("WARNING: under ~1,100 words the video will be under 8:00 (no mid-roll ads).")
