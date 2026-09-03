# -*- coding: utf-8 -*-
"""Insert the 202 table keys into each NON-en language block of js/i18n.js.

Root cause of the bad prior merge: it checked key presence against the WHOLE
file, so once `en` got the keys, every other language was skipped. Result:
only the `en` block contained the keys. This script inserts the translated
values into each non-en block (per-block insert, no whole-file skip).
`en` is already correct and is left untouched.
"""
import json, os, re

ROOT = r"C:/Users/Administrator/WorkBuddy/2026-08-12-16-19-26"
SRC = os.path.join(ROOT, "stark-steel-fresh", "js", "i18n.js")
KEYS = os.path.join(ROOT, "stark-steel-fresh", ".cache", "table_keys_all.json")
T_DIR = os.path.join(ROOT, "translations")
LANGS = ['zh', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'ar', 'ja', 'ko',
         'vi', 'th', 'tr', 'id', 'hi']


def esc(s):
    return s.replace('\\', '\\\\').replace('"', '\\"')


def main():
    en_src = json.load(open(KEYS, encoding='utf-8'))
    src = open(SRC, encoding='utf-8').read()
    if '\r' in src:
        src = src.replace('\r\n', '\n').replace('\r', '\n')

    trans = {}
    for lg in LANGS:
        f = os.path.join(T_DIR, 'table_%s.json' % lg)
        trans[lg] = json.load(open(f, encoding='utf-8'))

    for lg in LANGS:
        d = trans[lg]
        sm = '\n    %s: {' % lg
        em = '\n    },' if lg != 'hi' else '\n    }'
        i = src.index(sm)
        j = src.index(em, i)
        block = src[i:j]
        new_lines = []
        added = 0
        for k in en_src:
            if re.search(r'^[ \t]*%s[ \t]*:' % re.escape(k), block, re.M):
                continue
            v = d.get(k) or en_src.get(k) or ''
            new_lines.append('      %s: "%s",' % (k, esc(v)))
            added += 1
        if new_lines:
            insertion = '\n' + '\n'.join(new_lines)
            src = src[:j] + insertion + src[j:]
        print('%-3s inserted %d' % (lg, added))

    open(SRC, 'w', encoding='utf-8').write(src)
    print('written ->', SRC)


if __name__ == '__main__':
    main()
