const fs=require('fs');
const {JSDOM}=require('C://Users//Administrator//.workbuddy//binaries//node//workspace//node_modules//jsdom');
const ROOT='C://Users//Administrator//WorkBuddy//2026-08-12-16-19-26//stark-steel-fresh';
const page=process.argv[2]||'about.html';
let html=fs.readFileSync(ROOT+'/'+page,'utf-8')
  .replace(/<script[^>]*src=["']js\/script\.js["'][^>]*><\/script>/g,'');
const dom=new JSDOM(html,{runScripts:'dangerously',url:'http://localhost/',pretendToBeVisual:true,resources:'usable'});
const {window}=dom;
const i18n=fs.readFileSync(ROOT+'/js/i18n.js','utf-8');
const s=window.document.createElement('script'); s.textContent=i18n; window.document.body.appendChild(s);
window.document.dispatchEvent(new window.Event('DOMContentLoaded'));
setTimeout(()=>{
  const sel=window.document.querySelector('select.lang-select');
  const lead=window.document.querySelector('[data-i18n=aboutLead1]');
  console.log('select exists:', !!sel, '| lead exists:', !!lead);
  console.log('BEFORE switch, lead en:', lead? JSON.stringify(lead.textContent.trim().slice(0,40)) : 'n/a');
  if(sel){
    sel.value='zh';
    sel.dispatchEvent(new window.Event('change'));
    console.log('AFTER switch zh, lead zh:', lead? JSON.stringify(lead.textContent.trim().slice(0,40)) : 'n/a');
  }
  process.exit(0);
},300);
