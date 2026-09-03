# -*- coding: utf-8 -*-
"""Re-translate only the (lang,key) pairs that fell back to EN in the cache."""
import json, os, re, time, urllib.request, urllib.parse, urllib.error

ROOT = r"C:/Users/Administrator/WorkBuddy/2026-08-12-16-19-26"
CACHE = os.path.join(ROOT, "stark-steel-fresh", ".cache_pages_trans")
KEYS = os.path.join(ROOT, "stark-steel-fresh", ".cache_pages_keys.json")
LANGS = ['zh', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'ar', 'ja', 'ko', 'vi', 'th', 'tr', 'id', 'hi']
EN = json.load(open(KEYS, encoding='utf-8'))

def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode('utf-8', 'replace')
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8', 'replace')[:200] if e.fp else ''
    except Exception as e:
        return 0, str(e)[:120]

def google(text, tl):
    q = urllib.parse.quote(text)
    url = 'https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=en&tl=%s&q=%s' % (tl, q)
    st, body = fetch(url)
    if st == 429: return 'RATE'
    if st == 200:
        try:
            arr = json.loads(body)
            if arr and arr[0]: return arr[0].replace('\ufeff', '').strip()
        except Exception: pass
    return None

def mymemory(text, tl):
    q = urllib.parse.quote(text)
    url = 'https://api.mymemory.translated.net/get?q=%s&langpair=en|%s' % (q, tl)
    st, body = fetch(url)
    if st == 429: return 'RATE'
    if st == 200:
        try:
            t = json.loads(body).get('responseData', {}).get('translatedText')
            if t and t.strip(): return t.strip()
        except Exception: pass
    return None

def translate(text, tl):
    backoff = 3
    for _ in range(8):
        r = google(text, tl)
        if r == 'RATE': time.sleep(backoff); backoff = min(backoff*2, 30); continue
        if r and r.strip(): return r
        time.sleep(0.8)
        r = mymemory(text, tl)
        if r == 'RATE': time.sleep(backoff); backoff = min(backoff*2, 30); continue
        if r and r.strip(): return r
        time.sleep(1)
    return None

total_retried = 0
total_fixed = 0
for lg in LANGS:
    cf = os.path.join(CACHE, lg + '.json')
    if not os.path.exists(cf): continue
    d = json.load(open(cf, encoding='utf-8'))
    for k, v in list(d.items()):
        if v == EN[k]:  # fallback
            total_retried += 1
            nv = translate(EN[k], lg)
            if nv and nv != EN[k]:
                d[k] = nv
                total_fixed += 1
                print('FIXED', lg, k, '->', nv[:40])
            time.sleep(0.5)
    json.dump(d, open(cf, 'w', encoding='utf-8'), ensure_ascii=False)

print('\nretried:', total_retried, '| fixed:', total_fixed, '| remaining fallback:', total_retried - total_fixed)
