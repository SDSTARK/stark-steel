import re, os, glob, json

HTML = "."
pages = sorted(glob.glob(os.path.join(HTML, "product-*.html")))

# Load i18n.js keys
with open(os.path.join(HTML, "js/i18n.js"), encoding="utf-8") as f:
    js = f.read()

defined_keys = set(re.findall(r'^\s*([a-zA-Z0-9_]+):\s*[\'"\x60]', js, re.M))

def audit_page(path):
    with open(path, encoding="utf-8") as f:
        html = f.read()
    tables = re.findall(r'<table.*?</table>', html, re.S|re.I)
    res = []
    for ti, tbl in enumerate(tables):
        rows = re.findall(r'<tr.*?</tr>', tbl, re.S|re.I)
        colcounts = []
        hooks = 0
        celltexts = []
        for r in rows:
            cells = re.findall(r'<t[hd].*?</t[hd]>', r, re.S|re.I)
            colcounts.append(len(cells))
            for c in cells:
                txt = re.sub(r'<[^>]+>', '', c)
                txt = txt.strip()
                if txt:
                    celltexts.append(txt)
                if 'data-i18n' in c:
                    hooks += 1
        maxc = max(colcounts) if colcounts else 0
        inconsistent = len(set(colcounts)) > 1
        res.append({
            "table": ti+1, "rows": len(rows), "colcounts": colcounts,
            "maxcol": maxc, "inconsistent": inconsistent, "hooks": hooks,
            "sample": celltexts[:6]
        })
    return res

for p in pages:
    res = audit_page(p)
    name = os.path.basename(p)
    ntables = len(res)
    for r in res:
        flag = ""
        if r["inconsistent"]: flag += " [错版:列数不一]"
        if r["hooks"] == 0: flag += " [无翻译钩子]"
        print(f"{name} T{r['table']}: rows={r['rows']} maxcol={r['maxcol']} hooks={r['hooks']}{flag} cols={r['colcounts']}")
    if ntables == 0:
        print(f"{name}: NO TABLE")
