import re, os, glob

HTML = "."
pages = sorted(glob.glob(os.path.join(HTML, "product-*.html")))

def cells_text_hooks(tbl):
    rows = re.findall(r'<tr.*?</tr>', tbl, re.S|re.I)
    out=[]
    for r in rows:
        cells = re.findall(r'<t[hd].*?</t[hd]>', r, re.S|re.I)
        for c in cells:
            txt = re.sub(r'<[^>]+>', '', c)
            txt = re.sub(r'\s+', ' ', txt).strip()
            hook = re.search(r'data-i18n="([^"]+)"', c)
            out.append((txt, bool(hook), hook.group(1) if hook else None))
    return out

for p in pages:
    html = open(p, encoding='utf-8').read()
    tables = re.findall(r'<table.*?</table>', html, re.S|re.I)
    name = os.path.basename(p)
    for ti, tbl in enumerate(tables):
        cells = cells_text_hooks(tbl)
        textcells = [(t,k,key) for (t,k,key) in cells if t]
        n = len(textcells)
        untrans = [t for (t,k,key) in textcells if not k]
        # classify: pure number/spec?
        def is_spec(t):
            t2=t.replace(' ','')
            return bool(re.fullmatch(r'[0-9xX×*/\-\.,–—~()+\s%MMAaBbCcDdEeFfGgHhKkLlNnPpRrSsTtUuWwYyZz/|]*', t2)) and any(c.isdigit() for c in t2)
        untrans_real = [t for t in untrans if not is_spec(t)]
        pct = (len(untrans_real)/n*100) if n else 0
        if n>=4 and pct>=40:
            print(f"{name} T{ti+1}: cells={n} untranslated_text={len(untrans_real)} ({pct:.0f}%)  e.g. {untrans_real[:4]}")
