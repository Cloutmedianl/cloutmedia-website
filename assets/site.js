/* Clout Media · één script voor alle pagina's */
(()=>{
  const d=document,$=s=>d.querySelector(s),$$=s=>[...d.querySelectorAll(s)];
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const root=d.documentElement.dataset.root||'';

  // oude ankerlinks van de one-page site doorsturen
  const old={'#werk':'werk/','#pakketten':'pakketten/','#over':'over/','#faq':'vragen/','#scan':'scan/','#werkwijze':'over/#werkwijze'};
  if(d.body.dataset.page==='home'&&old[location.hash]){location.replace(root+old[location.hash]);return}

  // klaar: start de binnenkomst-animaties
  requestAnimationFrame(()=>requestAnimationFrame(()=>d.body.classList.add('ready')));

  // header wordt glas bij scrollen
  const hdr=$('.hdr');
  const glass=()=>hdr&&hdr.classList.toggle('glass',scrollY>8);
  addEventListener('scroll',glass,{passive:true});glass();

  // mobiel menu
  const sheet=$('#sheet'),burger=$('.burger');
  if(sheet&&burger){
    const close=()=>{sheet.classList.remove('open');sheet.setAttribute('aria-hidden','true');burger.setAttribute('aria-expanded','false');d.body.style.overflow='';burger.focus()};
    burger.addEventListener('click',()=>{sheet.classList.add('open');sheet.setAttribute('aria-hidden','false');burger.setAttribute('aria-expanded','true');d.body.style.overflow='hidden';sheet.querySelector('.x').focus()});
    sheet.querySelector('.x').addEventListener('click',close);
    sheet.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{sheet.classList.remove('open');d.body.style.overflow=''}));
    d.addEventListener('keydown',e=>{if(e.key==='Escape'&&sheet.classList.contains('open'))close()});
  }

  // één keer rustig binnenkomen
  const io=('IntersectionObserver' in window&&!reduce)?new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12,rootMargin:'0px 0px -40px 0px'}):null;
  $$('.rv,.word,.fan').forEach(el=>io?io.observe(el):el.classList.add('in'));

  // hero: telefoon kantelt licht mee met de muis (alleen computer)
  const tilt=$('.tilt'),stage=$('.stage');
  if(tilt&&stage&&!reduce&&matchMedia('(pointer:fine)').matches){
    let raf=0;
    stage.addEventListener('pointermove',e=>{const r=stage.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;cancelAnimationFrame(raf);raf=requestAnimationFrame(()=>{tilt.style.transform=`rotateY(${(x*12).toFixed(2)}deg) rotateX(${(-y*12).toFixed(2)}deg)`})});
    stage.addEventListener('pointerleave',()=>{tilt.style.transform=''});
  }

  // carrousel: slepen + pijlen
  const rail=$('.rail');
  if(rail){
    let down=false,sx=0,sl=0,moved=0;
    rail.addEventListener('pointerdown',e=>{if(e.pointerType!=='mouse')return;down=true;moved=0;sx=e.clientX;sl=rail.scrollLeft});
    addEventListener('pointermove',e=>{if(!down)return;const dx=e.clientX-sx;moved=Math.max(moved,Math.abs(dx));if(moved>4)rail.classList.add('drag');rail.scrollLeft=sl-dx});
    addEventListener('pointerup',()=>{if(!down)return;down=false;rail.classList.remove('drag')});
    rail.addEventListener('click',e=>{if(moved>4){e.preventDefault();e.stopPropagation()}},true);
    const step=()=>(rail.querySelector('.shot')?.offsetWidth||300)+24;
    $('#prev')?.addEventListener('click',()=>rail.scrollBy({left:-step(),behavior:reduce?'auto':'smooth'}));
    $('#next')?.addEventListener('click',()=>rail.scrollBy({left:step(),behavior:reduce?'auto':'smooth'}));
  }

  // lightbox
  const lb=$('#lb');
  if(lb){
    const img=lb.querySelector('img'),cap=lb.querySelector('figcaption');let last=null;
    const close=()=>{lb.classList.remove('open');lb.setAttribute('aria-hidden','true');d.body.style.overflow='';last&&last.focus()};
    $$('[data-big]').forEach(b=>b.addEventListener('click',()=>{last=b;img.src=b.dataset.big;img.alt=b.querySelector('img').alt;cap.textContent=b.dataset.cap+' · Voorbeeldwerk, AI-beeld';lb.classList.add('open');lb.setAttribute('aria-hidden','false');d.body.style.overflow='hidden';lb.querySelector('.x').focus()}));
    lb.querySelector('.x').addEventListener('click',close);
    lb.addEventListener('click',e=>{if(e.target===lb)close()});
    d.addEventListener('keydown',e=>{if(e.key==='Escape'&&lb.classList.contains('open'))close()});
  }

  // voor/na-slider met korte hint
  const ba=$('#ba');
  if(ba){
    const r=ba.querySelector('input'),set=v=>ba.style.setProperty('--pos',v+'%');
    r.addEventListener('input',()=>set(r.value));set(50);
    if(!reduce&&'IntersectionObserver' in window){
      const o=new IntersectionObserver(es=>{if(!es[0].isIntersecting)return;o.disconnect();
        const t0=performance.now(),dur=1400;
        const tick=t=>{const p=Math.min((t-t0)/dur,1),v=50+Math.sin(p*Math.PI*2)*10*(1-p);set(v.toFixed(2));if(p<1)requestAnimationFrame(tick);else set(50)};
        setTimeout(()=>requestAnimationFrame(tick),400);
      },{threshold:.5});o.observe(ba);
    }
  }

  // pakketkiezer
  const pk=$('#picker');
  if(pk){
    const Q=[['Op welke socials wil je actief zijn?',['Instagram/Facebook','Ook TikTok','Weet ik nog niet']],
             ['Wat wil je vooral bereiken?',['Er verzorgd uitzien','Nieuwe klanten bereiken','Overal goed gevonden worden, ook op Google']],
             ['Wat is je budget per maand?',['Tot €150','Tot €250','Tot €400']]];
    const P={start:['Start','€150','Een strakke, verzorgde pagina voor een vaste, lage prijs.'],compleet:['Compleet','€250','Met korte video\'s en TikTok bereik je ook mensen die je nog niet kennen.'],premium:['Premium','€395','Je socials, je Google Bedrijfsprofiel en je website in één hand.']};
    const advise=a=>{const [s,g,b]=a;const bud=[150,250,400][b];
      const fit=(g===2&&bud>=400)?'premium':((s===1||g===1)&&bud>=250)?'compleet':'start';
      const ideal=g===2?'premium':(s===1||g===1)?'compleet':'start';
      return {fit,ideal}};
    window.__cmAdvise=advise;
    let i=0,ans=[];const box=d.createElement('div');box.className='pk';pk.appendChild(box);
    const paint=()=>{
      if(i<Q.length){box.innerHTML=`<p><span class="q">${i+1}/3</span>${i===0?'Twijfel je? ':''}${Q[i][0]}</p>`+Q[i][1].map((t,v)=>`<button type="button" class="pick" data-v="${v}">${t}</button>`).join('');
        box.querySelectorAll('.pick').forEach(btn=>btn.addEventListener('click',()=>{ans.push(+btn.dataset.v);i++;swap()}));}
      else{const {fit,ideal}=advise(ans),f=P[fit],id=P[ideal];
        const txt=fit===ideal?`Ons advies: <b>${f[0]} · ${f[1]}</b>. ${f[2]}`:`Binnen je budget past <b>${f[0]} · ${f[1]}</b>, maar voor wat je wilt bereiken raden we <b>${id[0]} · ${id[1]}</b> aan.`;
        box.innerHTML=`<p data-fit="${fit}" data-ideal="${ideal}">${txt}</p><button type="button" class="again">Opnieuw</button>`;
        box.querySelector('.again').addEventListener('click',()=>{i=0;ans=[];swap()});}
    };
    const swap=()=>{if(reduce){paint();box.querySelector('button')?.focus({preventScroll:true});return}box.classList.add('out');setTimeout(()=>{paint();box.classList.remove('out');box.querySelector('button')?.focus({preventScroll:true})},220)};
    paint();
  }

  // vergelijking: tabbladen op mobiel
  const cmp=$('.cmp');
  if(cmp){const tabs=$$('.tabs [role=tab]');
    tabs.forEach(t=>t.addEventListener('click',()=>{tabs.forEach(x=>x.setAttribute('aria-selected',x===t?'true':'false'));cmp.dataset.on=t.dataset.col;cmp.classList.remove('sw');void cmp.offsetWidth;cmp.classList.add('sw')}));
    $('.tabs')?.addEventListener('keydown',e=>{const k=tabs.findIndex(t=>t.getAttribute('aria-selected')==='true');let n=k;if(e.key==='ArrowRight')n=(k+1)%3;else if(e.key==='ArrowLeft')n=(k+2)%3;else return;tabs[n].click();tabs[n].focus()});
  }

  // vragen: soepel open/dicht, één tegelijk
  $$('.faq details').forEach(dt=>{
    const sm=dt.querySelector('summary'),ans=dt.querySelector('.ans');
    sm.addEventListener('click',e=>{
      e.preventDefault();
      const opening=!dt.open;
      if(opening)$$('.faq details[open]').forEach(o=>{if(o!==dt)shut(o)});
      opening?openIt(dt):shut(dt);
    });
    function openIt(x){const a=x.querySelector('.ans');x.open=true;if(reduce)return;const h=a.scrollHeight;a.style.height='0px';requestAnimationFrame(()=>{a.style.height=h+'px'});a.addEventListener('transitionend',()=>{a.style.height=''},{once:true})}
  });
  function shut(x){const a=x.querySelector('.ans');if(reduce){x.open=false;return}a.style.height=a.scrollHeight+'px';requestAnimationFrame(()=>{a.style.height='0px'});a.addEventListener('transitionend',()=>{x.open=false;a.style.height=''},{once:true})}

  // WhatsApp-knop (computer): pas na de hero, en nooit boven beelden of tekst
  const wa=$('.wa');
  if(wa){
    const hero=$('.hero,.phero'),blockTag=/^(IMG|PICTURE|VIDEO|SVG|PATH|P|H1|H2|H3|H4|LI|A|SPAN|B|STRONG|SMALL|EM|I|BUTTON|TD|TH|LABEL|INPUT|SUMMARY|FIGCAPTION|CAPTION|LEGEND)$/i;
    const hasText=el=>[...el.childNodes].some(n=>n.nodeType===3&&n.data.trim());
    const free=()=>{const r=wa.getBoundingClientRect(),pad=10;
      const pts=[[r.left-pad,r.top-pad],[r.right+pad,r.top-pad],[r.left-pad,r.bottom+pad],[r.right+pad,r.bottom+pad],[(r.left+r.right)/2,(r.top+r.bottom)/2],[r.left-pad,(r.top+r.bottom)/2],[(r.left+r.right)/2,r.top-pad]];
      for(const [x,y] of pts){if(x<0||y<0||x>innerWidth||y>innerHeight)continue;
        for(const el of d.elementsFromPoint(x,y)){if(wa.contains(el))continue;if(blockTag.test(el.tagName)||hasText(el))return false;break}}
      for(const el of $$('.word,.stage,.fan')){const b=el.getBoundingClientRect();if(b.width&&!(b.right<r.left-pad||b.left>r.right+pad||b.bottom<r.top-pad||b.top>r.bottom+pad))return false}
      return true};
    let q=0;const upd=()=>{q=0;if(getComputedStyle(wa).display==='none')return;const past=hero?hero.getBoundingClientRect().bottom<0:scrollY>400;wa.classList.toggle('show',past&&free())};
    const sch=()=>{if(!q)q=requestAnimationFrame(upd)};
    addEventListener('scroll',sch,{passive:true});addEventListener('resize',sch);setTimeout(upd,300);
  }

  // zwevende balk op mobiel: pas na de hero, niet op de scanpagina
  const mbar=$('#mbar');
  if(mbar&&d.body.dataset.page!=='scan'){
    const hero=$('.hero,.phero'),stop=$$('[data-nobar]');
    const upd=()=>{const past=hero?hero.getBoundingClientRect().bottom<0:scrollY>400;const hide=stop.some(s=>{const r=s.getBoundingClientRect();return r.top<innerHeight&&r.bottom>0});mbar.classList.toggle('show',past&&!hide)};
    addEventListener('scroll',upd,{passive:true});upd();
  }else if(mbar)mbar.remove();

  // scanformulier (FormSubmit → cloutmedianl@gmail.com, niet aanpassen)
  const f=$('#form');
  if(f){
    const fields=[...f.querySelectorAll('.field input[required]')];
    const check=inp=>{const fl=inp.closest('.field');const ok=inp.checkValidity()&&inp.value.trim()!=='';fl.classList.toggle('bad',!ok);inp.setAttribute('aria-invalid',!ok);return ok};
    fields.forEach(i=>{i.addEventListener('blur',()=>{if(i.value)check(i)});i.addEventListener('input',()=>{if(i.closest('.field').classList.contains('bad'))check(i)})});
    const cons=$('#ok'),cw=cons.closest('.cfield');
    cons.addEventListener('change',()=>cw.classList.toggle('bad',!cons.checked));
    f.addEventListener('submit',async e=>{
      e.preventDefault();f.classList.remove('fail');
      const bad=fields.filter(i=>!check(i));const cOk=cons.checked;cw.classList.toggle('bad',!cOk);
      if(bad.length){bad[0].focus();return}if(!cOk){cons.focus();return}
      const btn=f.querySelector('button[type=submit]');btn.disabled=true;btn.firstChild.textContent='Bezig met versturen… ';
      try{
        const res=await fetch('https://formsubmit.co/ajax/cloutmedianl@gmail.com',{method:'POST',headers:{'Accept':'application/json'},body:new FormData(f)});
        if(!res.ok)throw 0;
        f.classList.add('sent');f.querySelector('.done h2').focus();
      }catch(_){btn.disabled=false;btn.firstChild.textContent='Vraag mijn gratis scan aan ';f.classList.add('fail')}
    });
  }
})();
