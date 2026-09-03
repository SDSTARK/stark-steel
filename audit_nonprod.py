import re, os, glob, json

ROOT = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = ROOT
I18N = os.path.join(ROOT, 'js', 'i18n.js')

# 1) Extract all data-i18n keys + their visible English text from every HTML page
pages = sorted(glob.glob(os.path.join(HTML_DIR, '*.html')))
key_to_text = {}      # key -> english source text (first seen)
key_pages = {}        # key -> set of pages

for p in pages:
    html = open(p, encoding='utf-8').read()
    # find elements with data-i18n="key"
    for m in re.finditer(r'data-i18n="([^"]+)"', html):
        key = m.group(1)
        # capture the element's text content following the attribute
        start = m.end()
        # find matching tag close of the element that owns this attribute
        # grab a chunk and strip tags
        chunk = html[start:start+2000]
        # get text inside the element (up to next same-level tag)
        # simple: take text until the next tag that closes current element
        txt = re.sub(r'<[^>]+>', ' ', chunk)
        txt = re.sub(r'\s+', ' ', txt).strip()
        # trim at first child element boundary roughly
        if key not in key_to_text and txt:
            key_to_text[key] = txt[:200]
        key_pages.setdefault(key, set()).add(os.path.basename(p))

# 2) Parse i18n.js en block to know what's already translated
js = open(I18N, encoding='utf-8').read()
# en block: from "en: {" to the closing that ends the dict entry (next top-level lang)
en_start = js.index('en: {') + len('en: {')
# find matching close by scanning braces
depth = 0
i = en_start
while i < len(js):
    c = js[i]
    if c == '{': depth += 1
    elif c == '}':
        depth -= 1
        if depth == 0:
            en_end = i
            break
    i += 1
en_block = js[en_start:en_end]

en_keys = set(re.findall(r'([A-Za-z0-9_]+)\s*:', en_block))

# language block boundaries
langs = ['zh','es','fr','de','it','pt','ru','ar','ja','ko','vi','th','tr','id','hi']
lang_keycount = {}
for lg in langs:
    pat = re.compile(r'\b'+lg+r':\s*\{', re.DOTALL)
    mm = pat.search(js)
    if not mm:
        lang_keycount[lg] = set()
        continue
    s = mm.end()
    d = 0; j = s
    while j < len(js):
        c = js[j]
        if c == '{': d += 1
        elif c == '}':
            d -= 1
            if d == 0:
                blk = js[s:j]; break
        j += 1
    lang_keycount[lg] = set(re.findall(r'([A-Za-z0-9_]+)\s*:', blk))

# 3) Report
all_used = set(key_to_text.keys())
missing_en = sorted(k for k in all_used if k not in en_keys)
print("TOTAL keys used across pages:", len(all_used))
print("Keys already in en block:", len(all_used & en_keys))
print("Keys MISSING from en block (cause of 'no reaction'):", len(missing_en))
for k in missing_en:
    print("  MISSING-EN:", k, "| pages:", sorted(key_pages[k]), "| text:", key_to_text[k][:60])

# per-language missing for keys that ARE in en (these would fall back to English = 'no translation')
print("\n=== Keys in en but missing in other languages (page-scoped, count only) ===")
for lg in langs:
    miss = [k for k in all_used if k in en_keys and k not in lang_keycount[lg]]
    if miss:
        print(f"  {lg}: {len(miss)} missing (e.g. {miss[:5]})")
