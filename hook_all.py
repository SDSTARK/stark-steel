# -*- coding: utf-8 -*-
"""Add data-i18n hooks to ALL translatable table cells on every product page.

Covers BOTH table classes:
  - T1 : class="pd-table"
  - T2 : class="pd-table-extra"
Prev run only handled 5 pages' first table, leaving T2 + other pages broken.

Rules:
- Pure codes / numbers / dimensions / steel grades / standards -> left alone.
- English prose cells get a key:  p{NN}t{T}R{row}C{col}
- Layout fixes (错版):
    * single-cell row in a multi-column table -> add colspan = table max columns
    * (keeps original <th>/<td> tag to preserve styling)
- Already-hooked cells are skipped (idempotent re-run safe).
"""
import re, json
from pathlib import Path

SITE = Path(".")

TYPO_FIX = [("Itme", "Item"), ("dowm", "down")]

SKIP_EXACT = {
    "NO.1", "NO.2D", "NO.2B", "BA", "NO.3", "NO.4", "240#", "320#", "400#",
    "NO.6", "NO.7", "NO.8", "2D", "2B", "No.1", "No.3", "No.4", "HR",
    "1,2", "2,0", "2,2", "2,5", "3,2", "3,4", "4,0", "4,2", "4,5",
    "508mm or 610mm", "72104900.00", "±0,05",
}

PURE_DATA = re.compile(
    r"""^[\d\s\.,\-\+×x*/()\[\]#%°±~<>=&:/|\\]*(mm|cm|m|kg|g|t|ft|in|MPa|N|#|%|°)?[\d\s\.,\-\+×x*/()\[\]#%°±~<>=&:/|\\]*$""",
    re.I,
)
GRADE_LIST = re.compile(
    r"^[\s,]*(?:[A-Z]{1,4}\d{0,4}[A-Z]{0,3}(?:-[A-Z0-9]{1,4})?(?:[\s,]+|$))+$"
)
STANDARD_TOKENS = {
    "AISI", "ASTM", "ASME", "BS", "DIN", "GB", "JIS", "EN", "ISO", "API", "SAE",
    "SGS", "BV", "TUV", "CE", "FOB", "CFR", "CIF", "EXW", "DDP", "DDU",
    "TT", "LC", "DP", "DA", "SPM", "CPL", "HR", "BA", "GP", "HC", "MOQ",
    "HRB", "HPB", "Q195", "Q235", "Q345", "SS400", "A36", "SGCC", "DX51D",
}
STANDARD_ONLY = re.compile(
    r"^[\s,;/&.·\-\+()]*(" + "|".join(sorted(STANDARD_TOKENS, key=len, reverse=True))
    + r")[\s,;/&.·\-\+()\d]*$", re.I)

CELL_RE = re.compile(r"<(th|td)([^>]*)>(.*?)</\1>", re.S | re.I)


def needs_translation(text):
    t = text.strip()
    if not t:
        return False
    if t in SKIP_EXACT:
        return False
    if PURE_DATA.match(t):
        return False
    if GRADE_LIST.match(t) and re.search(r"\d", t):
        return False
    if STANDARD_ONLY.match(t):
        return False
    if re.match(r"^[\s,;/]*[TDLP]/[TDLPA][\s,;/]*", t):
        return False
    if re.match(r"^[\s,;/]*(?:T/T|L/C|D/P|D/A)[\s,;/]*", t, re.I):
        return False
    if re.match(r"^(T/T|L/C)[\s,]", t, re.I) and len(re.findall(r"[A-Za-z]{5,}", t)) <= 2:
        return False
    items = [i.strip() for i in re.split(r"[,/;]", t) if i.strip()]
    if len(items) >= 3:
        def is_code(s):
            s = re.sub(r"[\s()\[\]:.]", "", s)
            if len(s) > 10:
                return False
            if re.search(r"[A-Za-z]{5,}", s):
                return False
            return bool(re.match(r"^[A-Za-z0-9#°\-\+~×x\.]+$", s))
        if all(is_code(i) for i in items):
            return False
    words = re.findall(r"[A-Za-z]{4,}", t)
    return bool(words)


def process(path):
    raw = path.read_bytes()
    eol = "\r\n" if b"\r\n" in raw else "\n"
    text = raw.decode("utf-8", errors="replace")
    page = path.stem.replace("product-", "p")
    total_hooked = []

    tables = list(re.finditer(
        r'<table\b([^>]*class="[^"]*pd-table[^"]*"[^>]*)>(.*?)</table>', text, re.S | re.I))
    if not tables:
        return 0, []

    out_text = text
    for ti, mt in enumerate(reversed(tables), 1):
        T = len(tables) - ti + 1
        attrs, tbl = mt.group(1), mt.group(2)
        for wr, right in TYPO_FIX:
            tbl = tbl.replace(wr, right)
        rows = re.findall(r"<tr[^>]*>(.*?)</tr>", tbl, re.S | re.I)
        maxcols = 1
        for r in rows:
            cs = len(CELL_RE.findall(r))
            if cs > maxcols:
                maxcols = cs

        state = {"ci": 0, "n_cells": 0, "maxcols": maxcols,
                 "page": page, "T": T, "ri": 0, "hooked": total_hooked}

        def repl(m):
            tag, at, content = m.group(1), m.group(2), m.group(3)
            state["ci"] += 1
            ci = state["ci"]
            plain = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", content)).strip()
            # layout fix (错版): a lone cell in a multi-column table -> span it
            if state["n_cells"] == 1 and state["maxcols"] > 1:
                if "colspan" not in at:
                    at = at.rstrip() + ' colspan="%d"' % state["maxcols"]
                if "data-i18n" in at:
                    return "<%s%s>%s</%s>" % (tag, at, content, tag)
                if needs_translation(plain):
                    key = "%st%dR%dC%d" % (state["page"], state["T"], state["ri"], ci)
                    state["hooked"].append((key, plain))
                    return '<%s data-i18n="%s"%s>%s</%s>' % (tag, key, at, content, tag)
                return "<%s%s>%s</%s>" % (tag, at, content, tag)
            # normal (multi-cell) row
            if "data-i18n" in at:
                return m.group(0)
            if needs_translation(plain):
                key = "%st%dR%dC%d" % (state["page"], state["T"], state["ri"], ci)
                state["hooked"].append((key, plain))
                return '<%s data-i18n="%s"%s>%s</%s>' % (tag, key, at, content, tag)
            return m.group(0)

        # capture full <tr>...</tr> so row wrappers are preserved
        rows_full = re.findall(r"(<tr[^>]*>.*?</tr>)", tbl, re.S | re.I)
        new_rows = []
        for ri, rfull in enumerate(rows_full, 1):
            state["ci"] = 0
            state["ri"] = ri
            state["n_cells"] = len(CELL_RE.findall(rfull))
            new_rows.append(CELL_RE.sub(repl, rfull))
        new_tbl = eol.join(new_rows)
        full = "<table" + attrs + ">" + new_tbl + "</table>"
        out_text = out_text[:mt.start()] + full + out_text[mt.end():]

    path.write_bytes(out_text.encode("utf-8"))
    return len(total_hooked), total_hooked


pages = sorted(SITE.glob("product-*.html"))
all_hooked = {}
for p in pages:
    n, hooked = process(p)
    all_hooked[p.stem] = hooked
    if n:
        print("%s: +%d hooks" % (p.name, n))

merged = {}
for pg, items in all_hooked.items():
    for k, v in items:
        merged[k] = v
Path(".cache/table_keys_all.json").write_text(
    json.dumps(merged, ensure_ascii=False, indent=1), encoding="utf-8")
print("\nTotal new keys: %d -> .cache/table_keys_all.json" % len(merged))
