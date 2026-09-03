# -*- coding: utf-8 -*-
"""Retry translation for any keys still missing/empty after translate_all."""
import json, os, time, urllib.request, urllib.parse, urllib.error

ROOT = r"C:/Users/Administrator/WorkBuddy/2026-08-12-16-19-26"
OUT_DIR = os.path.join(ROOT, "translations")
KEYS = os.path.join(ROOT, "stark-steel-fresh", ".cache", "table_keys_all.json")
LOG = os.path.join(ROOT, "stark-steel-fresh", "retry_all_log.txt")
LANGS = ['zh', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'ar', 'ja', 'ko',
         'vi', 'th', 'tr', 'id', 'hi']


def log(m):
    line = time.strftime('%H:%M:%S ') + m
    print(line, flush=True)
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write(line + '\n')


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode('utf-8', 'replace')
    except Exception as e:
        return 0, str(e)[:200]


def gtrans(text, tl):
    q = urllib.parse.quote(text)
    url = 'https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=en&tl=%s&q=%s' % (tl, q)
    st, b = fetch(url)
    if st == 200:
        try:
            a = json.loads(b)
            if a and a[0]:
                return a[0].replace('\ufeff', '').strip()
        except Exception:
            pass
    return None


def mymem(text, tl):
    q = urllib.parse.quote(text)
    url = 'https://api.mymemory.translated.net/get?q=%s&langpair=en|%s' % (q, tl)
    st, b = fetch(url)
    if st == 200:
        try:
            t = json.loads(b).get('responseData', {}).get('translatedText')
            if t and t.strip():
                return t.strip()
        except Exception:
            pass
    return None


def trans(text, tl):
    for _ in range(5):
        r = gtrans(text, tl)
        if r and r.strip():
            return r.strip()
        time.sleep(2)
    for _ in range(3):
        r = mymem(text, tl)
        if r and r.strip():
            return r.strip()
        time.sleep(2)
    return None


def main():
    keys = json.load(open(KEYS, encoding='utf-8'))
    total = 0
    for lg in LANGS:
        f = os.path.join(OUT_DIR, 'table_%s.json' % lg)
        d = json.load(open(f, encoding='utf-8')) if os.path.exists(f) else {}
        miss = [k for k in keys if not str(d.get(k, '')).strip()]
        if not miss:
            log('%-3s complete' % lg)
            continue
        log('%-3s retrying %d missing...' % (lg, len(miss)))
        fixed = 0
        for k in miss:
            v = trans(keys[k], lg)
            if v:
                d[k] = v
                fixed += 1
            time.sleep(0.5)
        json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        total += (len(miss) - fixed)
        log('%-3s fixed %d/%d, still missing %d' % (lg, fixed, len(miss), len(miss) - fixed))
    log('DONE. remaining missing across langs: %d' % total)


if __name__ == '__main__':
    main()
