# -*- coding: utf-8 -*-
"""Merge the 200 new table keys into js/i18n.js for all 16 languages.

- en: take English source from .cache/table_keys_all.json
- 15 others: take from translations/table_{lang}.json
- Skip any key already present in i18n.js (idempotent / no duplicates).
- Insert before each language block's closing marker.  Keep LF.
"""
import json, os, re

ROOT = r"C:/Users/Administrator/WorkBuddy/2026-08-12-16-19-26"
SRC = os.path.join(ROOT, "stark-steel-fresh", "js", "i18n.js")
KEYS = os.path.join(ROOT, "stark-steel-fresh", ".cache", "table_keys_all.json")
T_DIR = os.path.join(ROOT, "translations")
LANGS = ['en', 'zh', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'ar', 'ja', 'ko',
         'vi', 'th', 'tr', 'id', 'hi']


def esc(s):
    return s.replace('\\', '\\\\').replace('"', '\\"')


def main():
    en_src = json.load(open(KEYS, encoding='utf-8'))
    src = open(SRC, encoding='utf-8').read()
    if '\r' in src:
        src = src.replace('\r\n', '\n').replace('\r', '\n')

    trans = {'en': en_src}
    for lg in LANGS[1:]:
        f = os.path.join(T_DIR, 'table_%s.json' % lg)
        trans[lg] = json.load(open(f, encoding='utf-8'))

    for lg in LANGS:
        d = trans[lg]
        start_marker = '\n    %s: {' % lg
        end_marker = '\n    },' if lg != 'hi' else '\n    }'
        i = src.index(start_marker)
        j = src.index(end_marker, i)
        new_lines = []
        added = 0
        skipped = 0
        for k in en_src:
            if re.search(r'^\s*%s\s*:' % re.escape(k), src, re.M):
                skipped += 1
                continue
            v = d.get(k, '')
            new_lines.append('      %s: "%s",' % (k, esc(v)))
            added += 1
        if added:
            insertion = '\n' + '\n'.join(new_lines)
            src = src[:j] + insertion + src[j:]
        print('%-3s inserted %d (skipped %d already present)' % (lg, added, skipped))

    open(SRC, 'w', encoding='utf-8').write(src)
    print('written ->', SRC)


if __name__ == '__main__':
    main()
