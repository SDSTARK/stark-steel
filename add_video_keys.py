# -*- coding: utf-8 -*-
"""Add 2 new about-page video section keys and translate to 15 languages, merge into i18n.js."""
import json, os, re, time, urllib.request, urllib.parse, urllib.error

ROOT = r"C:/Users/Administrator/WorkBuddy/2026-08-12-16-19-26"
I18N = os.path.join(ROOT, "stark-steel-fresh", "js", "i18n.js")
LANGS = ['zh', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'ar', 'ja', 'ko', 'vi', 'th', 'tr', 'id', 'hi']

EN = {
    "companyVideoTitle": "Strength You Can Trust",
    "companyVideoSub": "Shandong Stark Steel — Your Global Metal Partner",
}

def fetch(url, headers=None, timeout=15):
    req = urllib.request.Request(url, headers=headers or {'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode('utf-8', 'replace')
    except urllib.error.HTTPError as e:
        try: return e.code, e.read().decode('utf-8', 'replace')[:300]
        except Exception: return e.code, ''
    except Exception as e:
        return 0, str(e)[:200]

def google(text, tl):
    q = urllib.parse.quote(text)
    url = 'https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=en&tl=%s&q=%s' % (tl, q)
    st, body = fetch(url)
    if st == 200:
        try:
            arr = json.loads(body)
            if arr and arr[0]:
                return arr[0].replace('\ufeff', '').strip()
        except Exception: pass
    return None

def mymemory(text, tl):
    q = urllib.parse.quote(text)
    url = 'https://api.mymemory.translated.net/get?q=%s&langpair=en|%s' % (q, tl)
    st, body = fetch(url)
    if st == 200:
        try:
            t = json.loads(body).get('responseData', {}).get('translatedText')
            if t and t.strip(): return t.strip()
        except Exception: pass
    return None

def translate(text, tl):
    for _ in range(3):
        r = google(text, tl)
        if r and r.strip(): return r.strip()
        time.sleep(1.2)
    for _ in range(2):
        r = mymemory(text, tl)
        if r and r.strip(): return r.strip()
        time.sleep(1.5)
    return None

# Translate
trans = {lg: {} for lg in LANGS}
fails = []
for lg in LANGS:
    for k, en in EN.items():
        v = translate(en, lg)
        if v: trans[lg][k] = v
        else:
            fails.append((lg, k)); trans[lg][k] = en  # fallback to en, never null
    print('%-3s done (title=%s)' % (lg, trans[lg]['companyVideoTitle'][:30]))

# Merge into i18n.js: insert into each language block (en + 15) if missing
js = open(I18N, encoding='utf-8').read()
all_langs = ['en'] + LANGS
for lg in all_langs:
    src = EN if lg == 'en' else trans[lg]
    # find block start
    m = re.search(r'\n    ' + lg + r': \{', js)
    if not m:
        print('BLOCK NOT FOUND for', lg); continue
    insert_pos = m.end()  # right after '{'
    # check if keys already present
    if '"companyVideoTitle"' in js.split(lg + ': {')[1].split('\n    ' + ('hi' if lg=='hi' else '[a-z][a-z]') + ':')[0]:
        # crude; rely on below replace-safe insert
        pass
    lines = []
    for k, v in src.items():
        if re.search(r'\n      ' + re.escape(k) + r'\s*:', js):
            continue  # already present
        lines.append('      "%s": %s,\n' % (k, json.dumps(v, ensure_ascii=False)))
    if lines:
        js = js[:insert_pos] + '\n' + ''.join(lines) + js[insert_pos:]

open(I18N, 'w', encoding='utf-8').write(js)
print('\nMerged companyVideoTitle/Sub into all 16 blocks.')
print('Fallback-to-en (translation failed):', fails if fails else 'none')
