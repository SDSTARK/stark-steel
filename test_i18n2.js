const fs = require('fs');
const path = require('path');
const JSDOM = require('C:\\Users\\Administrator\\.workbuddy\\binaries\\node\\workspace\\node_modules\\jsdom').JSDOM;

const ROOT = 'C:\\Users\\Administrator\\WorkBuddy\\2026-08-12-16-19-26\\stark-steel-fresh';
const pages = process.argv.slice(2);
for (const page of pages) {
  const htmlPath = path.join(ROOT, page);
  let html = fs.readFileSync(htmlPath, 'utf-8');
  html = html.replace(/<script[^>]*src=[^>]*><\/script>/g, '');
  const dom = new JSDOM(html, { runScripts: 'dangerously', url: 'http://localhost/' });
  const { window } = dom;
  const i18nSrc = fs.readFileSync(path.join(ROOT, 'js', 'i18n.js'), 'utf-8');
  const s = window.document.createElement('script');
  s.textContent = i18nSrc;
  window.document.body.appendChild(s);
  window.document.dispatchEvent(new window.Event('DOMContentLoaded'));
  const navEl = window.document.querySelector('[data-i18n="navHome"]');
  const before = navEl ? navEl.textContent.trim() : '(no navHome)';
  let after = before;
  if (window.StarkI18n) { window.StarkI18n.applyLang('zh'); after = navEl ? navEl.textContent.trim() : '(no navHome)'; }
  const sel = window.document.querySelector('.lang-switch select') ? 'YES' : 'NO';
  console.log(`\n=== ${page} ===`);
  console.log('  StarkI18n:', !!window.StarkI18n, '| switch select:', sel);
  console.log('  navHome en->zh:', JSON.stringify(before), '->', JSON.stringify(after));
}
