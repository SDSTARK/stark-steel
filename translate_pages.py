# -*- coding: utf-8 -*-
"""Translate the 90 page-content keys into 15 languages and merge into i18n.js (all 16 blocks)."""
import json, os, re, time, urllib.request, urllib.parse, urllib.error

ROOT = r"C:/Users/Administrator/WorkBuddy/2026-08-12-16-19-26"
I18N = os.path.join(ROOT, "stark-steel-fresh", "js", "i18n.js")
KEYS = os.path.join(ROOT, "stark-steel-fresh", ".cache_pages_keys.json")
LANGS = ['zh', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'ar', 'ja', 'ko', 'vi', 'th', 'tr', 'id', 'hi']

EN = json.load(open(KEYS, encoding='utf-8'))

def fetch(url, headers=None, timeout=15):
    req = urllib.request.Request(url, headers=headers or {'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode('utf-8', 'replace')
    except urllib.error.HTTPError as e:
        try: return e.code, e.read().decode('utf-8', 'replace')[:300]
        except Exception: return e.code, ''
    except Exception as e:
        return 0, str(e)[:200]

def google(text, tl):
    q = urllib.parse.quote(text)
    url = 'https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=en&tl=%s&q=%s' % (tl, q)
    st, body = fetch(url)
    if st == 200:
        try:
            arr = json.loads(body)
            if arr and arr[0]:
                return arr[0].replace('\ufeff', '').strip()
        except Exception: pass
    return None

def mymemory(text, tl):
    q = urllib.parse.quote(text)
    url = 'https://api.mymemory.translated.net/get?q=%s&langpair=en|%s' % (q, tl)
    st, body = fetch(url)
    if st == 200:
        try:
            t = json.loads(body).get('responseData', {}).get('translatedText')
            if t and t.strip(): return t.strip()
        except Exception: pass
    return None

def translate(text, tl):
    for _ in range(3):
        r = google(text, tl)
        if r and r.strip(): return r.strip()
        time.sleep(1.2)
    for _ in range(2):
        r = mymemory(text, tl)
        if r and r.strip(): return r.strip()
        time.sleep(1.5)
    return None

trans = {lg: {} for lg in LANGS}
fails = []
total = len(EN)
for li, lg in enumerate(LANGS):
    for ki, (k, en) in enumerate(EN.items()):
        v = translate(en, lg)
        if v: trans[lg][k] = v
        else:
            fails.append((lg, k)); trans[lg][k] = en
        time.sleep(0.25)
    print('[%d/%d] %-3s done  fails=%d' % (li+1, len(LANGS), lg, sum(1 for f in fails if f[0]==lg)))

# Merge
js = open(I18N, encoding='utf-8').read()
all_langs = ['en'] + LANGS
for lg in all_langs:
    src = EN if lg == 'en' else trans[lg]
    m = re.search(r'\n    ' + lg + r': \{', js)
    if not m:
        print('BLOCK NOT FOUND for', lg); continue
    insert_pos = m.end()
    lines = []
    for k, v in src.items():
        if re.search(r'\n      ' + re.escape(k) + r'\s*:', js):
            continue
        lines.append('      "%s": %s,\n' % (k, json.dumps(v, ensure_ascii=False)))
    if lines:
        js = js[:insert_pos] + '\n' + ''.join(lines) + js[insert_pos:]
open(I18N, 'w', encoding='utf-8').write(js)
print('\nMerged %d keys into all 16 blocks.' % len(EN))
print('Total translation failures (fell back to EN):', len(fails))
if fails:
    print('Failed:', fails[:20])
