// Verify: every data-i18n key on each product page resolves in i18n.js for all 16 langs.
const fs = require('fs');
const path = require('path');
const { JSDOM } = require('C:/Users/Administrator/.workbuddy/binaries/node/workspace/node_modules/jsdom');

const ROOT = 'C:/Users/Administrator/WorkBuddy/2026-08-12-16-19-26/stark-steel-fresh';
const i18nSrc = fs.readFileSync(path.join(ROOT, 'js/i18n.js'), 'utf8');

const LANGS = ['en','zh','es','fr','de','it','pt','ru','ar','ja','ko','vi','th','tr','id','hi'];
const pages = fs.readdirSync(ROOT).filter(f => /^product-\d+\.html$/.test(f)).sort();

let problems = 0;
const missingByPage = {};

for (const pg of pages) {
  const html = fs.readFileSync(path.join(ROOT, pg), 'utf8');
  const dom = new JSDOM(html, { runScripts: 'outside-only', url: 'https://sdstarksteel.com/' + pg });
  const { window } = dom;
  // expose localStorage shim if needed
  try { window.eval(i18nSrc); } catch (e) { console.log('EVAL ERR', pg, e.message); continue; }
  const S = window.StarkI18n;
  if (!S) { console.log('NO StarkI18n', pg); continue; }
  const els = [...window.document.querySelectorAll('[data-i18n]')];
  const keys = els.map(e => e.dataset.i18n);
  const uniq = [...new Set(keys)];
  const missing = [];
  const empty = [];
  for (const k of uniq) {
    for (const lg of LANGS) {
      const t = S.getText(k, lg);
      if (t === null) missing.push(lg + ':' + k);
      else if (typeof t === 'string' && t.trim() === '') empty.push(lg + ':' + k);
    }
  }
  // also detect elements left empty after applyLang for a sample language
  S.applyLang('zh');
  const emptyEls = els.filter(e => !(e.textContent || '').trim());
  if (missing.length || empty.length || emptyEls.length) {
    problems++;
    missingByPage[pg] = { keys: uniq.length, missing: missing.slice(0,8), empty: empty.slice(0,8), emptyEls: emptyEls.length };
    console.log(`${pg}: ${uniq.length} keys | missing=${missing.length} empty=${empty.length} emptyEls(zh)=${emptyEls.length}`);
    if (missing.length) console.log('   missing sample:', missing.slice(0,8).join(', '));
  } else {
    console.log(`${pg}: OK (${uniq.length} keys)`);
  }
}
console.log('\nPAGES WITH PROBLEMS:', problems);
fs.writeFileSync(path.join(ROOT, 'verify_report.json'), JSON.stringify(missingByPage, null, 2));
