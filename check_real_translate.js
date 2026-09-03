// Load a page with BOTH scripts, simulate real browser, switch language, verify body text translates.
const fs = require('fs');
const { JSDOM } = require('C:\\Users\\Administrator\\.workbuddy\\binaries\\node\\workspace\\node_modules\\jsdom');
const ROOT = 'C:\\Users\\Administrator\\WorkBuddy\\2026-08-12-16-19-26\\stark-steel-fresh';
const page = process.argv[2] || 'about.html';

let html = fs.readFileSync(ROOT + '/' + page, 'utf-8');
// strip external script srcs (we inject i18n.js manually; skip script.js timers)
html = html.replace(/<script[^>]*src="js\/script\.js"[^>]*><\/script>/g, '');
html = html.replace(/<script[^>]*src="js\/i18n\.js"[^>]*><\/script>/g, '');
const dom = new JSDOM(html, { runScripts: 'dangerously', url: 'http://localhost/', pretendToBeVisual: true });
const { window } = dom;
global.window = window; global.document = window.document;
window.requestAnimationFrame = (cb) => setTimeout(cb, 0);

function inject(file) {
  const s = window.document.createElement('script');
  s.textContent = fs.readFileSync(ROOT + '/' + file, 'utf-8');
  window.document.body.appendChild(s);
}
inject('js/i18n.js');

// find a body content key to inspect
function readKey(k) {
  const el = window.document.querySelector('[data-i18n="' + k + '"]');
  return el ? el.textContent.trim() : '(no element)';
}

const probe = ['aboutWho1', 'aboutLead1', 'aboutStatsTitle', 'contactLocAddr', 'newsLatestTitle', 'indexAdv1'];
console.log('PAGE:', page);
for (const lg of ['en', 'zh', 'es', 'ar']) {
  try { window.StarkI18n.applyLang(lg); } catch (e) { console.log('applyLang err', lg, e.message); }
  const vals = probe.filter(k => window.document.querySelector('[data-i18n="' + k + '"]')).map(k => readKey(k).slice(0, 28));
  console.log('  ' + lg + ': ' + JSON.stringify(vals));
}
process.exit(0);
