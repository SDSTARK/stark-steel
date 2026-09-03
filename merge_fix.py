# -*- coding: utf-8 -*-
"""Force-overwrite the 202 table keys in js/i18n.js with the correct
translated values from translations/table_{lang}.json (post-terminology).

The earlier (interrupted) merge had written English source values into the
non-en blocks, so we now replace every occurrence of each of the 202 keys
within each language block. Keys not in the 202 set are left untouched.
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
        sm = '\n    %s: {' % lg
        em = '\n    },' if lg != 'hi' else '\n    }'
        i = src.index(sm)
        j = src.index(em, i)
        block = src[i:j]
        replaced = 0
        for k in en_src:
            pat = re.compile(r'(^[ \t]*%s[ \t]*:[ \t]*")((?:[^"\\]|\\.)*)"' % re.escape(k), re.M)
            m = pat.search(block)
            if not m:
                continue
            v = d.get(k) or en_src.get(k) or ''
            newtext = m.group(1) + esc(v) + '"'
            block = block[:m.start()] + newtext + block[m.end():]
            replaced += 1
        src = src[:i] + block + src[j:]
        print('%-3s overwrote %d keys' % (lg, replaced))

    open(SRC, 'w', encoding='utf-8').write(src)
    print('written ->', SRC)


if __name__ == '__main__':
    main()
