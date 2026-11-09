"""Fast Wikimedia Commons fetcher: standard cached thumbnail width (1920), 4 parallel downloads.
usage: fetch_commons.py out_dir "File:Title 1.jpg" "File:Title 2.jpg" ...   (prints ok/fail per file)"""
import sys, json, os, urllib.request, urllib.parse, concurrent.futures as cf, time
UA = {'User-Agent': 'PaperEmpireResearch/0.2 (documentary sourcing)'}
out, titles = sys.argv[1], sys.argv[2:]
os.makedirs(out, exist_ok=True)
def info(batch):   # one API call for up to 50 titles
    q = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(dict(action='query', titles='|'.join(batch), prop='imageinfo', iiprop='url|size', iiurlwidth=1920, format='json'))
    pages = json.load(urllib.request.urlopen(urllib.request.Request(q, headers=UA), timeout=30))['query']['pages'].values()
    return {p['title']: p['imageinfo'][0] for p in pages if 'imageinfo' in p}
meta = {}
for k in range(0, len(titles), 50): meta.update(info(titles[k:k + 50]))
def get(title):
    ii = meta.get(title)
    if not ii: return title, 'no info'
    url = ii['thumburl'] if ii['width'] > 1920 else None
    if url is None:   # small original: ask for the largest standard cached width below it (originals are throttled)
        w = max([x for x in (330, 500, 960, 1280) if x < ii['width']] or [330])
        q = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(dict(action='query', titles=title, prop='imageinfo', iiprop='url', iiurlwidth=w, format='json'))
        url = list(json.load(urllib.request.urlopen(urllib.request.Request(q, headers=UA), timeout=30))['query']['pages'].values())[0]['imageinfo'][0]['thumburl']
    dest = os.path.join(out, title[5:].replace(' ', '_'))
    for a in range(3):
        try:
            data = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
            open(dest, 'wb').write(data); return title, f'ok {len(data)//1024}KB'
        except Exception as e: time.sleep(5 * (a + 1)); err = e
    return title, f'fail {err}'
with cf.ThreadPoolExecutor(4) as ex:
    for t, r in ex.map(get, titles): print(r, '|', t)
