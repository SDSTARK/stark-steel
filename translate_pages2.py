# -*- coding: utf-8 -*-
"""Robust translator for the 80 missing page-content keys.
- Incremental per-language cache (recoverable on interruption)
- 429 exponential backoff
- Idempotent: skips keys already present in i18n.js and already-cached translations
"""
import json, os, re, time, urllib.request, urllib.parse, urllib.error

ROOT = r"C:/Users/Administrator/WorkBuddy/2026-08-12-16-19-26"
I18N = os.path.join(ROOT, "stark-steel-fresh", "js", "i18n.js")
KEYS = os.path.join(ROOT, "stark-steel-fresh", ".cache_pages_keys.json")
CACHE = os.path.join(ROOT, "stark-steel-fresh", ".cache_pages_trans")
LANGS = ['zh', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'ar', 'ja', 'ko', 'vi', 'th', 'tr', 'id', 'hi']

EN = json.load(open(KEYS, encoding='utf-8'))
js_txt = open(I18N, encoding='utf-8').read()

def present(k):
    return bool(re.search(r'\n      ' + re.escape(k) + r'\s*:', js_txt))

# only translate keys missing from i18n.js
MISSING = [k for k in EN if not present(k)]
print('total collected:', len(EN), '| already in i18n.js:', len(EN) - len(MISSING), '| to translate:', len(MISSING))

os.makedirs(CACHE, exist_ok=True)

def fetch(url, headers=None, timeout=20, tries=1):
    req = urllib.request.Request(url, headers=headers or {'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode('utf-8', 'replace')
    except urllib.error.HTTPError as e:
        return e.code, (e.read().decode('utf-8', 'replace')[:300] if e.fp else '')
    except Exception as e:
        return 0, str(e)[:200]

def google(text, tl):
    q = urllib.parse.quote(text)
    url = 'https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=en&tl=%s&q=%s' % (tl, q)
    st, body = fetch(url)
    if st == 429:
        return 'RATE'
    if st == 200:
        try:
            arr = json.loads(body)
            if arr and arr[0]:
                return arr[0].replace('\ufeff', '').strip()
        except Exception:
            pass
    return None

def mymemory(text, tl):
    q = urllib.parse.quote(text)
    url = 'https://api.mymemory.translated.net/get?q=%s&langpair=en|%s' % (q, tl)
    st, body = fetch(url)
    if st == 429:
        return 'RATE'
    if st == 200:
        try:
            t = json.loads(body).get('responseData', {}).get('translatedText')
            if t and t.strip():
                return t.strip()
        except Exception:
            pass
    return None

def translate(text, tl):
    backoff = 2
    for _ in range(6):
        r = google(text, tl)
        if r == 'RATE':
            time.sleep(backoff); backoff = min(backoff * 2, 30); continue
        if r and r.strip():
            return r.strip()
        time.sleep(0.6)
        r = mymemory(text, tl)
        if r == 'RATE':
            time.sleep(backoff); backoff = min(backoff * 2, 30); continue
        if r and r.strip():
            return r.strip()
        time.sleep(1)
    return None

for li, lg in enumerate(LANGS):
    cache_file = os.path.join(CACHE, lg + '.json')
    trans = json.load(open(cache_file, encoding='utf-8')) if os.path.exists(cache_file) else {}
    done = 0
    for k in MISSING:
        if k in trans and trans[k]:
            done += 1
            continue
        v = translate(EN[k], lg)
        if v:
            trans[k] = v
            done += 1
        else:
            trans[k] = EN[k]  # fallback to EN
        time.sleep(0.35)
    json.dump(trans, open(cache_file, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    missing_now = sum(1 for k in MISSING if trans.get(k) == EN[k] and k in trans)
    print('[%d/%d] %-3s cached %d/%d (fallback-to-EN: %d)' % (li+1, len(LANGS), lg, done, len(MISSING), missing_now))

print('TRANSLATION DONE')
