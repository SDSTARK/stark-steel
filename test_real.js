const fs = require('fs');
const { JSDOM, VirtualConsole } = require('C:\\Users\\Administrator\\.workbuddy\\binaries\\node\\workspace\\node_modules\\jsdom');
const ROOT = 'C:\\Users\\Administrator\\WorkBuddy\\2026-08-12-16-19-26\\stark-steel-fresh';

const stub = 'window.setInterval=function(){return 0;};window.clearInterval=function(){};';
const scriptJs = fs.readFileSync(ROOT + '/js/script.js', 'utf-8');
const i18nJs = fs.readFileSync(ROOT + '/js/i18n.js', 'utf-8');

function test(page) {
  let html = fs.readFileSync(ROOT + '/' + page, 'utf-8');
  html = html.replace(/<script[^>]*src=[^>]*><\/script>/g, '');
  html = html.replace('</body>', '<script>' + stub + '</script><script>' + scriptJs + '</script><script>' + i18nJs + '</script></body>');

  const vc = new VirtualConsole();
  const errors = [];
  vc.on('jsdomError', e => errors.push('jsdomError: ' + (e.message || e)));
  vc.on('error', (...a) => errors.push('error: ' + a.join(' ')));

  const dom = new JSDOM(html, { runScripts: 'dangerously', url: 'http://localhost/', virtualConsole: vc });
  const { window } = dom;
  window.addEventListener('error', e => errors.push('window.error: ' + (e.error ? e.error.stack : e.message)));
  window.document.dispatchEvent(new window.Event('DOMContentLoaded'));

  const doc = window.document;
  const sel = doc.querySelector('select.lang-select');
  const navHome = doc.querySelector('[data-i18n="navHome"]');
  const before = navHome ? navHome.textContent.trim() : '(no navHome)';
  let err2 = null;
  try {
    if (sel) { sel.value = 'zh'; sel.dispatchEvent(new window.Event('change')); }
    else if (window.StarkI18n) { window.StarkI18n.applyLang('zh'); }
  } catch (e) { err2 = e.stack; }
  const after = navHome ? navHome.textContent.trim() : '(no navHome)';
  console.log('=== ' + page + ' ===');
  console.log('  lang-select rendered:', !!sel);
  console.log('  navHome before:', JSON.stringify(before), '-> after zh:', JSON.stringify(after));
  console.log('  switch worked:', after === '首页' || before !== after);
  if (errors.length) console.log('  JS ERRORS:', errors.slice(0, 4).join(' | '));
  if (err2) console.log('  switch threw:', err2.split('\n').slice(0, 3).join(' | '));
}

for (const p of ['about.html', 'index.html', 'news.html', 'contact.html']) test(p);
process.exit(0);
