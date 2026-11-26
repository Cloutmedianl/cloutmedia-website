"""Bouwt alle pagina's van de Clout Media-site met dezelfde header en footer.
Gebruik: python3 tools/build.py   (draai vanuit de map van de repository)"""
import os,re
SITE='https://cloutmedianl.github.io/cloutmedia-website/'
OUT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=lambda n:open(os.path.join(OUT,'tools',n),encoding='utf-8').read()

WA='https://wa.me/31636285409'
ARR='<span class="arr" aria-hidden="true">→</span>'
I_WA='<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20l1.3-4A8 8 0 1 1 8 18.7z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>'
I_MAIL='<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="3" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M4 7l8 6 8-6" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>'
I_IG='<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>'
WA_BIG='<svg width="26" height="26" viewBox="0 0 32 32" aria-hidden="true"><path fill="#fff" d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.7c-2 0-3.9-.5-5.6-1.5l-.4-.2-3.9 1 1-3.8-.3-.4A10.7 10.7 0 1 1 16 26.7zm5.9-8c-.3-.2-1.9-1-2.2-1-.3-.1-.5-.2-.7.2l-1 1.2c-.2.2-.4.3-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.6.3-.5c.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.1 1.1-1.1 2.7s1.2 3.2 1.3 3.4c.2.2 2.3 3.5 5.6 4.9 2.8 1.1 3.3.9 3.9.8.6-.1 1.9-.8 2.2-1.5.3-.8.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg>'

MENU=[('home','Home'),('werk','Werk'),('pakketten','Pakketten'),('over','Over'),('vragen','Vragen')]

import hashlib
VER=hashlib.md5((open(os.path.join(OUT,'assets','site.css'),'rb').read()+open(os.path.join(OUT,'assets','site.js'),'rb').read())).hexdigest()[:8]
def head(r,key,title,desc,img='img/og.jpg'):
    url=SITE+('' if key=='home' else (key+'/' if key not in('404',) else '404.html'))
    return f'''<!DOCTYPE html>
<html lang="nl" data-root="{r}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Clout Media">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b0b0c">
<link rel="icon" href="{r}favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{r}assets/icon-32.png">
<link rel="apple-touch-icon" href="{r}assets/icon-180.png">
<link rel="preload" href="{r}assets/fonts/poppins-700.woff" as="font" type="font/woff" crossorigin>
<link rel="preload" href="{r}assets/fonts/inter-400.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="{r}assets/site.css?v={VER}">
'''

def header(r,key):
    href=lambda k:(r or './') if k=='home' else f'{r}{k}/'
    links=''.join(f'<a href="{href(k)}"{" aria-current=\"page\"" if k==key else ""}>{t}</a>' for k,t in MENU)
    return f'''<a class="skip" href="#main">Naar de inhoud</a>
<header class="hdr">
  <div class="wrap nav">
    <a class="logo" href="{r or './'}" aria-label="Clout Media, naar home"><img src="{r}img/logo.png" alt="Clout Media" width="102" height="34"></a>
    <nav class="menu" aria-label="Hoofdmenu">{links}</nav>
    <div class="nav-r">
      <a class="btn btn-main" href="{r}scan/">Gratis scan</a>
      <button class="burger" type="button" aria-label="Menu openen" aria-expanded="false" aria-controls="sheet"><span></span></button>
    </div>
  </div>
</header>
<div class="sheet" id="sheet" aria-hidden="true">
  <div class="nav"><a class="logo" href="{r or './'}" aria-label="Clout Media, naar home"><img src="{r}img/logo.png" alt="Clout Media" width="102" height="34"></a><button class="x" type="button" aria-label="Menu sluiten"><svg width="18" height="18" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18" stroke="#fff" stroke-width="1.8" stroke-linecap="round"/></svg></button></div>
  <nav aria-label="Menu">{links}</nav>
  <a class="btn btn-main" href="{r}scan/">Gratis scan {ARR}</a>
</div>
'''

def footer(r,key,bar=True):
    return f'''<footer class="ftr">
  <div class="wrap">
    <div class="fgrid">
      <div class="fbrand"><img src="{r}img/logo.png" alt="Clout Media" width="108" height="36" loading="lazy"><p>Strakke socials voor lokale ondernemers. Gevestigd in Flevoland, actief in heel Nederland.</p></div>
      <div class="fcol"><h4>Contact</h4><ul>
        <li><a href="{WA}" target="_blank" rel="noopener">{I_WA}06 36 28 54 09</a></li>
        <li><a href="mailto:cloutmedianl@gmail.com">{I_MAIL}cloutmedianl@gmail.com</a></li>
        <li><a href="https://www.instagram.com/cloutmedianl/" target="_blank" rel="noopener">{I_IG}@cloutmedianl</a></li></ul></div>
      <div class="fcol"><h4>Menu</h4><ul>
        <li><a href="{r or './'}">Home</a></li><li><a href="{r}werk/">Werk</a></li><li><a href="{r}pakketten/">Pakketten</a></li><li><a href="{r}over/">Over</a></li><li><a href="{r}vragen/">Vragen</a></li>
        <li><a href="{r}privacy/">Privacyverklaring</a></li><li><a href="{r}voorwaarden/">Algemene voorwaarden</a></li></ul></div>
    </div>
    <!-- KVK: zet hier later "· KvK 12345678" achter Clout Media -->
    <div class="fbot"><span>© 2026 Clout Media</span><span>Social media beheer in Lelystad, Flevoland en heel Nederland</span></div>
  </div>
  <div class="word" aria-hidden="true">clout media</div>
</footer>
{'<div class="mbar" id="mbar"><a class="btn btn-main" href="'+r+'scan/">Gratis scan</a><a class="mw" href="'+WA+'" target="_blank" rel="noopener" aria-label="WhatsApp">'+WA_BIG+'</a></div>' if bar else ''}
<script src="{r}assets/site.js?v={VER}" defer></script>
</body>
</html>
'''

def page(path,key,title,desc,body,bar=True,extra_head=''):
    r='' if path in('index.html','404.html') else '../'
    html=head(r,key,title,desc)+extra_head+f'</head>\n<body data-page="{key}">\n'+header(r,key)+f'<main id="main">\n{body}\n</main>\n'+footer(r,key,bar)
    html=html.replace('{R}',r)
    h,b=html.split('<body',1);html=h+'<body'+b.replace('1-2 werkdagen','<span class="nw">1-2</span> werkdagen')
    if key=='404':html=html.replace('<meta charset="utf-8">\n','<meta charset="utf-8">\n<script>document.write(\'<base href="\'+(location.pathname.indexOf("/cloutmedia-website/")===0?"/cloutmedia-website/":"/")+\'">\')</script>\n',1)
    fp=os.path.join(OUT,path);os.makedirs(os.path.dirname(fp) or OUT,exist_ok=True)
    open(fp,'w',encoding='utf-8').write(html)

def phero(kicker,lines,lead,cls=''):
    l=' '.join(f'<span class="ln"><span>{x}</span></span>' for x in lines)
    return f'''<section class="phero{cls}"><div class="glow" aria-hidden="true"></div><div class="wrap" style="position:relative">
  <span class="kicker fade-up">{kicker}</span><h1 class="reveal mega">{l}</h1><p class="lead fade-up fu1">{lead}</p></div></section>'''

def cta(title_html,lead,alt=False,second=True,extra=''):
    s2=f'<a class="btn btn-ghost" href="{WA}" target="_blank" rel="noopener">Stuur een WhatsApp</a>' if second else ''
    return f'''<section class="cta{' alt' if alt else ''}" data-nobar><div class="glow" aria-hidden="true"></div><div class="wrap rv" style="position:relative">
  <h2>{title_html}</h2><p class="lead">{lead}</p><div class="ctas"><a class="btn btn-main" href="{{R}}scan/">Gratis social media scan {ARR}</a>{s2}</div>{extra}</div></section>'''

SHOTS=[('w2','Lunchroom','Nieuw op de kaart','Voorbeeldpost voor een lunchroom: nieuw op de kaart'),
       ('w5','Sportschool','Reel-cover','Voorbeeld van een reel-cover voor een sportschool'),
       ('w3','Bloemenwinkel','Actiepost','Voorbeeldpost voor een bloemenwinkel'),
       ('w6','Nagelstudio','Nieuwe kleur','Voorbeeldpost voor een nagelstudio'),
       ('w7','Bakker','Vers uit de oven','Voorbeeldpost voor een bakker')]
def shot(w,t,s,alt,lazy=True):
    return f'<button class="shot" type="button" data-big="{{R}}img/{w}-2x.webp" data-cap="{t} · {s.lower()}"><div class="im"><img src="{{R}}img/{w}.webp" srcset="{{R}}img/{w}.webp 540w, {{R}}img/{w}-2x.webp 1080w" sizes="(max-width:700px) 78vw, 340px" alt="{alt}" width="540" height="675"{" loading=\"lazy\"" if lazy else ""}></div><span>{t}</span><small>{s}</small></button>'
LB='<div class="lb" id="lb" aria-hidden="true" role="dialog" aria-label="Voorbeeldpost groot bekijken"><button class="x" type="button" aria-label="Sluiten"><svg width="18" height="18" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18" stroke="#fff" stroke-width="1.8" stroke-linecap="round"/></svg></button><figure><img src="" alt="" width="1080" height="1350"><figcaption></figcaption></figure></div>'

START=['8 posts per maand','Instagram en Facebook','Contentplan, alles ingepland','Vast aanspreekpunt']
COMP=['8 posts per maand','4 Reels/TikToks per maand','Instagram, Facebook en TikTok','Contentplan, alles ingepland','Maandoverzicht van wat werkte','Vast aanspreekpunt']
PREM=['<b>Alles van Compleet</b>','<div>Google Bedrijfsprofiel bijgehouden<small>2 Google-berichten per maand, nieuwe foto\'s, openingstijden en feestdagen up-to-date</small></div>','<div>Website-aanpassingen naar wens<small>Jij vraagt, wij passen aan: teksten, foto\'s, acties en meer.</small></div>','Vast aanspreekpunt']
ul=lambda xs:'<ul class="ul">'+''.join(f'<li>{x}</li>' for x in xs)+'</ul>'

FAQ=[('Wat kost het?','Start kost €150, Compleet €250 en Premium €395 per maand. De scan en de kennismaking zijn gratis.','prijs'),
('Zit ik ergens aan vast?','Nee. Je pakket is maandelijks opzegbaar en stopt aan het eind van de maand waarin je opzegt.','prijs'),
('Wat is het verschil tussen Compleet en Premium?','Premium is alles van Compleet, plus je Google Bedrijfsprofiel en website-aanpassingen naar wens.','prijs'),
('Wat doen jullie met mijn Google Bedrijfsprofiel?','We plaatsen 2 Google-berichten per maand, zetten er nieuwe foto\'s op en houden je openingstijden en feestdagen up-to-date. Zo klopt je informatie als iemand je zaak opzoekt.','prijs'),
('Wat valt onder website-aanpassingen naar wens?','Jij zegt wat er anders moet, wij passen het aan: teksten, foto\'s, openingstijden, acties en mededelingen, een nieuwe sectie of een extra pagina. Grote klussen vallen erbuiten, zoals een nieuwe website of nieuw ontwerp, een webshop, technische problemen, hosting of domein. Daarvoor krijg je vooraf een aparte prijs. Wordt het in een maand duidelijk meer werk dan normaal, dan overleggen we eerst. Dit werkt met websites met een eigen beheeromgeving, zoals WordPress, Wix of Squarespace.','prijs'),
('Wat moet ik zelf doen?','Foto\'s en video\'s maken van je zaak, je werk of je producten, en ze via WhatsApp sturen. Met je telefoon is prima. Wij zeggen precies wat we nodig hebben.',''),
('Ik ben geen fotograaf. Is dat erg?','Nee. Je krijgt simpele tips voor goede telefoonfoto\'s, en wij maken er strakke posts en video\'s van.',''),
('Moet ik mijn wachtwoorden geven?','Nee. Je maakt een eigen account voor Clout Media aan: beheerder in je Google Bedrijfsprofiel en redacteur op je website. Die toegang kun je altijd intrekken.',''),
('Wat krijg ik bij de gratis scan?','We bekijken je socials en sturen je binnen 1-2 werkdagen 3 concrete verbeterpunten. Daarna kies je zelf of je verder wilt.',''),
('Hoe snel zie ik resultaat?','Je pagina ziet er meteen strakker uit. Voor meer bereik is meestal een paar maanden regelmatig posten nodig. Aantallen beloven we niet.',''),
('Voor welke zaken werken jullie?','Voor alle lokale ondernemers: horeca, winkels, beauty, sport, praktijken, groothandels en meer. In heel Nederland.',''),
('Reageren jullie op berichten, reacties en reviews?','Nee, dat zit niet in de pakketten. Het contact met je volgers houd je zelf in de hand. Wil je dat uitbesteden? Vraag naar de mogelijkheden.','')]
def faq(items,id=''):
    return f'<div class="faq"{" id="+chr(34)+id+chr(34) if id else ""}>'+''.join(f'<details><summary>{q}<i aria-hidden="true"></i></summary><div class="ans"><p>{a}</p></div></details>' for q,a,_ in items)+'</div>'
def faq_ld(items):
    import json
    return '<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a,_ in items]},ensure_ascii=False)+'</script>\n'

PROMISES='''<div class="promises rv"><div><b>Maandelijks opzegbaar</b><span>Nooit langer vast dan de lopende maand.</span></div><div><b>Scan binnen 1-2 werkdagen</b><span>Je verbeterpunten snel in je mail.</span></div><div><b>Vaste prijs</b><span>Geen extra kosten achteraf.</span></div></div>'''

SPLIT='''<div class="split">
  <div class="col no rv"><h3>Zonder Clout Media</h3><ul class="list">
    <li>Je staat de hele dag in je zaak.</li>
    <li>Je weet niet wat je moet posten.</li>
    <li>Twee posts, dan een maand niks.</li>
    <li>Je ziet er niets van terug.</li></ul></div>
  <div class="col yes rv d1"><h3>Met Clout Media</h3><ul class="list">
    <li><div>Posts in jouw stijl<span>Met teksten die mensen laten stoppen met scrollen.</span></div></li>
    <li><div>Korte video's<span>Van jouw beelden, met tekst en muziek.</span></div></li>
    <li><div>Elke week iets nieuws<span>Alles ingepland. Jij hoeft niets te onthouden.</span></div></li>
    <li><div>Eén aanspreekpunt<span>Gewoon via WhatsApp.</span></div></li></ul></div>
</div>'''

def steps(long=False):
    S=[('Kennismaken','We bespreken je zaak, je mensen en je stijl. Online of op locatie.',['Vrijblijvend en gratis','We kijken samen naar je socials','Je hoort meteen wat wij anders zouden doen']),
       ('Contentplan','Wij maken een plan voor de maand. Jij stuurt foto\'s en video\'s via WhatsApp.',['Wat we posten en wanneer','Welke beelden we nodig hebben','Tips voor goede telefoonfoto\'s']),
       ('Wij posten','Wij ontwerpen, monteren en plannen alles in. Elke maand kijken we wat beter kan.',['Posts en video\'s in jouw stijl','Alles op tijd online','Bij Compleet en Premium: een maandoverzicht'])]
    return '<div class="steps">'+''.join(f'<div class="step rv{" d"+str(i) if i else ""}"><div class="bn" aria-hidden="true">0{i+1}</div><h3>{t}</h3><p>{p}</p>{"<ul>"+"".join(f"<li>{x}</li>" for x in xs)+"</ul>" if long else ""}</div>' for i,(t,p,xs) in enumerate(S))+'</div>'

def steps_compact():
    S=['Kennismaken','Jij stuurt beelden','Wij posten']
    return '<ol class="strip rv">'+''.join(f'<li><span class="bn" aria-hidden="true">0{i+1}</span><b>{t}</b></li>' for i,t in enumerate(S))+'</ol>'

# ---------------- HOME ----------------
FEED=''.join(f'<img src="img/{w}.webp" alt="" width="540" height="675"{" fetchpriority=\"high\"" if i==0 else ""}>' for i,w in enumerate(['w2','w5','w7','w3','w6','w2','w5','w7','w3','w6']))
def marquee():
    one=''.join(f'<figure class="mq-item"><img src="img/{w}.webp" srcset="img/{w}.webp 540w, img/{w}-2x.webp 1080w" sizes="300px" alt="{alt}" width="540" height="675" loading="lazy"><figcaption>{t}</figcaption></figure>' for w,t,_s,alt in SHOTS)
    two=one.replace('<figure class="mq-item">','<figure class="mq-item" aria-hidden="true">').replace(' alt="Voorbeeld',' alt="" data-x="Voorbeeld')
    return f'<div class="mq" role="region" aria-label="Voorbeeldposts"><div class="mq-track">{one}{two}</div></div>'
STATEMENT='Jij runt je zaak. Wij zorgen dat de rest het ziet.'
home=f'''<section class="hero"><div class="glow" aria-hidden="true"></div>
  <div class="wrap hgrid">
    <div>
      <span class="kicker fade-up">Social media beheer · Heel Nederland</span>
      <h1 class="reveal"><span class="ln"><span>Strak <span class="mint">online.</span></span></span> <span class="ln"><span>Elke week.</span></span></h1>
      <p class="lead fade-up fu1">Jij stuurt foto's via WhatsApp. Wij maken er elke week posts en Reels van.</p>
      <div class="ctas fade-up fu2"><a class="btn btn-ghost" href="pakketten/">Bekijk de pakketten {ARR}</a></div>
    </div>
    <div class="stage" aria-hidden="true"><div class="glow"></div>
      <div class="tilt"><div class="phone"><div class="screen"><div class="ig"><i></i>jouwzaak</div><div class="feed">{FEED}</div></div></div>
        <div class="chip c1"><i><svg width="16" height="16" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="4" fill="none" stroke="#fff" stroke-width="2"/><path d="M10 8.8v6.4l5.4-3.2z" fill="#fff"/></svg></i><span>Nieuwe Reel<small>staat ingepland</small></span></div>
        <div class="chip c2"><i><svg width="16" height="16" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></i><span>Post van deze week<small>klaar en online</small></span></div>
      </div>
    </div>
  </div>
  <a class="scrollhint" href="#main-2" aria-label="Scroll naar beneden"><span></span></a>
</section>

<section class="facts" id="main-2" aria-label="Kernpunten"><div class="wrap"><ul class="factrow rv">
  <li><b>Vanaf €150</b><span>per maand, vaste prijs</span></li>
  <li><b>Maandelijks opzegbaar</b><span>nooit langer vast</span></li>
  <li><b>Scan in 1-2 werkdagen</b><span>gratis en vrijblijvend</span></li></ul></div></section>

<section class="alt mqsec">
  <div class="wrap"><div class="head rv"><span class="kicker">Voorbeeldwerk</span><h2>Content die blijft hangen</h2></div></div>
  {marquee()}
  <div class="wrap railbar mqbar"><p class="tag"><b>Voorbeeldwerk</b> AI-beelden</p><a class="tlink" href="werk/">Bekijk al ons werk {ARR}</a></div>
</section>

<section>
  <div class="wrap">
    <div class="head rv"><span class="kicker">Waarom Clout Media</span><h2>Socials zijn belangrijk. Tijd is schaars.</h2></div>
    {SPLIT}
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="head rv"><span class="kicker">Werkwijze</span><h2>Zo simpel werkt het</h2></div>
    {steps_compact()}
    <div class="more"><a class="tlink" href="over/#werkwijze">Zo werken we {ARR}</a></div>
  </div>
</section>

<section class="statement"><div class="wrap"><p class="st">{' '.join(f'<span class="sw">{w}</span>' for w in STATEMENT.split())}</p></div></section>

{cta('Benieuwd wat er <span class="mint">beter</span> kan?','Vraag de scan aan en ontdek wat je socials nog missen.',alt=True,extra=f'<p class="routeq"><a class="tlink" href="vragen/">Eerst nog een vraag? Bekijk de vragen {ARR}</a></p>')}'''
page('index.html','home','Social media beheer Lelystad &amp; Flevoland | Clout Media','Social media beheer voor lokale ondernemers in Lelystad, Flevoland en heel Nederland. Elke week strakke posts en korte video\'s, vanaf €150 per maand.',home,
     extra_head='<script>(function(){var m={"#werk":"werk/","#pakketten":"pakketten/","#over":"over/","#faq":"vragen/","#scan":"scan/","#werkwijze":"over/#werkwijze"};if(m[location.hash])location.replace(m[location.hash])})()</script>\n<link rel="preload" as="image" href="img/w2.webp" fetchpriority="high">\n<script type="application/ld+json">{"@context":"https://schema.org","@type":"ProfessionalService","name":"Clout Media","description":"Social media beheer voor lokale ondernemers in Lelystad, Flevoland en heel Nederland","url":"'+SITE+'","email":"cloutmedianl@gmail.com","telephone":"+31636285409","areaServed":["Lelystad","Flevoland","Nederland"],"priceRange":"€150 - €395 per maand","sameAs":["https://www.instagram.com/cloutmedianl/"]}</script>\n')

# ---------------- WERK ----------------
werk=phero('Voorbeeldwerk',['Elke zaak een eigen <span class="mint">stijl.</span>'],'Sleep door de posts en klik om ze groot te zien.')+f'''
<section style="padding-top:24px">
  <div class="rail" role="region" aria-label="Voorbeeldposts">{''.join(shot(*x,lazy=(i>1)) for i,x in enumerate(SHOTS))}</div>
  <div class="wrap railbar"><p class="tag"><b>Voorbeeldwerk</b> AI-beelden. Echte cases volgen.</p><div class="arrows"><button type="button" id="prev" aria-label="Vorige posts"><svg width="20" height="20" viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button><button type="button" id="next" aria-label="Volgende posts"><svg width="20" height="20" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button></div></div>
</section>
<section class="alt">
  <div class="wrap">
    <div class="head rv"><span class="kicker">Het verschil</span><h2>Sleep en zie het verschil</h2><p class="lead">Links een gemiddelde feed. Rechts dezelfde zaak met Clout Media.</p></div>
    {P('ba.part').replace('src="img/','src="{R}img/')}
    <div class="under"><p class="tag"><b>Voorbeeld</b> Ter illustratie.</p></div>
  </div>
</section>
{cta('Hoe ziet jouw feed <span class="mint">eruit</span>?','Wij kijken mee en sturen je 3 concrete verbeterpunten.')}
{LB}'''
page('werk/index.html','werk','Voorbeeldwerk | Clout Media','Voorbeeldposts van Clout Media voor een lunchroom, sportschool, bloemenwinkel, nagelstudio en bakker. Elke zaak een eigen stijl.',werk)

# ---------------- PAKKETTEN ----------------
pak=phero('Pakketten',['Heldere prijzen.','Geen <span class="mint">verrassingen.</span>'],'Alle bedragen per maand. Elk pakket is maandelijks opzegbaar.')+f'''
<section style="padding-top:24px">
  <div class="wrap">
    <div class="plans3">
      <article class="card plan hov rv"><div class="phd"><div><h3>Start</h3><p class="for">Voor een verzorgde, strakke pagina.</p></div></div><div class="amt">€150<small>per maand</small></div>{ul(START)}<a class="btn btn-ghost" href="../scan/">Kies Start {ARR}</a></article>
      <article class="card plan top rv d1"><div class="phd"><div><h3>Compleet <span class="badge">Aanrader</span></h3><p class="for">Voor wie ook nieuwe mensen wil bereiken.</p></div></div><div class="amt">€250<small>per maand</small></div>{ul(COMP)}<a class="btn btn-dark" href="../scan/">Kies Compleet {ARR}</a></article>
      <article class="card plan prem hov rv d2"><div class="phd"><div><h3>Premium <span class="badge line">Met Google &amp; website</span></h3><p class="for">Voor wie overal goed gevonden wil worden.</p></div></div><div class="amt">€395<small>per maand</small></div>{ul(PREM)}<a class="btn btn-ghost" href="../scan/">Kies Premium {ARR}</a></article>
    </div>
    <div class="card picker rv" id="picker" aria-live="polite"></div>
  </div>
</section>
<section class="alt">
  <div class="wrap">
    <div class="head rv"><span class="kicker">Vergelijk</span><h2>Alles naast elkaar</h2></div>
    <div class="cmpwrap rv"><div class="tabs" role="tablist" aria-label="Kies een pakket"><button type="button" role="tab" data-col="1" aria-selected="false">Start</button><button type="button" role="tab" data-col="2" aria-selected="true">Compleet</button><button type="button" role="tab" data-col="3" aria-selected="false">Premium</button></div><table class="cmp" data-on="2"><caption class="sr">Vergelijking van de drie pakketten</caption><thead><tr><th scope="col"><span class="sr">Onderdeel</span></th><th scope="col" class="k1">Start</th><th scope="col" class="k2">Compleet</th><th scope="col" class="k3">Premium</th></tr></thead><tbody><tr><th scope="row">Prijs per maand</th><td class="k1">€150</td><td class="k2">€250</td><td class="k3">€395</td></tr><tr><th scope="row">Posts per maand</th><td class="k1">8</td><td class="k2">8</td><td class="k3">8</td></tr><tr><th scope="row">Reels/TikToks per maand</th><td class="k1"><span class="no" aria-label="Nee">—</span></td><td class="k2">4</td><td class="k3">4</td></tr><tr><th scope="row">Platforms</th><td class="k1">Instagram, Facebook</td><td class="k2">Instagram, Facebook, TikTok</td><td class="k3">Instagram, Facebook, TikTok</td></tr><tr><th scope="row">Contentplan en alles ingepland</th><td class="k1"><svg width="20" height="20" viewBox="0 0 20 20" aria-label="Ja" role="img"><circle cx="10" cy="10" r="10" fill="#fff"/><path d="M5.8 10.3l2.8 2.7 5.6-5.9" fill="none" stroke="#0b0b0c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></td><td class="k2"><svg width="20" height="20" viewBox="0 0 20 20" aria-label="Ja" role="img"><circle cx="10" cy="10" r="10" fill="#fff"/><path d="M5.8 10.3l2.8 2.7 5.6-5.9" fill="none" stroke="#0b0b0c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></td><td class="k3"><svg width="20" height="20" viewBox="0 0 20 20" aria-label="Ja" role="img"><circle cx="10" cy="10" r="10" fill="#fff"/><path d="M5.8 10.3l2.8 2.7 5.6-5.9" fill="none" stroke="#0b0b0c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></td></tr><tr><th scope="row">Maandoverzicht van wat werkte</th><td class="k1"><span class="no" aria-label="Nee">—</span></td><td class="k2"><svg width="20" height="20" viewBox="0 0 20 20" aria-label="Ja" role="img"><circle cx="10" cy="10" r="10" fill="#fff"/><path d="M5.8 10.3l2.8 2.7 5.6-5.9" fill="none" stroke="#0b0b0c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></td><td class="k3"><svg width="20" height="20" viewBox="0 0 20 20" aria-label="Ja" role="img"><circle cx="10" cy="10" r="10" fill="#fff"/><path d="M5.8 10.3l2.8 2.7 5.6-5.9" fill="none" stroke="#0b0b0c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></td></tr><tr><th scope="row">Google Bedrijfsprofiel</th><td class="k1"><span class="no" aria-label="Nee">—</span></td><td class="k2"><span class="no" aria-label="Nee">—</span></td><td class="k3"><svg width="20" height="20" viewBox="0 0 20 20" aria-label="Ja" role="img"><circle cx="10" cy="10" r="10" fill="#fff"/><path d="M5.8 10.3l2.8 2.7 5.6-5.9" fill="none" stroke="#0b0b0c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></td></tr><tr><th scope="row">Website-aanpassingen</th><td class="k1"><span class="no" aria-label="Nee">—</span></td><td class="k2"><span class="no" aria-label="Nee">—</span></td><td class="k3">Naar wens</td></tr><tr><th scope="row">Vast aanspreekpunt</th><td class="k1"><svg width="20" height="20" viewBox="0 0 20 20" aria-label="Ja" role="img"><circle cx="10" cy="10" r="10" fill="#fff"/><path d="M5.8 10.3l2.8 2.7 5.6-5.9" fill="none" stroke="#0b0b0c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></td><td class="k2"><svg width="20" height="20" viewBox="0 0 20 20" aria-label="Ja" role="img"><circle cx="10" cy="10" r="10" fill="#fff"/><path d="M5.8 10.3l2.8 2.7 5.6-5.9" fill="none" stroke="#0b0b0c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></td><td class="k3"><svg width="20" height="20" viewBox="0 0 20 20" aria-label="Ja" role="img"><circle cx="10" cy="10" r="10" fill="#fff"/><path d="M5.8 10.3l2.8 2.7 5.6-5.9" fill="none" stroke="#0b0b0c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></td></tr><tr><th scope="row">Maandelijks opzegbaar</th><td class="k1"><svg width="20" height="20" viewBox="0 0 20 20" aria-label="Ja" role="img"><circle cx="10" cy="10" r="10" fill="#fff"/><path d="M5.8 10.3l2.8 2.7 5.6-5.9" fill="none" stroke="#0b0b0c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></td><td class="k2"><svg width="20" height="20" viewBox="0 0 20 20" aria-label="Ja" role="img"><circle cx="10" cy="10" r="10" fill="#fff"/><path d="M5.8 10.3l2.8 2.7 5.6-5.9" fill="none" stroke="#0b0b0c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></td><td class="k3"><svg width="20" height="20" viewBox="0 0 20 20" aria-label="Ja" role="img"><circle cx="10" cy="10" r="10" fill="#fff"/><path d="M5.8 10.3l2.8 2.7 5.6-5.9" fill="none" stroke="#0b0b0c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></td></tr></tbody></table></div>
    <p class="fine rv">Niet inbegrepen: advertenties, reageren op berichten en reviews, filmen of fotograferen op locatie en een nieuwe website. Ter vergelijking: een bureau vraagt vaak €500 tot €1.500 per maand.</p>
    <p class="routeq rv"><a class="tlink" href="../vragen/#prijs">Nog vragen over prijzen of pakketten? {ARR}</a></p>
  </div>
</section>
{cta('Twijfel je <span class="mint">nog</span>?','Begin met de scan. Daarna adviseren we eerlijk welk pakket past.')}'''
page('pakketten/index.html','pakketten','Pakketten en prijzen | Clout Media','Drie pakketten: Start €150 (8 posts), Compleet €250 (8 posts en 4 Reels/TikToks) en Premium €395 met Google Bedrijfsprofiel en website-aanpassingen. Maandelijks opzegbaar.',pak)

# ---------------- OVER ----------------
# FOTO van Luca: zet hier het pad, bijv. 'img/luca.webp' (staand, ca. 1600x2000), en draai de build.
# Zolang dit leeg is, staat er geen foto en geen vervanging op de pagina.
FOTO=''
FOTO_HTML=(f'<figure class="portrait rv"><img src="../{FOTO}" alt="Luca, oprichter van Clout Media" width="800" height="1000" loading="lazy"></figure>' if FOTO else '')
FOTO_COMMENT='<!-- FOTO: plek staat klaar. Zet in tools/build.py FOTO = "img/luca.webp" en draai de build. -->'
over=phero('Over Clout Media',['Fris bureau.','Vaste <span class="mint">basis.</span>'],'Wie er achter Clout Media zit en hoe we werken.')+f'''
<section style="padding-top:24px">
  <div class="wrap">
    {FOTO_COMMENT}
    <div class="about{' has-foto' if FOTO else ''}">
      <div class="rv"><p class="quote">"Ik ben opgegroeid met social media. Ik weet hoe je <span class="mint">opvalt in een feed</span>, en dat wil ik voor jouw zaak doen."</p>
        <div class="sign"><div><b>Luca</b><small>Oprichter van Clout Media</small></div></div></div>
      <div class="side2">{FOTO_HTML}<div class="txt rv d1"><p>Ik ben student Handel &amp; Ondernemen. Veel goede lokale zaken zijn online bijna onzichtbaar, terwijl de buurt de hele dag op de telefoon zit.</p>
        <p>Achter de schermen kijkt een ervaren adviseur in ondernemen en bedrijfsprocessen met me mee.</p></div></div>
    </div>
  </div>
</section>
<section class="alt" id="werkwijze">
  <div class="wrap"><div class="head rv"><span class="kicker">Werkwijze</span><h2>Hoe we samenwerken</h2></div>{steps(True)}</div>
</section>
<section>
  <div class="wrap"><div class="head rv" style="margin-bottom:0"><span class="kicker">Onze beloftes</span><h2>Dit kun je verwachten</h2></div>{PROMISES}</div>
</section>
{cta('Zullen we <span class="mint">kennismaken</span>?','Online of op locatie, wanneer het jou uitkomt.',alt=True)}'''
page('over/index.html','over','Over ons | Clout Media','Clout Media is opgericht door Luca, student Handel &amp; Ondernemen uit Flevoland, met een ervaren adviseur achter de schermen. Lees hoe we werken.',over)

# ---------------- VRAGEN ----------------
FQ1=[x for x in FAQ if x[2]=='prijs'];FQ2=[x for x in FAQ if x[2]!='prijs']
vr=phero('Veelgestelde vragen',['Goed om te <span class="mint">weten.</span>'],'Staat je vraag er niet tussen? Stuur ons een bericht.')+f'''
<section style="padding-top:24px"><div class="wrap">
  <h2 class="fqh rv" id="prijs">Prijzen en pakketten</h2>{faq(FQ1)}
  <h2 class="fqh rv">Samenwerken</h2>{faq(FQ2)}
</div></section>
{cta('Nog een <span class="mint">vraag</span>?','Stuur ons een WhatsApp, of begin met de scan.',alt=True)}'''
page('vragen/index.html','vragen','Veelgestelde vragen | Clout Media','Antwoorden over social media beheer bij Clout Media: prijzen, pakketten, wat je zelf doet en wat je kunt verwachten.',vr,extra_head=faq_ld(FAQ))

# ---------------- SCAN ----------------
scan=f'''<section class="phero" style="text-align:left;padding-bottom:clamp(80px,10vw,136px)"><div class="glow" aria-hidden="true" style="left:0;margin-left:-300px"></div>
  <div class="wrap sgrid" style="position:relative">
    <div class="copy">
      <span class="kicker fade-up">Gratis social media scan</span>
      <h1 class="reveal mega" style="margin:0;max-width:14ch"><span class="ln"><span>Ontdek wat er beter kan aan je <span class="mint">socials.</span></span></span></h1>
      <p class="lead fade-up fu1">We bekijken je pagina en sturen je binnen 1-2 werkdagen 3 concrete verbeterpunten.</p>
      <ul class="points fade-up fu2"><li>Hoe je feed overkomt op iemand die je voor het eerst ziet</li><li>Punten die je meteen kunt toepassen</li><li>Daarna een kennismaking, als jij dat wilt</li></ul>
      <div class="contact fade-up fu3">
        <a class="card hov" href="{WA}" target="_blank" rel="noopener">{I_WA}<span><small>WhatsApp of bellen</small><strong>06 36 28 54 09</strong></span></a>
        <a class="card hov" href="mailto:cloutmedianl@gmail.com">{I_MAIL}<span><small>Liever mailen?</small><strong>cloutmedianl@gmail.com</strong></span></a>
        <a class="card hov" href="https://www.instagram.com/cloutmedianl/" target="_blank" rel="noopener">{I_IG}<span><small>Instagram</small><strong>@cloutmedianl</strong></span></a>
      </div>
    </div>
    <form class="form fade-up fu2" id="form" novalidate>
      <h2>Vraag je gratis scan aan</h2>
      <p class="sub">Invullen duurt 1 minuut.</p>
      <input type="hidden" name="_subject" value="Nieuwe aanvraag gratis scan via cloutmedia.nl">
      <input type="hidden" name="_template" value="table">
      <input type="hidden" name="_captcha" value="false">
      <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">
      <div class="row2">
        <div class="field"><label for="f1">Je naam</label><input id="f1" name="Naam" autocomplete="name" required aria-describedby="e1"><p class="err" id="e1">Vul je naam in.</p></div>
        <div class="field"><label for="f2">Bedrijfsnaam</label><input id="f2" name="Bedrijf" autocomplete="organization" required aria-describedby="e2"><p class="err" id="e2">Vul de naam van je bedrijf in.</p></div>
      </div>
      <div class="row2">
        <div class="field"><label for="f3">Plaats</label><input id="f3" name="Plaats" autocomplete="address-level2" placeholder="Bijv. Lelystad" required aria-describedby="e3"><p class="err" id="e3">Vul je plaats in.</p></div>
        <div class="field"><label for="f4">E-mail</label><input id="f4" name="E-mail" type="email" autocomplete="email" required aria-describedby="e4"><p class="err" id="e4">Vul een geldig e-mailadres in.</p></div>
      </div>
      <div class="field"><label for="f5">Link naar je social media</label><input id="f5" name="Social link" placeholder="Bijv. instagram.com/jouwzaak" required aria-describedby="h5 e5"><p class="hint" id="h5">Nog geen pagina? Vul dan "geen" in.</p><p class="err" id="e5">Vul een link in, of "geen".</p></div>
      <fieldset class="field"><legend>Hoe wil je daarna kennismaken?</legend><div class="seg">
        <label><input type="radio" name="Afspraak" value="Online" checked> Online</label>
        <label><input type="radio" name="Afspraak" value="Op locatie"> Op locatie</label>
        <label><input type="radio" name="Afspraak" value="Alleen de scan"> Alleen de scan</label></div></fieldset>
      <div class="cfield"><label class="consent"><input type="checkbox" id="ok" required> <span>Ik ga akkoord met de <a href="../privacy/" target="_blank">privacyverklaring</a>. Mijn gegevens worden alleen gebruikt voor de scan en om contact met mij op te nemen.</span></label></div>
      <p class="failmsg" role="alert">Versturen lukte niet. Stuur ons een WhatsApp op <a href="{WA}">06 36 28 54 09</a> of mail naar cloutmedianl@gmail.com.</p>
      <button class="btn btn-dark" type="submit">Vraag mijn gratis scan aan {ARR}</button>
      <div class="done" role="status"><div class="ok" aria-hidden="true"><svg width="28" height="28" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="#b8f5d0" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></div><h2 tabindex="-1">Bedankt, je aanvraag is binnen</h2><p>Je krijgt je scan binnen 1-2 werkdagen. Heb je in de tussentijd een vraag? Stuur ons gerust een WhatsApp.</p></div>
    </form>
  </div>
</section>'''
page('scan/index.html','scan','Gratis social media scan | Clout Media','Vraag een gratis social media scan aan. Binnen 1-2 werkdagen krijg je 3 concrete verbeterpunten voor je socials. Gratis en vrijblijvend.',scan,bar=False)

# ---------------- JURIDISCH ----------------
def legal(path,key,title,h1,lead,part,desc):
    t=P(part)
    t=re.sub(r'<p>(Laatst bijgewerkt[^<]*|Clout Media · Versie[^<]*)(<!--.*?-->)?</p>',lambda m:f'<p class="meta">{m.group(1)}</p>'+(m.group(2) or ''),t,count=1)
    t=t.replace('<h3>','<h2>').replace('</h3>','</h2>')
    body=phero(key.capitalize() if key!='voorwaarden' else 'Voorwaarden',[h1],lead)+f'<section style="padding-top:24px"><div class="wrap"><article class="prose">{t}</article></div></section>'
    page(path,key,title,desc,body)
legal('privacy/index.html','privacy','Privacyverklaring | Clout Media','Privacyverklaring','Welke gegevens we verzamelen, waarom, en wat je rechten zijn.','privacy.part','Privacyverklaring van Clout Media: welke gegevens we verwerken, waarom, hoe lang en wat je rechten zijn.')
legal('voorwaarden/index.html','voorwaarden','Algemene voorwaarden | Clout Media','Algemene voorwaarden','De afspraken die gelden voor onze offertes, opdrachten en diensten.','voorwaarden.part','Algemene voorwaarden van Clout Media voor offertes, opdrachten en social media diensten.')

# ---------------- 404 ----------------
nf=f'''<section class="nf"><div class="wrap"><div class="big" aria-hidden="true">404</div><h1 style="font-size:clamp(32px,4.4vw,52px);margin-top:12px">Deze pagina bestaat niet</h1><p class="lead" style="margin-left:auto;margin-right:auto">Misschien is de link veranderd. Ga terug naar home, of vraag meteen je gratis scan aan.</p><div class="ctas" style="justify-content:center"><a class="btn btn-main" href="./">Naar home {ARR}</a><a class="btn btn-ghost" href="scan/">Gratis scan</a></div></div></section>'''
page('404.html','404','Pagina niet gevonden | Clout Media','Deze pagina bestaat niet. Ga terug naar de homepage van Clout Media.',nf,
     extra_head='<meta name="robots" content="noindex">\n')

# ---------------- sitemap + robots ----------------
urls=['','werk/','pakketten/','over/','vragen/','scan/','privacy/','voorwaarden/']
open(os.path.join(OUT,'sitemap.xml'),'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{SITE}{u}</loc><lastmod>2026-11-19</lastmod></url>\n' for u in urls)+'</urlset>\n')
open(os.path.join(OUT,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\nDisallow: /site/\nDisallow: /nieuw/\nDisallow: /screenshots/\nDisallow: /tools/\n\nSitemap: {SITE}sitemap.xml\n')
print('klaar')
