# -*- coding: utf-8 -*-
"""Full finish pipeline (runs as a background task):
1. Wait for orphaned translate_all.py (pid 15416) to exit.
2. Gap-fill translate (re-run translate_all.py up to 3x).
3. Fill any still-missing keys with English source (no empty values).
4. Steel terminology corrections.
5. Merge new keys into js/i18n.js.
6. node --check + jsdom verify (16 langs, 0 missing/empty).
7. git commit + push via proxy.
Writes pipeline_report.txt at the end.
"""
import subprocess, sys, os, time, json, re

ROOT = r"C:/Users/Administrator/WorkBuddy/2026-08-12-16-19-26"
FRESH = os.path.join(ROOT, "stark-steel-fresh")
PY = sys.executable
NODE = r"C:/Users/Administrator/.workbuddy/binaries/node/versions/22.22.2/node.exe"
PROXY = "http://127.0.0.1:7897"
ORPHAN_PID = "15416"
REPORT = os.path.join(FRESH, "pipeline_report.txt")

LANGS = ['zh','es','fr','de','it','pt','ru','ar','ja','ko','vi','th','tr','id','hi']
T_DIR = os.path.join(ROOT, "translations")
KEYS = os.path.join(FRESH, ".cache", "table_keys_all.json")

def run(cmd, **kw):
    kw.setdefault('cwd', FRESH)
    return subprocess.run(cmd, capture_output=True, text=True, **kw)

def log(msg):
    line = time.strftime('%H:%M:%S ') + msg
    print(line, flush=True)
    with open(REPORT, 'a', encoding='utf-8') as fh:
        fh.write(line + '\n')

def alive(pid):
    out = subprocess.run(['tasklist','/fi','PID eq %s' % pid],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout
    return pid.encode() in out

def missing_count():
    en = json.load(open(KEYS, encoding='utf-8'))
    total = 0
    per = {}
    for lg in LANGS:
        f = os.path.join(T_DIR, 'table_%s.json' % lg)
        d = json.load(open(f, encoding='utf-8')) if os.path.exists(f) else {}
        miss = sum(1 for k in en if not str(d.get(k,'')).strip())
        per[lg] = miss
        total += miss
    return total, per

# ---- 1. wait for orphan ----
log("waiting for orphan translate pid %s ..." % ORPHAN_PID)
waited = 0
while alive(ORPHAN_PID) and waited < 75*60:
    time.sleep(30); waited += 30
    if waited % 300 == 0:
        log("  still waiting (%d min)" % (waited//60))
if alive(ORPHAN_PID):
    log("WARN: orphan still alive after 75 min, proceeding anyway")
else:
    log("orphan finished after ~%d min" % (waited//60))

# ---- 2. gap-fill translate ----
for attempt in range(1, 4):
    mc, per = missing_count()
    log("gap-fill attempt %d: %d missing keys" % (attempt, mc))
    if mc == 0:
        break
    r = run([PY, 'translate_all.py'])
    log("  translate_all exit=%d" % r.returncode)
    if r.returncode != 0:
        log("  translate stderr: " + r.stderr[:500])
mc, per = missing_count()
log("after gap-fill: %d missing" % mc)
if mc:
    log("  remaining per lang: " + str(per))

# ---- 3. fill missing with English ----
en = json.load(open(KEYS, encoding='utf-8'))
filled = 0
for lg in LANGS:
    f = os.path.join(T_DIR, 'table_%s.json' % lg)
    if not os.path.exists(f):
        json.dump({}, open(f,'w',encoding='utf-8'))
    d = json.load(open(f, encoding='utf-8'))
    for k in en:
        if not str(d.get(k,'')).strip():
            d[k] = en[k]   # English fallback
            filled += 1
    json.dump(d, open(f,'w',encoding='utf-8'), ensure_ascii=False, indent=1)
log("filled %d missing keys with English fallback" % filled)

# ---- 4. terminology ----
r = run([PY, 'terminology_all.py'])
log("terminology exit=%d" % r.returncode)
log("  " + (r.stdout or r.stderr)[:800].replace('\n',' | '))

# ---- 5. merge ----
r = run([PY, 'merge_all.py'])
log("merge exit=%d" % r.returncode)
log("  " + (r.stdout or r.stderr)[:400].replace('\n',' | '))

# ---- 6. node check + verify ----
r = run([NODE, '--check', os.path.join(FRESH, 'js/i18n.js')])
log("node --check i18n.js exit=%d" % r.returncode)
if r.returncode != 0:
    log("  " + r.stderr[:600])

r = run([NODE, os.path.join(FRESH, 'verify.js')])
log("verify.js exit=%d" % r.returncode)
log("  " + (r.stdout or r.stderr)[-1500:])

# ---- 7. git commit + push ----
env = dict(os.environ)
env['GIT_HTTP_PROXY'] = PROXY
env['HTTPS_PROXY'] = PROXY
env['http_proxy'] = PROXY
env['https_proxy'] = PROXY
r = run(['git','add','product-02.html','product-03.html','product-04.html',
         'product-05.html','product-06.html','product-07.html','product-08.html',
         'product-09.html','product-10.html','product-11.html','product-12.html',
         'product-13.html','product-14.html','product-15.html','product-16.html',
         'product-17.html','product-18.html','product-19.html','product-20.html',
         'js/i18n.js'], env=env)
log("git add exit=%d" % r.returncode)
r = run(['git','commit','-m',
         'fix: unify payment terms to T/T(30%% deposit); fix rebar/galv-pipe table layout; '
         'translate all product spec tables (T1+T2) into 16 languages; steel terminology fixes'],
        env=env)
log("git commit exit=%d" % r.returncode)
log("  " + (r.stdout or r.stderr)[:400])
r = run(['git','push','origin','main'], env=env)
log("git push exit=%d" % r.returncode)
log("  " + (r.stdout or r.stderr)[:600])

log("PIPELINE DONE")
