import re, json, glob, os

ROOT = "."

# ---------- 1) Payment terms -> uniform "T/T (30% deposit)" ----------
pay_re = re.compile(r'(<th data-i18n="thPaymentTerm[^"]*">.*?</th>\s*)<td>[^<]*</td>', re.S|re.I)
new_td = '<td data-i18n="paymentTermsValue">T/T (30% deposit)</td>'
pay_files = 0
for f in sorted(glob.glob(os.path.join(ROOT, "product-*.html"))):
    s = open(f, encoding="utf-8").read()
    if "thPaymentTerm" not in s:
        continue
    s2, n = pay_re.subn(lambda m: m.group(1) + new_td, s)
    if n:
        open(f, "w", encoding="utf-8", newline="\n").write(s2)
        pay_files += 1
        print(f"payment terms unified: {os.path.basename(f)} ({n} cell(s))")
print(f"payment-terms files touched: {pay_files}")

# ---------- 2) product-08 continuation rows: <th colspan=2> -> <td colspan=2> ----------
p08 = os.path.join(ROOT, "product-08.html")
s = open(p08, encoding="utf-8").read()
p08re = re.compile(r'<th colspan="2" data-i18n="(p08R\d+C1)">([\s\S]*?)</th>')
s2, n = p08re.subn(lambda m: '<td colspan="2" data-i18n="%s">%s</td>' % (m.group(1), m.group(2)), s)
if n:
    open(p08, "w", encoding="utf-8", newline="\n").write(s2)
    print(f"product-08 continuation rows fixed: {n}")
else:
    print("product-08: no continuation rows matched")

# ---------- 3) product-04 restructure messy rows 8-10 into clean 2-col block ----------
p04 = os.path.join(ROOT, "product-04.html")
s = open(p04, encoding="utf-8").read()
old = ("<tr>\n"
       '<th data-i18n="thDiameterMm">Diameter(mm)</th>\n'
       '<td data-i18n="p04t1R8C2">Hot Rolling Round Bar</td>\n'
       "<td>25 - 600</td>\n"
       '<td data-i18n="p04t1R8C4">Cold Rolling Square Bar</td>\n'
       "<td>6 - 50.8</td>\n"
       "</tr>\n"
       "<tr>\n"
       '<th data-i18n="thHotRollingSquareBar">Hot Rolling Square Bar</th>\n'
       "<td>21 - 54</td>\n"
       '<td data-i18n="p04t1R9C3">Cold Rolling Hexagon Bar</td>\n'
       "<td>9.5 - 65</td>\n"
       "</tr>\n"
       "<tr>\n"
       '<th data-i18n="thColdRollingRoundBar">Cold Rolling Round bar</th>\n'
       "<td>6 - 101.6</td>\n"
       '<td data-i18n="p04t1R10C3">Forged Rebar</td>\n'
       "<td>200 - 1000</td>\n"
       "</tr>")
new = ("<tr>\n"
       '<th data-i18n="thItem">Item</th>\n'
       '<th data-i18n="thDiameterMm">Diameter (mm)</th>\n'
       "</tr>\n"
       "<tr>\n"
       '<td data-i18n="p04dia1">Hot Rolling Round Bar</td>\n'
       "<td>25 - 600</td>\n"
       "</tr>\n"
       "<tr>\n"
       '<td data-i18n="p04dia2">Cold Rolling Square Bar</td>\n'
       "<td>6 - 50.8</td>\n"
       "</tr>\n"
       "<tr>\n"
       '<td data-i18n="p04dia3">Hot Rolling Square Bar</td>\n'
       "<td>21 - 54</td>\n"
       "</tr>\n"
       "<tr>\n"
       '<td data-i18n="p04dia4">Cold Rolling Hexagon Bar</td>\n'
       "<td>9.5 - 65</td>\n"
       "</tr>\n"
       "<tr>\n"
       '<td data-i18n="p04dia5">Cold Rolling Round Bar</td>\n'
       "<td>6 - 101.6</td>\n"
       "</tr>\n"
       "<tr>\n"
       '<td data-i18n="p04dia6">Forged Rebar</td>\n'
       "<td>200 - 1000</td>\n"
       "</tr>")
if old in s:
    s = s.replace(old, new, 1)
    open(p04, "w", encoding="utf-8", newline="\n").write(s)
    print("product-04 rows 8-10 restructured into clean 2-col block")
else:
    print("WARN: product-04 old block not found - check exact whitespace")

# ---------- 4) Update key json: drop obsolete p04 keys, add new dia keys ----------
jpath = os.path.join(ROOT, ".cache", "table_keys_all.json")
d = json.load(open(jpath, encoding="utf-8"))
for k in ["p04t1R8C2", "p04t1R8C4", "p04t1R9C3", "p04t1R10C3",
          "thHotRollingSquareBar", "thColdRollingRoundBar"]:
    if k in d:
        del d[k]
        print(f"  removed obsolete key: {k}")
for k, v in {
    "p04dia1": "Hot Rolling Round Bar",
    "p04dia2": "Cold Rolling Square Bar",
    "p04dia3": "Hot Rolling Square Bar",
    "p04dia4": "Cold Rolling Hexagon Bar",
    "p04dia5": "Cold Rolling Round Bar",
    "p04dia6": "Forged Rebar",
}.items():
    d[k] = v
json.dump(d, open(jpath, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("key json updated: total keys =", len(d))

# ---------- 5) Add paymentTermsValue to i18n.js (all 16 langs, uniform) ----------
ij = os.path.join(ROOT, "js", "i18n.js")
s = open(ij, encoding="utf-8").read()
if '"paymentTermsValue"' not in s:
    langs = ['en','zh','es','fr','de','it','pt','ru','ja','ko','vi','th','tr','id','ar','hi']
    for lg in langs:
        s = re.sub(r'(    %s: \{)' % lg, r'\1\n      "paymentTermsValue": "T/T (30% deposit)",', s, count=1)
    open(ij, "w", encoding="utf-8", newline="\n").write(s)
    print("paymentTermsValue added to i18n.js (16 langs)")
else:
    print("paymentTermsValue already present")
print("DONE phaseA")
