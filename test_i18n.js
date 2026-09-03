const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const ROOT = __dirname;
const pages = process.argv.slice(2).length ? process.argv.slice(2) : ['about.html','news.html','index.html'];

for (const page of pages) {
  const htmlPath = path.join(ROOT, page);
  let html = fs.readFileSync(htmlPath, 'utf-8');
  // strip external script tags so we control injection
  html = html.replace(/<script[^>]*src=[^>]*><\/script>/g, '');
  const dom = new JSDOM(html, { runScripts: 'outside-only', url: 'http://localhost/' });
  const { window } = dom;
  // inject i18n.js source
  const i18nSrc = fs.readFileSync(path.join(ROOT, 'js', 'i18n.js'), 'utf-8');
  const scriptEl = window.document.createElement('script');
  scriptEl.textContent = i18nSrc;
  window.document.body.appendChild(scriptEl);
  // trigger DOMContentLoaded if needed
  window.document.dispatchEvent(new window.Event('DOMContentLoaded'));

  const navEl = window.document.querySelector('[data-i18n="navHome"]');
  const before = navEl ? navEl.textContent.trim() : '(no navHome el)';
  if (window.StarkI18n) {
    window.StarkI18n.applyLang('zh');
  }
  const after = navEl ? navEl.textContent.trim() : '(no navHome el)';
  const switchHasSelect = window.document.querySelector('.lang-switch select') ? 'select-present' : 'NO-select';
  console.log(`\n=== ${page} ===`);
  console.log('  StarkI18n loaded :', !!window.StarkI18n);
  console.log('  navHome before   :', JSON.stringify(before));
  console.log('  navHome after zh :', JSON.stringify(after));
  console.log('  lang-switch      :', switchHasSelect);
}
