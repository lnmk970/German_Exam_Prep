/* Learn tab: learning only. No timers, no scores that count against you. Every item explains itself. */
(function(){
'use strict';
const $=(s,r)=>(r||document).querySelector(s),$$=(s,r)=>Array.from((r||document).querySelectorAll(s));
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const md=s=>esc(s).replace(/\*\*(.+?)\*\*/g,'<b>$1</b>').replace(/\*(.+?)\*/g,'<i>$1</i>').replace(/\n/g,'<br>');
const LS={get(k,d){try{const v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(e){return d}},set(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}};
const SUB=[['g1','Sprachbausteine 1'],['g2','Sprachbausteine 2'],['fix','Fix the sentence'],['sch','Schreiben phrases'],['spr','Sprechen phrases']];
let bank=null,sub='g1',view=null;
async function load(){if(!bank){const r=await fetch('bank-lernen.json?v=1');if(!r.ok)throw new Error('bank');bank=await r.json()}return bank}
const done=()=>LS.get('pg:learn',{});const mark=(id)=>{const d=done();d[id]=1;LS.set('pg:learn',d)};
function shuffle(a){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
async function render(v){view=v;
 try{await load()}catch(e){v.innerHTML='<div class="card">Could not load the exercises. Please reload the page.</div>';return}
 const d=done();
 v.innerHTML='<div class="ln-note"><b>Learn mode.</b> No timer and no pressure. Tap an answer, read why, and try again as often as you like. All explanations are in English.</div>'
 +'<div class="ln-sub">'+SUB.map(s=>'<button data-s="'+s[0]+'"'+(s[0]===sub?' class="on"':'')+'>'+s[1]+'</button>').join('')+'</div><div id="ln-body"></div>';
 $$('.ln-sub button',v).forEach(b=>b.onclick=()=>{sub=b.dataset.s;render(v)});
 const B=$('#ln-body',v);
 if(sub==='g1')gaps1(B,d);else if(sub==='g2')gaps2(B,d);else if(sub==='fix')fix(B,d);else frames(B,d,sub==='sch'?'schreiben':'sprechen')}
function letter(text,fill){return esc(text).replace(/\{(\d)\}/g,(m,n)=>'<span class="ln-g" id="lg'+n+'">'+(fill&&fill[n]||'('+n+')')+'</span>')}
function gaps1(B,d){
 B.innerHTML='<div class="card"><h2>Sprachbausteine Teil 1</h2><p class="mut" style="margin:0">A personal letter with gaps. Pick a, b or c. In the exam you get 10 gaps; here every gap is explained.</p></div>'
 +bank.gaps1.map((g,gi)=>'<div class="card" data-g="'+g.id+'"><h3>'+esc(g.title)+(d[g.id]?' <span class="ln-tag">done</span>':'')+'</h3><p class="mut">'+esc(g.intro)+'</p><div class="ln-letter">'+letter(g.text)+'</div>'
  +g.gaps.map((x,n)=>'<div class="ln-gc" data-n="'+(n+1)+'"><h4>Gap '+(n+1)+'</h4><div class="ln-o">'+x.o.map((o,oi)=>'<button data-o="'+oi+'">'+'abc'[oi]+') '+esc(o)+'</button>').join('')+'</div><div class="ln-fb" hidden></div></div>').join('')+'</div>').join('');
 bank.gaps1.forEach(g=>{const card=$('[data-g="'+g.id+'"]',B),got={};
  $$('.ln-gc',card).forEach(gc=>{const n=+gc.dataset.n,x=g.gaps[n-1];
   $$('.ln-o button',gc).forEach(bt=>bt.onclick=()=>{const oi=+bt.dataset.o,good=oi===x.ok,fb=$('.ln-fb',gc);
    $$('.ln-o button',gc).forEach(b=>b.classList.remove('ok','no'));bt.classList.add(good?'ok':'no');
    const gp=$('#lg'+n,card);gp.textContent=x.o[oi];gp.className='ln-g '+(good?'ok':'no');
    fb.hidden=false;fb.className='ln-fb'+(good?'':' no');
    fb.innerHTML='<b>'+(good?'Correct':'Not this one')+(good?'':' · try another option')+'</b>'+md(good?x.why:'**'+x.o[oi]+'** does not fit here. Look at the words around the gap, then try again. When you find the right one you will see the full explanation.');
    if(good){got[n]=1;if(Object.keys(got).length===g.gaps.length){mark(g.id);if(!$('.ln-tag',card)){const t=document.createElement('span');t.className='ln-tag';t.textContent='done';$('h3',card).appendChild(t)}}}})})})}
function gaps2(B,d){
 B.innerHTML='<div class="card"><h2>Sprachbausteine Teil 2</h2><p class="mut" style="margin:0">A formal letter and a box of words. Choose one for each gap. Some box words are extra. You see feedback right after each choice.</p></div>'
 +bank.gaps2.map(g=>'<div class="card" data-g="'+g.id+'"><h3>'+esc(g.title)+(d[g.id]?' <span class="ln-tag">done</span>':'')+'</h3><p class="mut">'+esc(g.intro)+'</p><div class="ln-box">'+g.box.map(w=>'<span data-w="'+esc(w)+'">'+esc(w)+'</span>').join('')+'</div><div class="ln-letter">'+letter(g.text)+'</div>'
  +g.gaps.map((x,n)=>'<div class="ln-gc" data-n="'+(n+1)+'"><h4>Gap '+(n+1)+'</h4><select class="ln-sel"><option value="">choose a word</option>'+shuffle(g.box).map(w=>'<option>'+esc(w)+'</option>').join('')+'</select><div class="ln-fb" hidden></div></div>').join('')+'</div>').join('');
 bank.gaps2.forEach(g=>{const card=$('[data-g="'+g.id+'"]',B),got={};
  $$('.ln-gc',card).forEach(gc=>{const n=+gc.dataset.n,x=g.gaps[n-1];
   $('select',gc).onchange=e=>{const w=e.target.value;if(!w)return;const good=w===x.ok,fb=$('.ln-fb',gc),gp=$('#lg'+n,card);
    gp.textContent=w;gp.className='ln-g '+(good?'ok':'no');fb.hidden=false;fb.className='ln-fb'+(good?'':' no');
    fb.innerHTML='<b>'+(good?'Correct':'Not this one')+(good?'':' · try another word')+'</b>'+md(good?x.why:'**'+w+'** does not fit this gap. Read the words before and after it. Think: which word type is missing (preposition, article, conjunction, adverb)?');
    if(good){got[n]=1;if(Object.keys(got).length===g.gaps.length){mark(g.id);if(!$('.ln-tag',card)){const t=document.createElement('span');t.className='ln-tag';t.textContent='done';$('h3',card).appendChild(t)}}}
    $$('.ln-box span',card).forEach(sp=>sp.classList.toggle('used',Object.keys(got).some(k=>g.gaps[k-1].ok===sp.dataset.w)))}})})}
function fix(B,d){
 const items=shuffle(bank.fix);let i=0;
 function show(){const it=items[i];if(!it){B.innerHTML='<div class="card"><h2>All '+items.length+' sentences done</h2><p class="mut">Come back any time for another round in a new order.</p><button class="btn" id="again">Start again</button></div>';$('#again').onclick=()=>fix(B,d);return}
  B.innerHTML='<div class="card"><p class="ln-prog">Sentence '+(i+1)+' of '+items.length+'<span class="ln-tag">'+esc(it.tag)+'</span></p><h3>This sentence has a mistake. Which version is correct?</h3><p style="font-size:1.1rem;margin:6px 0 12px"><b>'+esc(it.wrong)+'</b></p><div class="ln-o" style="flex-direction:column;align-items:stretch">'+shuffle(it.o).map((o,k)=>'<button data-k="'+k+'" style="text-align:left">'+esc(o.t)+'</button>').join('')+'</div><div class="ln-fb" hidden></div><div class="row" style="margin-top:12px"><button class="btn" id="nx" hidden>Next sentence</button></div></div>';
  const ord=$$('.ln-o button',B).map(b=>b.textContent);let solved=false;
  $$('.ln-o button',B).forEach(bt=>bt.onclick=()=>{if(solved)return;const o=it.o.find(x=>x.t===bt.textContent),fb=$('.ln-fb',B);fb.hidden=false;
   if(o.ok){solved=true;bt.classList.add('ok');fb.className='ln-fb';fb.innerHTML='<b>Correct</b>'+md(it.why);$('#nx').hidden=false;mark('fix:'+it.right)}
   else{bt.classList.add('no');bt.disabled=true;fb.className='ln-fb no';fb.innerHTML='<b>Not this one</b>'+md(o.n)}});
  $('#nx').onclick=()=>{i++;show();window.scrollTo(0,0)}}
 show()}
function frames(B,d,sec){
 const list=bank.frames.filter(f=>f.sec===sec);
 B.innerHTML='<div class="card"><h2>'+(sec==='schreiben'?'Schreiben: sentence building blocks':'Sprechen: sentence building blocks')+'</h2><p class="mut" style="margin:0">Learn these frames, then use them in the practice task. Each frame says what it does and why the grammar works. Write or say your own answer first, then open the model.</p></div>'
 +list.map(f=>'<div class="card"><h3>'+esc(f.title)+'</h3><p class="mut">'+esc(f.when)+'</p>'+f.items.map(it=>'<div class="ln-fr"><b>'+esc(it.de)+'</b><p>'+md(it.en)+'</p></div>').join('')
  +'<div class="ln-note" style="margin-top:12px"><b>Practice:</b> '+esc(f.task)+'</div><textarea class="ln-ta" placeholder="Write your answer here (not saved, not scored)"></textarea><div class="row" style="margin-top:8px"><button class="btn ghost sm" data-m>Show a model answer</button></div><div class="ln-model" hidden>'+esc(f.model)+'</div></div>').join('');
 $$('[data-m]',B).forEach(b=>b.onclick=()=>{const m=b.closest('.card').querySelector('.ln-model');m.hidden=!m.hidden;b.textContent=m.hidden?'Show a model answer':'Hide model answer'})}
window.PGLearn={render};
})();
