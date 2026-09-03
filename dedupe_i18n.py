# -*- coding: utf-8 -*-
"""Deduplicate the 80 page-content keys within each language block of i18n.js.
Only the known page keys (single-line JSON entries) are deduped; all other
content is preserved untouched. Keeps the LAST occurrence (identical anyway)."""
import json, os, re

ROOT = r"C:/Users/Administrator/WorkBuddy/2026-08-12-16-19-26"
I18N = os.path.join(ROOT, "stark-steel-fresh", "js", "i18n.js")
KEYS = json.load(open(os.path.join(ROOT, "stark-steel-fresh", ".cache_pages_keys.json"), encoding='utf-8'))
PAGE_KEYS = set(KEYS.keys())

lines = open(I18N, encoding='utf-8').read().split('\n')
out = []
block_re = re.compile(r'^    ([a-z][a-z]): \{')
key_re = re.compile(r'^      "([A-Za-z0-9_]+)"\s*:')
removed = 0
in_block = False
seen_in_block = set()
for ln in lines:
    m = block_re.match(ln)
    if m:
        in_block = True
        seen_in_block = set()
        out.append(ln)
        continue
    if in_block and ln.strip() == '},':
        in_block = False
        out.append(ln)
        continue
    if in_block:
        km = key_re.match(ln)
        if km and km.group(1) in PAGE_KEYS:
            if km.group(1) in seen_in_block:
                removed += 1
                continue  # drop duplicate
            seen_in_block.add(km.group(1))
    out.append(ln)

open(I18N, 'w', encoding='utf-8').write('\n'.join(out))
print('duplicates removed:', removed)
# verify
txt = open(I18N, encoding='utf-8').read()
left = sum(1 for k in PAGE_KEYS if len(re.findall(r'\n      "%s"\s*:' % re.escape(k), txt)) != 16)
print('page keys NOT appearing exactly 16x:', left)
