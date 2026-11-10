# Black-and-white press treatment for every photo (MOTION.md §5), baked with ffmpeg.
import json, os, subprocess, glob
RAW = "../raw"
names = {"stores": "st", "bend": "bd", "closed": "cl", "vhs": "vhs", "netflix": "nfenv", "hastings": "hast", "icahn": "icahn",
         "antioco": "antioco", "viacom": "viacom", "dish": "dish", "dallasdt": "dallas", "nflogo": "nflogo", "bblogo": "bbcard", "seven": "seven"}
single = {"netflix", "icahn", "antioco", "viacom", "dish", "dallasdt", "nflogo", "bblogo", "seven"}
for f in sorted(glob.glob(f"{RAW}/*.*")):
    b = os.path.basename(f)
    if b.endswith(".json"): continue
    slug, idx = b.rsplit(".", 1)[0].rsplit("_", 1)
    out = names[slug] + ("" if slug in single else idx)
    if slug == "nflogo":   # the logo stays a flat mark, in ink
        subprocess.run(["magick", f, "-colorspace", "gray", "-fuzz", "12%", "-fill", "none", "-draw", "color 0,0 floodfill", f"assets/img/{out}.png"]); continue
    vf = ("scale=2304:1296:force_original_aspect_ratio=increase,crop=2304:1296,hue=s=0,"
          "eq=contrast=1.25:brightness=-0.02,vignette=PI/5,noise=alls=6:allf=t")
    if slug in ("antioco", "icahn", "hastings"):   # portraits keep their aspect, just big enough
        vf = "scale=1600:-2,hue=s=0,eq=contrast=1.2,vignette=PI/6,noise=alls=5:allf=t"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f, "-vf", vf, "-q:v", "3", f"assets/img/{out}.jpg"])
print(len(os.listdir("assets/img")), "treated")
