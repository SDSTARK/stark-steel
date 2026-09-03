# -*- coding: utf-8 -*-
"""Translate the 200 new table keys (table_keys_all.json) into 15 languages.

Writes into the shared C:/.../translations/table_{lang}.json (which already
holds the prior p05/06/08/09/10 keys); existing keys are preserved.
Resume-capable: writes every 10 keys.
"""
import json, os, sys, time, urllib.request, urllib.parse, urllib.error

ROOT = r"C:/Users/Administrator/WorkBuddy/2026-08-12-16-19-26"
OUT_DIR = os.path.join(ROOT, "translations")
KEYS = os.path.join(ROOT, "stark-steel-fresh", ".cache", "table_keys_all.json")
LOG = os.path.join(ROOT, "stark-steel-fresh", "translate_all_log.txt")
LANGS = ['zh', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'ar', 'ja', 'ko',
         'vi', 'th', 'tr', 'id', 'hi']
os.makedirs(OUT_DIR, exist_ok=True)


def log(msg):
    line = time.strftime('%H:%M:%S ') + msg
    print(line, flush=True)
    with open(LOG, 'a', encoding='utf-8') as fh:
        fh.write(line + '\n')


def fetch(url, headers=None, timeout=15):
    req = urllib.request.Request(url, headers=headers or {'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode('utf-8', 'replace')
    except urllib.error.HTTPError as e:
        try:
            return e.code, e.read().decode('utf-8', 'replace')[:300]
        except Exception:
            return e.code, ''
    except Exception as e:
        return 0, str(e)[:200]


def google_translate(text, tl):
    q = urllib.parse.quote(text)
    url = ('https://clients5.google.com/translate_a/t?client=dict-chrome-ex'
           '&sl=en&tl=%s&q=%s' % (tl, q))
    st, body = fetch(url)
    if st == 200:
        try:
            arr = json.loads(body)
            if arr and arr[0]:
                return arr[0].replace('\ufeff', '').strip()
        except Exception:
            pass
    return None


def mymemory_translate(text, tl):
    q = urllib.parse.quote(text)
    url = 'https://api.mymemory.translated.net/get?q=%s&langpair=en|%s' % (q, tl)
    st, body = fetch(url)
    if st == 200:
        try:
            j = json.loads(body)
            t = j.get('responseData', {}).get('translatedText')
            if t and t.strip():
                return t.strip()
        except Exception:
            pass
    return None


def translate_text(text, tl):
    for attempt in range(3):
        try:
            r = google_translate(text, tl)
        except Exception:
            r = None
        if r and r.strip():
            return r.strip()
        time.sleep(1.2 * (attempt + 1))
    for attempt in range(2):
        try:
            r = mymemory_translate(text, tl)
        except Exception:
            r = None
        if r and r.strip():
            return r.strip()
        time.sleep(1.5 * (attempt + 1))
    return None


def main():
    keys = json.load(open(KEYS, encoding='utf-8'))
    log('table keys to translate: %d' % len(keys))
    total_fail = 0
    for lg in LANGS:
        outfile = os.path.join(OUT_DIR, 'table_%s.json' % lg)
        done = {}
        if os.path.exists(outfile):
            done = json.load(open(outfile, encoding='utf-8'))
        todo = [k for k in keys if k not in done]
        if not todo:
            log('%-3s already complete (%d)' % (lg, len(done)))
            continue
        log('%-3s translating %d keys...' % (lg, len(todo)))
        fails = []
        for i, k in enumerate(todo, 1):
            v = translate_text(keys[k], lg)
            if v is None:
                fails.append(k)
                log('   FAIL %s' % k)
            else:
                done[k] = v
            if i % 10 == 0:
                with open(outfile, 'w', encoding='utf-8') as fh:
                    json.dump(done, fh, ensure_ascii=False, indent=1)
                log('   %s %d/%d' % (lg, i, len(todo)))
            time.sleep(0.35)
        with open(outfile, 'w', encoding='utf-8') as fh:
            json.dump(done, fh, ensure_ascii=False, indent=1)
        total_fail += len(fails)
        log('%-3s done: %d keys, %d failures' % (lg, len(done), len(fails)))
    log('ALL DONE. total failures: %d' % total_fail)


if __name__ == '__main__':
    main()
