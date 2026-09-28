"""Génère la section anglaise /en/ de seggfaye.com (phase 1). Lancer depuis la racine du site."""
import json, os, re, subprocess, urllib.parse

SITE = "https://seggfaye.com"
WA = "33652650395"
DATE = "2026-09-28T12:00:00+02:00"
AUTHOR = {"@type": "Person", "name": "Lamine Faye", "url": SITE + "/le-guedjologue.html",
          "jobTitle": "Guedjologue", "sameAs": ["https://www.tiktok.com/@seggfaye"]}
PUBLISHER = {"@type": "Organization", "name": "Louma by Seggfaye", "url": SITE,
             "logo": {"@type": "ImageObject", "url": SITE + "/logosite.webp"}}


def wa(text):
    return f"https://wa.me/{WA}?text=" + urllib.parse.quote(text)


CSS = """
@font-face{font-family:'Playfair Display';font-style:italic;font-weight:700;font-display:swap;src:url(/fonts/playfair-italic-700.woff) format('woff')}
@font-face{font-family:'Playfair Display';font-style:normal;font-weight:700;font-display:swap;src:url(/fonts/playfair-normal.woff2) format('woff2')}
@font-face{font-family:'Playfair Display';font-style:normal;font-weight:900;font-display:swap;src:url(/fonts/playfair-normal.woff2) format('woff2')}
@font-face{font-family:'Plus Jakarta Sans';font-style:normal;font-weight:400;font-display:swap;src:url(/fonts/jakarta.woff2) format('woff2')}
@font-face{font-family:'Plus Jakarta Sans';font-style:normal;font-weight:500;font-display:swap;src:url(/fonts/jakarta.woff2) format('woff2')}
@font-face{font-family:'Plus Jakarta Sans';font-style:normal;font-weight:600;font-display:swap;src:url(/fonts/jakarta.woff2) format('woff2')}
@font-face{font-family:'Plus Jakarta Sans';font-style:normal;font-weight:700;font-display:swap;src:url(/fonts/jakarta.woff2) format('woff2')}
@font-face{font-family:'Plus Jakarta Sans';font-style:normal;font-weight:800;font-display:swap;src:url(/fonts/jakarta.woff2) format('woff2')}
:root{--bg:#100d08;--bg-2:#161210;--card:#1a1612;--gold:#c9a84c;--cream:#f1e8d8;--muted:#8a7e6a;--border:rgba(201,168,76,.12);--border-hi:rgba(201,168,76,.35)}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Plus Jakarta Sans',system-ui,sans-serif;background:var(--bg);color:var(--cream);line-height:1.8}
a{color:var(--gold);text-decoration:none}a:hover{text-decoration:underline}
.topbar{display:flex;justify-content:space-between;align-items:center;gap:1rem;flex-wrap:wrap;max-width:1100px;margin:0 auto;padding:1rem 1.5rem;border-bottom:1px solid var(--border)}
.topbar .brand{font-family:'Playfair Display',serif;font-weight:900;font-size:1.15rem;color:var(--cream)}
.topbar nav{display:flex;gap:1.1rem;flex-wrap:wrap;font-size:.85rem}
.topbar nav a{color:var(--cream)}.topbar nav a.lang{color:var(--gold);font-weight:700}
.breadcrumb{padding:1rem 1.5rem;font-size:.8rem;color:var(--muted);max-width:760px;margin:0 auto}
.breadcrumb a{color:var(--muted)}.breadcrumb span{color:var(--gold)}
article,.wrap{max-width:760px;margin:0 auto;padding:0 1.5rem 4rem}
.wide{max-width:1100px}
.article-header{margin-bottom:2.5rem}
.article-cat{font-size:.7rem;font-weight:700;letter-spacing:.25em;text-transform:uppercase;color:var(--gold);margin-bottom:.8rem}
h1{font-family:'Playfair Display',serif;font-size:2.4rem;font-weight:900;line-height:1.15;color:var(--cream);margin-bottom:1rem}
@media(max-width:600px){h1{font-size:1.8rem}}
.article-meta{font-size:.8rem;color:var(--muted);display:flex;gap:1.5rem;flex-wrap:wrap}
.article-meta strong{color:var(--cream);font-weight:600}
h2{font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:700;color:var(--cream);margin:2.5rem 0 1rem;padding-top:1.5rem;border-top:1px solid var(--border)}
h3{font-family:'Playfair Display',serif;color:var(--gold);font-size:1.15rem;margin:1.2rem 0 .5rem}
p,li{color:var(--muted);font-size:.95rem}p{margin-bottom:1.2rem}
ul,ol{margin:0 0 1.2rem 1.3rem}li{margin-bottom:.35rem}
strong{color:var(--cream)}
.highlight-box{background:rgba(201,168,76,.08);border:1px solid rgba(201,168,76,.25);border-radius:.8rem;padding:1.2rem 1.5rem;margin:1.5rem 0}
.highlight-box p{color:var(--cream);margin-bottom:0}
.hero-img{width:100%;max-height:430px;object-fit:cover;border-radius:.8rem;margin-bottom:1.5rem}
.btn{display:inline-block;background:var(--gold);color:#100d08;font-weight:700;padding:.7rem 1.3rem;border-radius:2rem;margin:.3rem .4rem .3rem 0}
.btn:hover{text-decoration:none;opacity:.9}
.btn.ghost{background:transparent;color:var(--gold);border:1px solid var(--border-hi)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:1rem;margin:1.2rem 0 2rem}
.card{background:var(--card);border:1px solid var(--border);border-radius:.8rem;overflow:hidden;display:flex;flex-direction:column}
.card img{width:100%;height:170px;object-fit:cover}
.card .body{padding:1rem 1.1rem;display:flex;flex-direction:column;gap:.35rem;flex:1}
.card h3{margin:0;font-size:1.05rem}
.card .local{font-size:.75rem;color:var(--muted);letter-spacing:.05em}
.card .price{color:var(--cream);font-weight:700}
.card p{font-size:.85rem;margin:0;flex:1}
.card .actions{display:flex;gap:.8rem;flex-wrap:wrap;font-size:.82rem;margin-top:.4rem}
.faq{margin:2rem 0}.faq details{border-bottom:1px solid var(--border);padding:1rem 0}
.faq summary{cursor:pointer;font-weight:600;color:var(--cream);font-size:.95rem;list-style:none}
.faq summary::before{content:'+ ';color:var(--gold);font-weight:700}.faq details[open] summary::before{content:'- '}
.faq details p{margin-top:.6rem;font-size:.9rem}
footer{text-align:center;padding:2rem;font-size:.75rem;color:var(--muted);border-top:1px solid var(--border)}
"""

GTAG = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-D32329HF3X"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-D32329HF3X');
document.addEventListener('click', function(e){
  var a = e.target.closest ? e.target.closest('a[href]') : null;
  if(!a) return;
  var h = a.href || '';
  if(h.indexOf('wa.me') > -1){ gtag('event', 'whatsapp_click', {'link_url': h, 'page_path': location.pathname}); }
});
</script>"""


def page(path, fr, title, desc, image, body, schemas, og_type="article"):
    url = SITE + path
    alt = ""
    if fr:
        alt = (f'<link rel="alternate" hreflang="en" href="{url}">\n'
               f'<link rel="alternate" hreflang="fr" href="{SITE}{fr}">\n'
               f'<link rel="alternate" hreflang="x-default" href="{SITE}{fr}">\n')
    lang_link = fr or "/"
    ld = "\n".join(f'<script type="application/ld+json">\n{json.dumps(s, ensure_ascii=False, indent=2)}\n</script>' for s in schemas)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{GTAG}
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preload" href="/fonts/jakarta.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/playfair-normal.woff2" as="font" type="font/woff2" crossorigin>
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
{alt}<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/{image}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="fr_FR">
<meta property="og:site_name" content="Louma by Seggfaye">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/{image}">
{ld}
<style>{CSS}</style>
</head>
<body>
<header class="topbar">
  <a class="brand" href="/en/">Louma by Seggfaye</a>
  <nav>
    <a href="/en/shop.html">Shop</a>
    <a href="/en/shipping.html">Shipping</a>
    <a href="/en/senegalese-food.html">Senegalese food</a>
    <a href="/en/thieboudienne-recipe.html">Thieboudienne</a>
    <a href="/en/dawadawa-iru-soumbala.html">Dawadawa</a>
    <a href="/en/cymbium-yeet.html">Cymbium</a>
    <a class="lang" href="{lang_link}" hreflang="fr" lang="fr">Français</a>
  </nav>
</header>
{body}
<footer>
  <p>Louma by Seggfaye &mdash; Authentic Senegalese food from the Îles du Saloum</p>
  <p style="margin-top:.3rem;"><a href="https://wa.me/{WA}">WhatsApp</a> &middot; <a href="https://www.tiktok.com/@seggfaye">TikTok</a> &middot; <a href="https://www.youtube.com/@loumaseggfaye">YouTube</a> &middot; <a href="{lang_link}" hreflang="fr">Version française</a></p>
</footer>
</body>
</html>
"""


def crumbs(name, path):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/en/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": SITE + path}]}


def article_ld(path, title, desc, image):
    return {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc,
            "inLanguage": "en", "author": AUTHOR, "publisher": PUBLISHER, "datePublished": DATE,
            "dateModified": DATE, "image": f"{SITE}/{image}", "mainEntityOfPage": SITE + path}


def faq_ld(qas):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}} for q, a in qas]}


def faq_html(qas):
    return '<div class="faq">\n' + "\n".join(f"    <details><summary>{q}</summary>\n      <p>{a}</p></details>" for q, a in qas) + "\n  </div>"


def header(cat, h1, minutes):
    return f"""  <header class="article-header">
    <div class="article-cat">{cat}</div>
    <h1>{h1}</h1>
    <div class="article-meta">
      <span>By <strong><a href="/le-guedjologue.html" style="color:var(--gold)">Lamine Faye, the Guedjologue</a></strong></span>
      <span>Published <strong>September 28, 2026</strong></span>
      <span>Reading time: <strong>{minutes} min</strong></span>
    </div>
  </header>"""


SHIPPING = """<div class="highlight-box">
    <p><strong>Shipping:</strong> France and Europe from our online shop. <strong>UK from €18.99, the Americas and Asia from €35.19</strong> with Colissimo International (tracked). <a href="/en/shipping.html">See all shipping rates</a>. We do not ship to Africa.</p>
  </div>"""

PAGES = {}

# ---------------------------------------------------------------- CYMBIUM
p, fr = "/en/cymbium-yeet.html", "/blog/cymbium-coquillage-yeet-senegal.html"
t = "Cymbium: the sea snail Senegal calls yeet"
d = "Cymbium is the big West African sea snail that Senegal calls yeet: species, the 17.5 cm legal size, its taste and how to cook it. By the Guedjologue."
qas = [
    ("What is cymbium?", "A large sea snail (a gastropod mollusc) from the coasts of West Africa. In Senegal it is called yeet. Its flesh is dried and fermented, then used as a seasoning in thieboudienne."),
    ("Are cymbium and yeet the same thing?", "Yes. Cymbium is the scientific name of the genus, yeet is its Wolof name. You will also see it written yett, yette or yet."),
    ("How big must a cymbium be to be caught?", "At least 17.5 cm in Senegal. Below that size it is illegal: the animal has not yet had time to reproduce."),
    ("What does dried cymbium taste like?", "A very powerful umami taste, deep and briny. One small piece flavours a whole pot, which is why it is nicknamed the African Maggi."),
    ("Where can I buy dried cymbium (yeet)?", "Louma by Seggfaye sells large pieces of dried yeet under the name Yeet Maggi, in 100 g packs, shipped across Europe, the UK, the Americas and Asia (Colissimo International)."),
]
b = f"""<nav class="breadcrumb"><a href="/en/">Home</a> &gt; <span>Cymbium (yeet)</span></nav>
<article>
{header("The Guedjologue's guide", "Cymbium: the sea snail Senegal calls yeet", 4)}
  <img class="hero-img" src="/yeet1.webp" alt="Dried cymbium, the sea snail called yeet in Senegal" loading="eager">
  <div class="highlight-box">
    <p><strong>In short:</strong> <strong>cymbium</strong> is a large sea snail from the coasts of West Africa. In Senegal we call it <strong>yeet</strong> (also written yett, yette or yet). Dried and fermented, it becomes the seasoning that gives thieboudienne its taste. And its fishing is regulated by law: <strong>nothing under 17.5 cm</strong>.</p>
  </div>
  <p>Search for “cymbium” and you land on scientific pages: <em>Cymbium pepo</em>, <em>Cymbium glans</em>, the volute family. All correct, but they miss the point: in Senegal this shell is not a museum curiosity. It is <strong>everyday food</strong>, and I sell it.</p>
  <h2>What exactly is cymbium?</h2>
  <p>Cymbium is a <strong>gastropod mollusc</strong>: a big sea snail, if you like. It lives buried in the sand, in shallow water along the coast, from Senegal down to Angola.</p>
  <p>There are <strong>several species</strong>. The largest, <em>Cymbium glans</em>, grows beyond 30 cm and can weigh several kilos. <em>Cymbium pepo</em> lives further north. Fishermen don't bother with Latin: for everyone, it is <strong>yeet</strong>.</p>
  <h2>Cymbium or yeet: one animal, two words</h2>
  <p><strong>Cymbium</strong> is the genus name used by scientists. <strong>Yeet</strong> is its name in Wolof, the main language of Senegal. Wolof is spoken more than it is written, so everyone spells it by ear: <strong>yett</strong>, <strong>yette</strong> or <strong>yet</strong>. It is the same shellfish.</p>
  <h2>Why we don't take the small ones: the 17.5 cm rule</h2>
  <p>In Senegal, <strong>the law forbids catching cymbium under 17.5 cm</strong>, measured from the tip of the shell to its lowest point. Below that size the animal has not had time to reproduce. Catching it means eating tomorrow's harvest.</p>
  <p>In the <strong>Îles du Saloum</strong> (the Saloum Delta), communities go further than the law. From <strong>June to August</strong>, they close fishing areas themselves, led above all by the women. Nobody forces them: it is a <strong>biological rest</strong>. The sea rests, the yeet grows.</p>
  <p>Science is looking at it too. In 2023 and 2024, Senegalese and French researchers (ISRA-CRODT and the LEMAR laboratory in Brest, with JICA) studied cymbium growth in tanks at Ouakam and Pointe Sarène, to prepare a management plan and test farming.</p>
  <h2>The taste: why it is called the African Maggi</h2>
  <p>Fresh, cymbium flesh is <strong>as tender as butter</strong>. Dried and fermented, it develops a <strong>very powerful umami taste</strong>, deep and briny: the same family of flavours as fermented anchovies or Japanese dashi.</p>
  <p>One small piece flavours a whole pot. That is why we call it the <strong>African Maggi</strong>: it does the job of a stock cube, naturally, with no additives. Our grandmothers used it long before stock cubes reached Africa.</p>
  <h2>Which dishes it goes into</h2>
  <p>Dried cymbium goes first into <a href="/en/thieboudienne-recipe.html">thieboudienne</a>, Senegal's national dish, listed by UNESCO as intangible cultural heritage in 2021. You also find it in caldou (fish broth), soupou kandja (okra sauce) and mbakhalou Saloum.</p>
  <p>The rule never changes: crumble it into the sauce <strong>at the start of cooking</strong>, it melts and flavours the whole dish. And salt afterwards, never before: it already brings salt.</p>
  <h2>Cymbium on video</h2>
  <div style="margin:1.2rem auto;max-width:360px;">
    <iframe style="width:100%;aspect-ratio:9/16;border:0;border-radius:.6rem;" src="https://www.youtube.com/embed/NM4Mb80QsTk" title="What is yeet (cymbium)? — Louma by Seggfaye" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    <p style="font-size:.8rem;text-align:center;margin-top:.4rem;">Cymbium straight out of the sea (in French and Wolof)</p>
  </div>
  <h2>Where to buy dried cymbium</h2>
  <p>I sell dried cymbium under its Senegalese name: <strong>Yeet Maggi</strong>, 6 € per 100 g. I only sell large pieces: that is not a sales pitch, it is the law and respect for the sea.</p>
  {SHIPPING}
  <p><a class="btn" href="{wa('Hello, I would like to order dried yeet (cymbium).')}">Order on WhatsApp</a><a class="btn ghost" href="/en/shop.html">See the shop</a></p>
  <h2>Frequently asked questions about cymbium</h2>
  {faq_html(qas)}
  <h2>Read next</h2>
  <p><a href="/en/thieboudienne-recipe.html">Authentic thieboudienne recipe</a></p>
  <p><a href="/en/dawadawa-iru-soumbala.html">Dawadawa, iru, soumbala, netetou: one seasoning, many names</a></p>
  <p><a href="/en/senegalese-food.html">Senegalese food: the dishes you need to know</a></p>
</article>"""
PAGES[p] = page(p, fr, t, d, "yeet1.webp", b, [article_ld(p, t, d, "yeet1.webp"), crumbs("Cymbium (yeet)", p), faq_ld(qas)])

# ---------------------------------------------------------------- DAWADAWA
p, fr = "/en/dawadawa-iru-soumbala.html", "/blog/dawadawa-netetou-african-locust-bean.html"
t = "Dawadawa, iru, soumbala: the African locust bean seasoning"
d = "Dawadawa (Ghana, Nigeria), iru (Yoruba), soumbala (Mali), netetou (Senegal): the same fermented African locust bean seeds. How it is made, how to cook with it, where to buy it."
qas = [
    ("What is dawadawa?", "A West African fermented seasoning made from the seeds of the African locust bean tree (néré, Parkia biglobosa). It gives a deep, natural umami taste to sauces and soups."),
    ("Are dawadawa, iru, soumbala and netetou the same?", "Yes, the same product under different names: netetou in Senegal, soumbala in Mali and Burkina Faso, soumbara in Guinea and Côte d'Ivoire, dawadawa in Ghana and northern Nigeria, iru among the Yoruba."),
    ("How is dawadawa made?", "The seeds are boiled for almost a whole day, fermented for several days, dried in the sun, then pounded into powder or shaped into balls. About five days in all."),
    ("Why does it smell so strong?", "That is the fermentation. The smell goes away with cooking and leaves a deep umami taste: the signature of the real thing."),
    ("Where can I buy dawadawa (netetou)?", "Louma by Seggfaye sells netetou as a powder, a dome, a bar and a ready-made mix, shipped across Europe, the UK, the Americas and Asia (Colissimo International)."),
]
b = f"""<nav class="breadcrumb"><a href="/en/">Home</a> &gt; <span>Dawadawa</span></nav>
<article>
{header("The Guedjologue's guide", "Dawadawa, iru, soumbala: one seasoning, many names", 5)}
  <img class="hero-img" src="/netetou-poudre.webp" alt="Netetou powder, the Senegalese name for dawadawa (African locust bean)" loading="eager">
  <div class="highlight-box">
    <p><strong>In short:</strong> <strong>dawadawa</strong>, known in English as <strong>African locust bean</strong>, is what we call <strong>netetou</strong> in Senegal. Same product: fermented seeds of the néré tree, the natural seasoning that replaced stock cubes long before they were invented.</p>
  </div>
  <p>One day I came across a video of a Ghanaian cook talking about dawadawa. I smiled: he was describing my netetou exactly. Same seed, same smell that sends some people running and makes others hungry, same job in the pot. From one end of West Africa to the other, it is the same story with a different name.</p>
  <h2>What is dawadawa?</h2>
  <p>Dawadawa is a <strong>fermented West African seasoning</strong> made from the seeds of the néré tree (<em>Parkia biglobosa</em>), the African locust bean. Its job: a 100 % natural flavour enhancer, the deep umami that gives power to sauces, soups and stews.</p>
  <h2>One product, many names</h2>
  <ul>
    <li><strong>Netetou</strong>: in Senegal (the Wolof name).</li>
    <li><strong>Soumbala</strong>: in Mali and Burkina Faso.</li>
    <li><strong>Soumbara</strong>: in Guinea and Côte d'Ivoire.</li>
    <li><strong>Dawadawa</strong>: in Ghana and northern Nigeria.</li>
    <li><strong>Iru</strong>: among the Yoruba, in Nigeria.</li>
    <li><strong>African locust bean</strong>: the English name used across the diaspora.</li>
  </ul>
  <p>Same tree, same seed, same fermentation, same use. If you are looking for dawadawa or iru and you find netetou, look no further.</p>
  <h2>How it is made (five days of patience)</h2>
  <h3>1. The seed</h3>
  <p>It all starts with the néré fruit: a pod with a sweet yellow pulp that people eat, and hard seeds inside. Only the seeds become dawadawa.</p>
  <h3>2. The long boil</h3>
  <p>The seeds are boiled for a very long time, almost a whole day, over a wood fire, because they are hard. Then they are hulled.</p>
  <h3>3. The fermentation</h3>
  <p>This is the heart of the process. The seeds are well covered and left to ferment for several days. That is when, as we say at home, “the smell comes in”: the fermentation that gives dawadawa its powerful aroma and all its taste.</p>
  <h3>4. Drying and final shape</h3>
  <p>Around the fifth day, the seeds are dried in the sun for a few hours. Then, depending on local habits, they are pounded into powder or shaped into balls. Two shapes, one seasoning.</p>
  <h2>The “Maggi” before Maggi</h2>
  <p>As my grandmother used to say: before stock cubes, there was néré. You crushed the dawadawa in a little water, added salt and a pinch of chilli, let it simmer, and the sauce already had all its taste. That is why the néré is nicknamed “the Maggi tree”.</p>
  <h2>That smell (don't let it scare you)</h2>
  <p>Yes, dawadawa smells strong. Raw, it is surprising, and many people don't dare because of it. But the smell disappears with cooking and leaves a depth of taste no cube can replace. The smell is the signature of fermentation: the sign that it is the real thing.</p>
  <h2>How to cook with it</h2>
  <p>Crush or crumble a spoonful into your sauce <strong>at the start of cooking</strong>, as you would with a stock cube. In Senegal it goes into <a href="/en/thieboudienne-recipe.html">thieboudienne</a>, into the stuffing of the fish, and into many sauces.</p>
  <h2>Where to buy dawadawa (netetou)</h2>
  <p>In our shop you will find netetou prepared the traditional way: <strong>powder</strong> (ready to use), <strong>dome</strong> and <strong>bar</strong> (to crush yourself), 5 € per 100 g, and <strong>Netetou Mix</strong>, my own blend with dried shrimp and kéthiakh (smoked fish).</p>
  {SHIPPING}
  <p><a class="btn" href="{wa('Hello, I would like to order netetou (dawadawa).')}">Order on WhatsApp</a><a class="btn ghost" href="/en/shop.html">See the shop</a></p>
  <h2>Frequently asked questions about dawadawa</h2>
  {faq_html(qas)}
  <h2>Read next</h2>
  <p><a href="/en/cymbium-yeet.html">Cymbium (yeet): the other “African Maggi”</a></p>
  <p><a href="/en/thieboudienne-recipe.html">Authentic thieboudienne recipe</a></p>
  <p><a href="/en/senegalese-food.html">Senegalese food: the dishes you need to know</a></p>
</article>"""
PAGES[p] = page(p, fr, t, d, "netetou-poudre.webp", b, [article_ld(p, t, d, "netetou-poudre.webp"), crumbs("Dawadawa", p), faq_ld(qas)])

# ---------------------------------------------------------------- THIEBOUDIENNE
p, fr = "/en/thieboudienne-recipe.html", "/blog/recette-thieboudienne-authentique.html"
t = "Thieboudienne recipe: Senegal's national dish, the authentic way"
d = "Authentic thieboudienne (ceebu jen) recipe, step by step: Senegal's national rice and fish dish, UNESCO heritage. Ingredients, the 3 secret gestures, red vs white."
ingredients = ["1.5 kg fresh firm fish (thiof, capitaine or similar)", "1 piece of guedj (dried fermented fish)", "1 piece of yeet (dried cymbium)",
               "1 tablespoon of netetou (dawadawa)", "1 kg broken rice", "200 ml vegetable oil", "3 tablespoons tomato paste", "2 onions",
               "4 garlic cloves", "1 bunch of parsley", "Chilli paste, salt, pepper", "1 piece of tamarind", "1 bitter African eggplant (diakhatou)",
               "2 carrots", "1 piece of cabbage", "1 piece of cassava", "2 turnips", "1 handful of okra"]
steps = [
    ("Make the stuffing (roff)", "Blend or pound parsley, garlic, onion, chilli, salt, pepper and a little netetou. Cut 3 or 4 deep slits on each side of the fish and fill them generously with the stuffing."),
    ("Sear the fish", "Heat the oil in a large pot. Brown the stuffed fish on both sides without moving it too much so it doesn't break. Set aside."),
    ("Build the sauce", "In the same oil, fry the sliced onions. Add the tomato paste and let it catch for 90 seconds until brick-coloured, then deglaze. Add the guedj and the yeet, cover with about 2 litres of water and simmer for 20 minutes."),
    ("Add the vegetables", "Add them by cooking time: cassava and carrots first, cabbage and turnips 10 minutes later, then the bitter eggplant and okra 5 minutes later. Put the fish back and simmer 25 minutes. Taste and adjust the salt."),
    ("Cook the rice in the broth", "Take out the fish and vegetables and keep them warm. Strain the broth: you need about twice the volume of rice. Add the washed broken rice, cook until the liquid is absorbed, then cover the pot with a clean cloth and the lid and leave 10 minutes without opening."),
    ("Serve", "Spread the rice in a large round dish, place the fish in the centre and the vegetables around it. Serve with lime and chilli paste. We eat together, around the dish."),
]
qas = [
    ("What is thieboudienne?", "Senegal's national dish: rice cooked in a tomato and fish broth, served with fish and vegetables. In Wolof, “thieb” means rice and “dienne” means fish. It is listed by UNESCO as intangible cultural heritage since 2021."),
    ("How do you spell it?", "Thieboudienne, thiéboudienne, thiebou dieune, tieboudiene, or in Wolof spelling ceebu jën. Many people simply say thieb."),
    ("What is the difference between thieboudienne and jollof rice?", "Both are West African tomato rice dishes, but thieboudienne is cooked with fish and seasoned with dried fermented seafood (guedj, yeet) and netetou, and the rice is cooked in the fish broth. Tradition places its birth in Saint-Louis, Senegal."),
    ("Does thieboudienne use palm oil?", "No. It is cooked with vegetable oil. The red-orange colour of the rice comes only from tomato."),
    ("Which rice for thieboudienne?", "Broken rice, not basmati or long-grain rice. Broken rice absorbs the broth better and gives the right texture."),
]
recipe = {"@context": "https://schema.org", "@type": "Recipe", "name": "Thieboudienne (ceebu jen), Senegalese rice and fish",
          "description": d, "inLanguage": "en", "image": f"{SITE}/plat-thieboudienne.jpg", "author": AUTHOR, "datePublished": DATE,
          "recipeCuisine": "Senegalese", "recipeCategory": "Main course", "recipeYield": "6 servings",
          "keywords": "thieboudienne, ceebu jen, Senegalese food, rice and fish, UNESCO",
          "recipeIngredient": ingredients,
          "recipeInstructions": [{"@type": "HowToStep", "name": n, "text": x} for n, x in steps]}
b = f"""<nav class="breadcrumb"><a href="/en/">Home</a> &gt; <span>Thieboudienne recipe</span></nav>
<article>
{header("Recipe", "Thieboudienne: the authentic recipe of Senegal's national dish", 8)}
  <img class="hero-img" src="/plat-thieboudienne.jpg" alt="Thieboudienne, Senegalese rice and fish, served in a large round dish" loading="eager">
  <div class="highlight-box">
    <p><strong>In short:</strong> thieboudienne (<strong>ceebu jën</strong> in Wolof) is Senegal's national dish: rice cooked in a tomato and fish broth, served with fish and vegetables. It has been <strong>UNESCO intangible cultural heritage since 2021</strong>. What makes it thieboudienne rather than “rice and fish” are three seasonings: <strong>guedj</strong>, <strong>yeet</strong> and <strong>netetou</strong>.</p>
  </div>
  <p>My name is Lamine Faye, people call me the Guedjologue. I grew up in the <strong>Îles du Saloum</strong>, in the Saloum Delta, where thieboudienne is made with ingredients you find nowhere else. Here is the real recipe, the one we cook in Senegal.</p>
  <h2>Where does thieboudienne come from? Saint-Louis</h2>
  <p>Thieboudienne was born in <strong>Saint-Louis</strong>, Senegal's former capital, in the fishing communities of the island. That is what UNESCO records in its 2021 listing. Tradition attributes the recipe to <strong>Penda Mbaye</strong>, a cook from Guet Ndar, the fishermen's district, in the 19th century. In colonial times, broken rice from Indochina replaced local grains: it became the base of the dish.</p>
  <h2>The secret ingredients</h2>
  <p><strong>Guedj</strong>: dried and fermented fish. It gives the deep umami flavour. One small piece is enough.</p>
  <p><strong>Yeet</strong>: dried and fermented <a href="/en/cymbium-yeet.html">cymbium</a>, a big sea snail, nicknamed the African Maggi.</p>
  <p><strong>Netetou</strong>: fermented néré seeds, the <a href="/en/dawadawa-iru-soumbala.html">dawadawa</a> of Ghana and Nigeria. A 100 % natural flavour enhancer that replaces stock cubes.</p>
  <h2>Ingredients (6 people)</h2>
  <ul>
{chr(10).join('    <li>' + i + '</li>' for i in ingredients)}
  </ul>
  <h2>Step by step</h2>
  <ol>
{chr(10).join(f'    <li><strong>{n}.</strong> {x}</li>' for n, x in steps)}
  </ol>
  <h2>The Guedjologue's 3 secret gestures</h2>
  <p><strong>1. Toast the tomato.</strong> Let the tomato paste catch in the hot oil for 90 seconds until it turns brick-coloured, then deglaze. It multiplies the aroma and tames the acidity.</p>
  <p><strong>2. Flavour the broth before the rice.</strong> Forget cubes. The real secret is the ancestral trio: yeet, netetou, bay leaf. Golden rule: good broth, good rice.</p>
  <p><strong>3. Steam it under a cloth.</strong> When the rice has absorbed the broth, put a clean cloth over the pot, then the lid. Ten minutes, no peeking. The steam finishes the cooking: separate, shiny grains.</p>
  <h2>Red or white thieboudienne</h2>
  <p>This recipe is the <strong>red</strong> thieboudienne, the best known, made with tomato paste. The <strong>white</strong> version, thiebou wekh, uses fresh tomato instead: a lighter sauce. Both use guedj and yeet.</p>
  <h2>No palm oil, and broken rice</h2>
  <p>Contrary to a common belief, red palm oil does not go into thieboudienne: it is cooked with vegetable oil, and the colour comes from the tomato. And it is made with <strong>broken rice</strong>, not basmati or long-grain rice.</p>
  <h2>Where to find the ingredients</h2>
  <p>Guedj, yeet and netetou are not in supermarkets. That is why I created Louma by Seggfaye: I source directly from the fishermen and the women processors of the Îles du Saloum, with no middlemen.</p>
  {SHIPPING}
  <p><a class="btn" href="{wa('Hello, I would like the ingredients for thieboudienne (guedj, yeet, netetou).')}">Order the ingredients on WhatsApp</a><a class="btn ghost" href="/en/shop.html">See the shop</a></p>
  <h2>Frequently asked questions</h2>
  {faq_html(qas)}
  <h2>Read next</h2>
  <p><a href="/en/senegalese-food.html">Senegalese food: the dishes you need to know</a></p>
  <p><a href="/en/cymbium-yeet.html">Cymbium (yeet), the African Maggi</a></p>
  <p><a href="/en/dawadawa-iru-soumbala.html">Dawadawa, iru, soumbala, netetou</a></p>
</article>"""
PAGES[p] = page(p, fr, t, d, "plat-thieboudienne.jpg", b, [recipe, crumbs("Thieboudienne recipe", p), faq_ld(qas)])

# ---------------------------------------------------------------- SENEGALESE FOOD
p, fr = "/en/senegalese-food.html", "/blog/plats-senegalais.html"
t = "Senegalese food: the dishes you need to know"
d = "A guide to Senegalese food by a Senegalese cook: thieboudienne, yassa, mafé, caldou, soupou kandja, mbakhalou Saloum, thiakry, and the ingredients behind them."
dishes = [
    ("Thieboudienne", "ceebu jën · the national dish", "Rice cooked in a tomato and fish broth, with fish and vegetables. UNESCO heritage since 2021.", "/en/thieboudienne-recipe.html", "plat-thieboudienne.jpg"),
    ("Thiebou yapp", "rice with meat", "The meat version of Senegalese rice: fragrant rice served with meat and vegetables.", None, "plat-thiebou-yapp.jpg"),
    ("Yassa chicken", "onions & lemon", "Marinated chicken, grilled, then simmered in a sauce of melted onions and lemon.", None, "plat-yassa.jpg"),
    ("Yassa fish", "fried fish with onions", "The fish version of yassa: fried fish on white rice, covered with the lemon and onion sauce.", None, "plat-yassa-poisson.jpg"),
    ("Mafé", "peanut sauce", "A creamy peanut sauce with meat or fish, served on white rice.", None, "plat-mafe.jpg"),
    ("Caldou", "fish broth", "The light dish of Senegal: a fish broth flavoured with guedj, lemon and vegetables.", None, "plat-caldou.jpg"),
    ("Soupou kandja", "okra sauce", "A rich okra sauce with red palm oil, yeet and guedj.", None, "plat-soupoukandja.jpg"),
    ("Mbakhalou Saloum", "rice with ground peanuts", "The signature dish of the Îles du Saloum: rice cooked in a sauce of ground peanuts.", None, "plat-mbakhalou.jpg"),
    ("Thiakry", "the dessert", "Millet couscous with sweetened curdled milk, served cold. The sweetness that ends the meal.", None, "plat-thiakry.jpg"),
]
qas = [
    ("What is the national dish of Senegal?", "Thieboudienne (ceebu jën), rice with fish, listed by UNESCO as intangible cultural heritage since 2021."),
    ("What are the most famous Senegalese dishes?", "Thieboudienne, yassa, mafé, caldou, soupou kandja and mbakhalou Saloum, and thiakry for dessert."),
    ("Which ingredients do you need to cook Senegalese food?", "Guedj (dried fermented fish), yeet (dried cymbium), netetou (fermented néré seeds, also called dawadawa or soumbala), red palm oil for some sauces, and broken rice."),
]
cards = "\n".join(
    f"""    <div class="card"><img src="/{img}" alt="{n}, Senegalese dish" loading="lazy"><div class="body"><h3>{n}</h3><div class="local">{sub}</div><p>{txt}</p>{f'<div class="actions"><a href="{link}">Read the recipe →</a></div>' if link else ''}</div></div>"""
    for n, sub, txt, link, img in dishes)
b = f"""<nav class="breadcrumb"><a href="/en/">Home</a> &gt; <span>Senegalese food</span></nav>
<div class="wrap wide">
{header("Guide", "Senegalese food: the dishes you need to know", 5)}
  <div class="highlight-box">
    <p><strong>In short:</strong> the best-known Senegalese dishes are <strong>thieboudienne</strong> (rice and fish, the national dish), <strong>yassa</strong> (onions and lemon), <strong>mafé</strong> (peanut sauce), <strong>caldou</strong> (fish broth), <strong>soupou kandja</strong> (okra sauce) and <strong>mbakhalou Saloum</strong>. Most of them are seasoned with guedj, yeet and netetou.</p>
  </div>
  <p>I am Lamine Faye, the Guedjologue, and I grew up in the Îles du Saloum. Here are the great dishes of Senegalese cooking, the ones the diaspora misses the most.</p>
  <div class="grid">
{cards}
  </div>
  <h2>The Senegalese pantry</h2>
  <p>Almost all these dishes share the same base ingredients, the ones you can't find in a supermarket:</p>
  <ul>
    <li><strong>Guedj</strong>: dried and fermented fish, the source of the deep umami taste.</li>
    <li><strong>Yeet</strong>: dried <a href="/en/cymbium-yeet.html">cymbium</a>, the “African Maggi”.</li>
    <li><strong>Netetou</strong>: fermented néré seeds, known as <a href="/en/dawadawa-iru-soumbala.html">dawadawa, iru or soumbala</a>.</li>
    <li><strong>Broken rice</strong>, and red palm oil for some sauces (never in thieboudienne).</li>
  </ul>
  {SHIPPING}
  <p><a class="btn" href="/en/shop.html">Shop the ingredients</a><a class="btn ghost" href="{wa('Hello, I would like to order Senegalese ingredients.')}">Ask on WhatsApp</a></p>
  <h2>Frequently asked questions</h2>
  {faq_html(qas)}
</div>"""
PAGES[p] = page(p, fr, t, d, "plat-thieboudienne.jpg", b, [article_ld(p, t, d, "plat-thieboudienne.jpg"), crumbs("Senegalese food", p), faq_ld(qas)])

# ---------------------------------------------------------------- SHOP
SHOP = [
    ("Dried seafood & guedj (fermented fish)", [
        ("guej-beurre", "Guedj Beurre", "Dried fermented meagre (courbine), the classic guedj for thieboudienne."),
        ("guej-kong", "Guedj Kong", "Dried fermented sea catfish (mâchoiron)."),
        ("guej-sol", "Guedj Sole", "Dried sole, delicate, and the only guedj dried without its skin."),
        ("guej-yass", "Guedj Yass", "The rarest guedj: dried without any salt, preserved by its own fat and the sun."),
        ("guej-tambajang", "Guedj Tambajang", "Whole dried mullet, used as a seasoning."),
        ("guej-beur-casamance", "Guedj Beurre Casamance", "Meagre dried then wood-smoked, Casamance style. Deeper, more complex."),
        ("guej-toumboulan", "Toumboulan", "Dried ray fin cartilage. Very rare. Thickens sauces naturally."),
        ("yeet-maggi", "Yeet Maggi (dried cymbium)", "The “African Maggi”: dried fermented sea snail, large pieces only (17.5 cm legal size)."),
        ("kongfume", "Smoked catfish (kong fumé)", "Sea catfish smoked the Senegalese way."),
        ("kongfume-gambie", "Smoked catfish from Gambia", "Same fish, smoked the Gambian way."),
        ("crevettes-sechees", "Dried shrimp", "Small sun-dried shrimp from the Îles du Saloum."),
        ("yoxos", "Yoxos (dried mangrove oysters)", "Oysters picked in the mangroves of the Îles du Saloum, then dried."),
        ("pagne", "Pagne (dried cockles)", "Dried cockles from the Îles du Saloum."),
        ("tuffa", "Toufa (dried murex)", "A small sea snail, dried."),
        ("pack-saloum", "Saloum Pack", "Four treasures of the Îles du Saloum: toufa, yoxos, dried shrimp and cockles."),
        ("keciax", "Kéthiakh", "Sardinella salted, smoked and dried."),
    ]),
    ("Seasonings", [
        ("netetu-poudre", "Netetou powder (dawadawa)", "Fermented néré seeds, ground and ready to use. The natural stock cube."),
        ("netetu-dom", "Netetou dome", "Fermented néré seeds, whole, to crush yourself."),
        ("netetu-barre", "Netetou bar", "Fermented néré seeds pounded into a compact bar."),
        ("netetu-mix", "Netetou Mix", "My blend: roasted netetou, dried shrimp and kéthiakh, with a touch of chilli."),
        ("sauce-netetu-beugeuc", "Netetou & bissap leaf sauce", "Ready-made sauce of netetou and bissap leaves (beugeuc)."),
        ("beugeuc-feuille-bissap", "Beugeuc (bissap leaves)", "The leaves of the bissap plant, used in cooking."),
        ("puree-piment", "Kani (hot chilli paste)", "Artisanal hot chilli paste, served on the side."),
    ]),
    ("Drinks & fruits", [
        ("bissap-rouge", "Red bissap (dried hibiscus)", "Dried hibiscus calyces for the famous bissap drink (zobo, sorrel)."),
        ("bouye-baobab", "Bouye (baobab powder)", "Baobab fruit powder, for bouye juice and desserts."),
        ("maad-confi", "Maad jam", "Jam of maad (Saba senegalensis), a tangy wild fruit from Senegal."),
        ("maad-fruit", "Maad fruit", "Fresh maad (Saba senegalensis), in season."),
    ]),
    ("Millet, grains & peanuts", [
        ("thiere-champion", "Thiéré (millet couscous)", "Fine millet couscous."),
        ("arraw-dugup", "Arraw (millet pellets)", "Hand-rolled millet pellets for traditional porridge."),
        ("ciakri", "Thiakry", "Millet for thiakry, the dessert with curdled milk."),
        ("sankal-duggup", "Sankal (millet grits)", "Coarse millet semolina for fondé porridge."),
        ("niebe-saloum", "Niébé (black-eyed peas)", "Black-eyed peas from the Saloum."),
        ("guerte-noflay", "Roasted peanut powder", "Finely ground roasted peanuts, for mbakhalou and sauces."),
        ("tigadegue-250", "Tigadégué (peanut paste) 250 g", "Artisanal peanut paste for mafé."),
        ("tiguadegue-500", "Tigadégué (peanut paste) 500 g", "Artisanal peanut paste for mafé."),
    ]),
    ("Oils & honey", [
        ("diwtir-pure", "Diwtir (red palm oil)", "Pure red palm oil for soupou kandja and other sauces."),
        ("lem-miel", "Pure honey from Kédougou", "Pure honey from Kédougou, south-east Senegal."),
    ]),
]


def load_products():
    js = subprocess.run(["node", "-e", """
global.window={};global.document={addEventListener(){},querySelectorAll(){return []},getElementById(){return null}};
const src=require('fs').readFileSync('produits.js','utf8');const m=src.match(/(?:const|var|let)\\s+(\\w+)\\s*=\\s*\\[/);
console.log(JSON.stringify(eval(src+';'+m[1])));"""], capture_output=True, text=True, check=True).stdout
    return {x["id"]: x for x in json.loads(js)}


PROD = load_products()
UNIT = {"par 100g": "per 100 g", "par 300g": "per 300 g", "par 500g": "per 500 g", "par 200g": "per 200 g", "par 150g": "per 150 g",
        "par 250g": "per 250 g", "250g": "250 g", "300g": "300 g", "200g": "200 g", "500g": "500 g", "par kg": "per kg",
        "par 1L": "per litre", "1,5L": "1.5 litre", "par 0,5L": "per 0.5 litre"}
sections, items_ld, pos = [], [], 0
for title_s, items in SHOP:
    cs = []
    for pid, name, txt in items:
        pr = PROD[pid]
        if not pr.get("stock", True):
            continue
        price = f"€{pr['prix']:g}"
        unit = UNIT.get(pr["unite"], pr["unite"])
        pos += 1
        items_ld.append({"@type": "ListItem", "position": pos, "url": f"{SITE}/produits/{pid}.html", "name": name})
        cs.append(f"""    <div class="card"><img src="/{pr['image']}" alt="{name}" loading="lazy"><div class="body"><h3>{name}</h3><div class="price">{price} <span style="font-weight:400;color:var(--muted)">{unit}</span></div><p>{txt}</p><div class="actions"><a href="{wa('Hello, I would like to order: ' + name + ' (' + price + ' ' + unit + ').')}">Order on WhatsApp</a><a href="/produits/{pid}.html" hreflang="fr">Details (in French)</a></div></div></div>""")
    sections.append(f'  <h2>{title_s}</h2>\n  <div class="grid">\n' + "\n".join(cs) + "\n  </div>")
p = "/en/shop.html"
t = "Shop Senegalese food online: guedj, yeet, netetou, bissap | Louma"
d = "Authentic Senegalese ingredients from the Îles du Saloum: dried fish (guedj), cymbium (yeet), netetou (dawadawa), dried shrimp, bissap, baobab, millet. Shipped across Europe, the Americas, the UK and Asia."
b = f"""<nav class="breadcrumb"><a href="/en/">Home</a> &gt; <span>Shop</span></nav>
<div class="wrap wide">
  <header class="article-header">
    <div class="article-cat">Shop</div>
    <h1>Authentic Senegalese ingredients</h1>
    <p>Sourced directly from the fishermen and the women processors of the Îles du Saloum, and from producers across Senegal. Prices in euros.</p>
  </header>
  {SHIPPING}
  <p><strong>How to order:</strong> tap “Order on WhatsApp” on any product, tell us your country, and we confirm the total with shipping (rates on the <a href="/en/shipping.html">shipping page</a>). Payment by PayPal or Wero.</p>
{chr(10).join(sections)}
  <p style="margin-top:2rem;"><a class="btn" href="{wa('Hello, I would like to place an order.')}">Order on WhatsApp</a></p>
</div>"""
shop_ld = {"@context": "https://schema.org", "@type": "ItemList", "name": "Louma by Seggfaye — Senegalese ingredients", "itemListElement": items_ld}
PAGES[p] = page(p, None, t, d, "packsaloum-sachetdebout1.webp", b, [shop_ld, crumbs("Shop", p)], og_type="website")

# ---------------------------------------------------------------- SHIPPING
p = "/en/shipping.html"
t = "Shipping rates: Europe, UK, USA, Canada, Asia | Louma by Seggfaye"
d = "Shipping rates for Senegalese food from France: Europe, United Kingdom, the Americas (USA, Canada) and Asia with Colissimo International, tracked. We do not ship to Africa."
ROWS = [("up to 500 g", "€18.99", "€35.19"), ("up to 1 kg", "€23.39", "€39.19"), ("up to 2 kg", "€26.19", "€53.99"),
        ("up to 5 kg", "€32.59", "€78.69"), ("up to 10 kg", "€50.99", "€148.99")]
rows = "\n".join(f"      <tr><td style='padding:.45rem'>{w}</td><td style='padding:.45rem'>{uk}</td><td style='padding:.45rem'>{c}</td></tr>" for w, uk, c in ROWS)
TH = "padding:.5rem;border-bottom:1px solid var(--border-hi)"
b = f"""<nav class="breadcrumb"><a href="/en/">Home</a> &gt; <span>Shipping</span></nav>
<article>
  <header class="article-header">
    <div class="article-cat">Shipping</div>
    <h1>Shipping rates</h1>
  </header>
  <p>We ship from France. Our dried products (guedj, yeet, netetou, dried shrimp, bissap, millet…) travel well. <strong>Fresh and frozen fish are delivered in France and Europe only.</strong></p>
  <h2>France and Europe</h2>
  <p>Order directly in our <a href="/">online shop</a> (in French): the shipping cost is calculated in the basket. Or order on WhatsApp.</p>
  <h2>United Kingdom, the Americas and Asia</h2>
  <p>Colissimo International, tracked. Price by total weight of the parcel (packaging included).</p>
  <table style="width:100%;border-collapse:collapse;margin:1rem 0 1.5rem;font-size:.95rem">
    <thead><tr style="color:var(--gold);text-align:left"><th style="{TH}">Parcel weight</th><th style="{TH}">United Kingdom</th><th style="{TH}">Americas (USA, Canada…) &amp; Asia</th></tr></thead>
    <tbody style="color:var(--cream)">
{rows}
    </tbody>
  </table>
  <p>Import duties and taxes, if any, are charged by your country on arrival and paid by the recipient.</p>
  <h2>Africa</h2>
  <p>We do not ship to Africa.</p>
  <h2>How to order from abroad</h2>
  <p>Choose your products in the <a href="/en/shop.html">shop</a>, then send us your list and your country on WhatsApp. We confirm the total (products + shipping) and you pay by PayPal or Wero.</p>
  <p><a class="btn" href="{wa('Hello, I would like to order from abroad. My country is: ')}">Order on WhatsApp</a><a class="btn ghost" href="/en/shop.html">See the shop</a></p>
</article>"""
PAGES[p] = page(p, None, t, d, "packsaloum-sachetdebout1.webp", b, [crumbs("Shipping", p)], og_type="website")

# ---------------------------------------------------------------- HOME
p = "/en/"
t = "Louma by Seggfaye: authentic Senegalese food from the Îles du Saloum"
d = "Senegalese online market: guedj (dried fish), yeet (cymbium), netetou (dawadawa), dried shrimp, bissap, baobab. Sourced in the Îles du Saloum by Lamine Faye, the Guedjologue."
guides = [("/en/senegalese-food.html", "Senegalese food", "The dishes you need to know, from thieboudienne to thiakry.", "plat-mafe.jpg"),
          ("/en/thieboudienne-recipe.html", "Thieboudienne recipe", "Senegal's national dish, the authentic way.", "plat-thieboudienne.jpg"),
          ("/en/dawadawa-iru-soumbala.html", "Dawadawa, iru, soumbala", "One fermented seasoning, many names.", "netetou-dome.webp"),
          ("/en/cymbium-yeet.html", "Cymbium (yeet)", "The sea snail Senegal calls the African Maggi.", "yeet1.webp")]
gcards = "\n".join(f'    <div class="card"><img src="/{img}" alt="{n}" loading="lazy"><div class="body"><h3><a href="{u}">{n}</a></h3><p>{x}</p></div></div>' for u, n, x, img in guides)
b = f"""<div class="wrap wide" style="padding-top:2rem;">
  <header class="article-header">
    <div class="article-cat">Senegalese online market</div>
    <h1>Authentic Senegalese food, from the Îles du Saloum to your kitchen</h1>
    <p>I am <strong>Lamine Faye</strong>, known as <strong>the Guedjologue</strong>. I grew up in the Îles du Saloum, the Saloum Delta in Senegal, a UNESCO World Heritage site. Louma by Seggfaye brings you the ingredients of Senegalese cooking that you can't find in supermarkets: <strong>guedj</strong> (dried fermented fish), <strong>yeet</strong> (dried cymbium), <strong>netetou</strong> (dawadawa), dried shrimp, bissap, baobab, millet.</p>
    <p><a class="btn" href="/en/shop.html">Visit the shop</a><a class="btn ghost" href="{wa('Hello, I would like some information about your products.')}">Ask on WhatsApp</a></p>
  </header>
  <img class="hero-img" src="/packsaloum-sachetdebout1.webp" alt="Saloum Pack: dried seafood from the Îles du Saloum" loading="eager">
  <h2>Why Louma</h2>
  <ul>
    <li><strong>Direct sourcing</strong> from the fishermen and the women processors of the Îles du Saloum, with no middlemen.</li>
    <li><strong>Traditional methods</strong>: sun-dried, smoked or fermented the way it has always been done.</li>
    <li><strong>Responsible fishing</strong>: for example, we only sell yeet over the 17.5 cm legal size.</li>
  </ul>
  {SHIPPING}
  <h2>Guides by the Guedjologue</h2>
  <div class="grid">
{gcards}
  </div>
  <p>Follow me on <a href="https://www.tiktok.com/@seggfaye">TikTok (@seggfaye)</a> and <a href="https://www.youtube.com/@loumaseggfaye">YouTube (@loumaseggfaye)</a>.</p>
</div>"""
org = {"@context": "https://schema.org", "@type": "WebSite", "name": "Louma by Seggfaye", "url": SITE + "/en/", "inLanguage": "en"}
PAGES[p] = page(p, "/", t, d, "packsaloum-sachetdebout1.webp", b, [org], og_type="website")

os.makedirs("en", exist_ok=True)
for path, htmlsrc in PAGES.items():
    f = "en/index.html" if path == "/en/" else path.lstrip("/")
    open(f, "w").write(htmlsrc)
    print("écrit", f, len(htmlsrc))
