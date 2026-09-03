# -*- coding: utf-8 -*-
"""Merge the 80 missing page-content keys into all 16 language blocks of i18n.js.
Reads translations from .cache_pages_trans/<lang>.json. Idempotent.
"""
import json, os, re

ROOT = r"C:/Users/Administrator/WorkBuddy/2026-08-12-16-19-26"
I18N = os.path.join(ROOT, "stark-steel-fresh", "js", "i18n.js")
KEYS = os.path.join(ROOT, "stark-steel-fresh", ".cache_pages_keys.json")
CACHE = os.path.join(ROOT, "stark-steel-fresh", ".cache_pages_trans")
LANGS = ['zh', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'ar', 'ja', 'ko', 'vi', 'th', 'tr', 'id', 'hi']

EN = json.load(open(KEYS, encoding='utf-8'))
js = open(I18N, encoding='utf-8').read()

# only keys not already in i18n.js
def present(k):
    return bool(re.search(r'\n      ' + re.escape(k) + r'\s*:', js))
MISSING = [k for k in EN if not present(k)]
print('keys to merge:', len(MISSING))

# load cached translations
trans = {lg: (json.load(open(os.path.join(CACHE, lg + '.json'), encoding='utf-8')) if os.path.exists(os.path.join(CACHE, lg + '.json')) else {}) for lg in LANGS}

ALL_BLOCKS = ['en'] + LANGS
total_merged = 0
for lg in ALL_BLOCKS:
    src = EN if lg == 'en' else trans.get(lg, {})
    m = re.search(r'\n    ' + lg + r': \{', js)
    if not m:
        print('BLOCK NOT FOUND:', lg); continue
    insert_pos = m.end()
    lines = []
    for k in MISSING:
        val = src.get(k, EN[k])
        lines.append('      "%s": %s,\n' % (k, json.dumps(val, ensure_ascii=False)))
    block_open = js[:insert_pos] + '\n'
    block_rest = js[insert_pos:]
    js = block_open + ''.join(lines) + block_rest
    total_merged += len(MISSING)
    print('merged into', lg, '(%d keys)' % len(MISSING))

open(I18N, 'w', encoding='utf-8').write(js)
print('\nTOTAL merged entries:', total_merged)

# verify
js2 = open(I18N, encoding='utf-8').read()
still_missing = [k for k in MISSING if not re.search(r'\n      ' + re.escape(k) + r'\s*:', js2)]
print('still missing after merge:', len(still_missing), still_missing[:10])
