const fs = require('fs');
const path = require('path');
const { JSDOM } = require('C:\\Users\\Administrator\\.workbuddy\\binaries\\node\\workspace\\node_modules\\jsdom');

const ROOT = 'C:\\Users\\Administrator\\WorkBuddy\\2026-08-12-16-19-26\\stark-steel-fresh';
const I18N = path.join(ROOT, 'js', 'i18n.js');
const i18nSrc = fs.readFileSync(I18N, 'utf-8');

// extract language codes from i18n.js LANGS
const langs = [...i18nSrc.matchAll(/code:\s*'([a-z]{2})'/g)].map(m => m[1]);
console.log('Languages:', langs.join(','));

const pages = fs.readdirSync(ROOT).filter(f => f.endsWith('.html')).sort();
let staticFail = [];
let dynFail = [];

for (const page of pages) {
  const htmlPath = path.join(ROOT, page);
  let html = fs.readFileSync(htmlPath, 'utf-8');
  const hasI18n = /src="js\/i18n\.js"/.test(html);
  const hasSwitch = /class="lang-switch"/.test(html);
  const hasHooks = /data-i18n=/.test(html);
  if (hasHooks && !hasI18n) staticFail.push(`${page}: has data-i18n but NO i18n.js include`);

  // dynamic: strip external scripts, inject i18n, test all langs
  const stripped = html.replace(/<script[^>]*src=[^>]*><\/script>/g, '');
  const dom = new JSDOM(stripped, { runScripts: 'dangerously', url: 'http://localhost/' });
  const { window } = dom;
  const s = window.document.createElement('script');
  s.textContent = i18nSrc;
  window.document.body.appendChild(s);
  window.document.dispatchEvent(new window.Event('DOMContentLoaded'));

  if (!window.StarkI18n) { dynFail.push(`${page}: StarkI18n not loaded`); continue; }

  const keys = [...window.document.querySelectorAll('[data-i18n]')].map(e => e.dataset.i18n);
  const keySet = [...new Set(keys)];
  let pageMissing = [];
  for (const lg of langs) {
    for (const k of keySet) {
      const t = window.StarkI18n.getText(k, lg);
      if (t === null || t === undefined || String(t).trim() === '') {
        pageMissing.push(`${k}@${lg}`);
      }
    }
  }
  if (pageMissing.length) dynFail.push(`${page}: ${pageMissing.length} empty/null (e.g. ${pageMissing.slice(0,5).join(', ')})`);
}

console.log('\n=== STATIC (script include) issues ===');
console.log(staticFail.length ? staticFail.join('\n') : '  NONE - every page with hooks includes i18n.js');
console.log('\n=== DYNAMIC (all keys resolve in all 16 langs) ===');
console.log(dynFail.length ? dynFail.join('\n') : '  NONE - all data-i18n keys resolve in all 16 languages');
console.log('\nPages checked:', pages.length);
