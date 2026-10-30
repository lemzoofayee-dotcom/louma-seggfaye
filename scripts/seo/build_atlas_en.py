"""Génère en/wolof-fish-names.html (version anglaise) depuis atlas-poissons-wolof.html.
Les noms wolof, latins et les photos sont repris tels quels ; seuls les textes sont traduits.
Usage : python3 scripts/seo/build_atlas_en.py  (à relancer si l'atlas FR change)
"""
import json
import os
import re

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
FR = open(os.path.join(REPO, 'atlas-poissons-wolof.html'), encoding='utf-8').read()
URL = 'https://seggfaye.com/en/wolof-fish-names.html'
FR_URL = 'https://seggfaye.com/atlas-poissons-wolof.html'
IMG = 'https://seggfaye.com/assets/atlas-poissons/atlas-poissons-wolof-partage.jpg'
TITLE = 'Fish names in Wolof: the atlas of 77 species from Senegal'
DESC = ('Thiof, yakh, kong, yaboye, yeet, pagne… The Wolof names of 77 fish, shellfish and crustaceans '
        'from Senegal, with their English, French and Latin names. By Lamine Faye, the Guedjologue.')

ZONES = {'Fond': 'Bottom', 'Surface': 'Surface', 'Coquillage': 'Shellfish',
         'Raie &amp; requin': 'Ray &amp; shark', 'Raie & requin': 'Ray &amp; shark'}
NOTES = {
    '« beurre » = la francisation de « berr »': '“beurre” is the French spelling of “berr”',
    'nommé d&#x27;après la houe': 'named after the hoe',
    'la carpe rouge': 'the “red carp” of the markets',
    'le plus puissant des sept guedj': 'the strongest of the seven guedj',
    'le mérou blanc': 'the “white grouper”',
    'la carpe blanche': 'the “white carp”',
    'dans le pack des Îles du Saloum': 'in the Îles du Saloum pack',
    'le cymbium — un coquillage, pas un poisson': 'the cymbium: a sea snail, not a fish',
    'deux espèces, un seul nom': 'two species, one name',
    'les coques des Îles du Saloum': 'the cockles of the Îles du Saloum',
    'l&#x27;escargot de mer, un murex': 'the sea snail, a murex',
    '7 · le seul vendu au kilo': '7 · the only one sold by the kilo',
    'le mulet, séché entier': 'the mullet, dried whole',
    'la sardinelle du quotidien': 'the everyday sardinella',
    '': '',
}
DOUBTS = {
    '« plapla » = surnom français': '“plapla” is a French nickname',
    'aussi kotti (koti) — le mot de Saint-Louis': 'also kotti (koti), the Saint-Louis word',
    'la planche dit yooxoñ': 'the CRODT chart says yooxoñ',
    'Waxandoor désigne aussi le thon obèse : au Sénégal, on ne distingue pas vraiment les thons':
        'Waxandoor also means the bigeye tuna: in Senegal, tunas are not really told apart',
    'surnommé « plat plat » lui aussi': 'also nicknamed “plat plat” (flat flat)',
}


def card_en(c):
    fr_name = re.search(r'<div class="fr">(.*?)</div>', c).group(1)
    en_name = re.search(r'<div class="en">(.*?)</div>', c).group(1)
    wolfr = re.search(r'<div class="wolfr">(.*?)</div>', c).group(1)
    # alt, zone, ordre anglais puis français
    c = re.sub(r'alt="[^"]*"', f'alt="{en_name} — {wolfr} in Wolof"', c, count=1)
    c = re.sub(r'<i></i>([^<]*)</span>', lambda m: '<i></i>' + ZONES[m.group(1)] + '</span>', c)
    c = c.replace(f'<div class="fr">{fr_name}</div><div class="en">{en_name}</div>',
                  f'<div class="en">{en_name}</div><div class="fr">{fr_name}</div>')
    c = re.sub(r'>Vendu chez Louma<span>([^<]*)</span>(.*?)</a>',
               lambda m: f'>Sold at Louma<span>{m.group(1)}</span>{NOTES[m.group(2)]}</a>', c)
    c = re.sub(r'(<(?:span|div) class="doubt">)(.*?)(</(?:span|div)>)',
               lambda m: m.group(1) + DOUBTS[m.group(2)] + m.group(3), c)
    c = c.replace('graphie exacte :', 'correct spelling:').replace('>Photo : ', '>Photo: ')
    return c, wolfr


cards = re.findall(r'<article class="card.*?</article>', FR, re.S)
assert len(cards) == 77, len(cards)
converted = [card_en(c) for c in cards]
grid = ''.join(c for c, _ in converted)
wolof_names = [w for _, w in converted]

style = re.search(r'<style>.*?</style>', FR, re.S).group(0)
style = style.replace('</style>', '.card .en{font-size:13.5px;color:var(--text-2);font-style:normal;margin-top:0;}\n'
                                  '.card .fr{font-size:12px;color:var(--text-3);font-style:italic;margin-top:2px;}\n'
                                  '.langlink{float:right;color:var(--gold);}\n</style>')
gtag = re.search(r'<!-- Google tag.*?</script>\s*</script>|<!-- Google tag.*?</script>\n<script>.*?</script>', FR, re.S).group(0)
fonts = re.search(r'<link href="https://fonts.googleapis.com" rel="preconnect">.*?onload="this.media=\'all\'">', FR, re.S).group(0)
script = FR[FR.rfind('<script>'):FR.rfind('</body>')].replace("' espèces':' espèce'", "' species':' species'")

article = {
    '@context': 'https://schema.org', '@type': 'Article', 'headline': TITLE, 'description': DESC,
    'author': {'@type': 'Person', 'name': 'Lamine Faye', 'url': 'https://seggfaye.com/le-guedjologue.html',
               'jobTitle': 'Guedjologue', 'sameAs': ['https://www.tiktok.com/@seggfaye']},
    'publisher': {'@type': 'Organization', 'name': 'Louma by Seggfaye', 'url': 'https://seggfaye.com',
                  'logo': {'@type': 'ImageObject', 'url': 'https://seggfaye.com/logosite.webp'}},
    'datePublished': '2026-10-30T18:00:00+01:00', 'dateModified': '2026-10-30T18:00:00+01:00',
    'image': IMG, 'mainEntityOfPage': URL, 'inLanguage': 'en',
    'keywords': ['fish names in Wolof', 'Wolof fish names', 'Senegal fish names', 'fish in Wolof',
                 'Senegalese fish', 'thiof fish', 'yaboye', 'guedj'] + wolof_names,
}
crumbs = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
    {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://seggfaye.com/en/'},
    {'@type': 'ListItem', 'position': 2, 'name': 'Wolof fish names'}]}

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
{gtag}
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{TITLE} | Louma</title>
<meta name="description" content="{DESC}">
<link rel="canonical" href="{URL}">
<link rel="alternate" hreflang="en" href="{URL}">
<link rel="alternate" hreflang="fr" href="{FR_URL}">
<link rel="alternate" hreflang="x-default" href="{FR_URL}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:image" content="{IMG}">
<meta property="og:url" content="{URL}">
<meta property="og:type" content="article">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="fr_FR">
<meta property="og:site_name" content="Louma by Seggfaye">
<meta property="article:author" content="Lamine Faye">
<meta property="article:published_time" content="2026-10-30">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{TITLE}">
<meta name="twitter:description" content="{DESC}">
<meta name="twitter:image" content="{IMG}">
<script type="application/ld+json">
{json.dumps(article, ensure_ascii=False, indent=2)}
</script>
<script type="application/ld+json">
{json.dumps(crumbs, ensure_ascii=False, indent=2)}
</script>
{fonts}
{style}
</head>
<body>

<nav class="breadcrumb"><a href="/en/">Home</a> &gt; <span>Wolof fish names</span><a class="langlink" href="/atlas-poissons-wolof.html" hreflang="fr" lang="fr">Français</a></nav>

<div class="wrap">
<header>
  <p class="kicker">Louma by Seggfaye · the Guedjologue</p>
  <h1>Fish names <em>in Wolof</em></h1>
  <p class="hook">Every fish has a name before it has a price.</p>
  <p class="lede">The <strong>77 marine species of Senegal</strong> (fish, shellfish and crustaceans) with their <strong>Wolof</strong>, English, French and scientific names. The <strong>18 gold-bordered cards</strong> are the ones that become a product in our shop: one click opens the product page (in French).</p>
  <p class="src">Based on the charts <em>Espèces démersales</em> and <em>Espèces pélagiques marines du Sénégal</em> by the CRODT, Senegal’s oceanographic research centre, read at full zoom and cross-checked with the FishBase list of Wolof and Lebu names. Official Wolof is reproduced <strong>exactly</strong> as on the chart; when the chart misspells a Latin name, the valid scientific spelling is shown under the card.</p>
  <p class="src" style="margin-top:12px;"><strong>Two spellings, one fish.</strong> The chart writes Wolof in the official alphabet; markets and our shop use a French-style spelling: <em>c → th</em>, <em>x → kh</em>, <em>j → di</em>, <em>ñ → gn</em>. So <strong>Coof</strong> is the <strong>thiof</strong>, <strong>Njaane</strong> the <strong>diane</strong>, <strong>Sipax</strong> the <strong>cipakh</strong> shrimp, <strong>Paañ</strong> the <strong>pagne</strong>. The Latin name proves it every time.</p>
</header>

<div class="tools">
  <label class="search">
    <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="M20 20l-3.5-3.5"></path></svg>
    <input id="q" type="search" placeholder="Search: thiof, coof, yakh, meagre, cymbium…" aria-label="Search a species">
  </label>
  <div class="filters" role="group" aria-label="Filter by habitat">
    <button data-f="all" aria-pressed="true">All</button>
    <button data-f="fond" aria-pressed="false">Bottom fish</button>
    <button data-f="surface" aria-pressed="false">Surface fish</button>
    <button data-f="coq" aria-pressed="false">Shellfish &amp; crustaceans</button>
    <button data-f="raie" aria-pressed="false">Rays &amp; sharks</button>
    <button data-f="louma" aria-pressed="false">Sold at Louma</button>
  </div>
  <span class="count" id="count">77 species</span>
</div>

<div class="grid" id="grid">{grid}
  <p class="empty" id="empty" hidden>No name matches.</p>
</div>

<section class="debate">
  <h2>Four names settled in two days</h2>
  <p>A chart is not the truth: it is one more source. Four names contradicted each other from one source to another. They are now settled, and in three cases out of four the disagreement was not about the species but about the word.</p>
  <div class="rows">
    <div class="row"><h3>Diarégne<span>settled 11/09</span></h3><div>
      <p>Our product page said “diarégne (pageot)”. <b>That was wrong</b>: the pandora (pageot) is the <b>youfouf</b>, a Lebu name, <b>tikki</b> in Wolof.</p>
      <p>Diarégne comes from the Lebu <b>jaroñ</b>. It is the <b>pink dentex</b> (<span class="lat2">Dentex gibbosus</span>), called “<b>dent long fil</b>” in Senegalese markets, after the filament that extends its dorsal fin. And “dent long <b>fil</b>” is where the “<b>colas fil</b>” of French fishmongers comes from.</p></div></div>
    <div class="row"><h3>Plapla<span>settled 11/09</span></h3><div>
      <p>It is not a Wolof name. It is a <b>French nickname</b>: the diaspora does not know the fish’s name, sees that it is flat and says “<b>plat plat</b>” (flat flat).</p>
      <p>The word describes a shape, not a species, which is why the chart also gives it to <span class="lat2">Chloroscombrus chrysurus</span>, another flat fish. The fish sold under this name is the <b>ileer geej</b>, the African sicklefish.</p></div></div>
    <div class="row"><h3>Toufa<span>settled 11/09</span></h3><div>
      <p>Identified on fishing footage: lamellar ridges, high spire, spiky surface. It is a <b>murex</b>.</p>
      <p>Three matching clues: the shell has spikes, it must be <b>broken</b> to get the meat out, and it is collected <b>with the cockles</b>, which makes sense since the murex feeds on them. The chart calls it <b>yooxoñ</b>, but at Louma this word means the oysters. Same shell, two words.</p></div></div>
    <div class="row"><h3>Sompate<span>false conflict</span></h3><div>
      <p>The chart and FishBase give “sompatt” to two different grunts. But FishBase gives “sompaat” <b>and</b> “carpe blanche” (white carp) <b>to both</b>.</p>
      <p>“Sompate” is therefore a <b>market name</b> covering two close species, not the name of one species. There was nothing to settle.</p></div></div>
  </div>
  <p style="margin-top:26px;color:var(--text-3);font-size:14px;">Three of these four “contradictions” came from the same misunderstanding: <b>a word is not a species</b>. The chart names species; the market names shapes and uses. Both are right in their own way.</p>
</section>

<section class="sources">
  <h2>Sources and credits</h2>
  <p><strong>Names:</strong> CRODT charts <em>Espèces démersales</em> and <em>Espèces pélagiques marines du Sénégal</em>, FishBase Senegal, and market names validated by Lamine Faye, the Guedjologue.</p>
  <p><strong>Photos:</strong> Louma by Seggfaye for our shop products; Wikimedia Commons (free licences, author credited under each photo); DORIS (FFESSM), aquaportail.com, souslesmers.fr, iNaturalist and FishBase for the others. All rights remain with their authors. Are you the author of a photo and would like a different credit or its removal? <a href="https://wa.me/33652650395">Write to us</a>, it is done within 48 hours.</p>
  <p>A name is missing, or your village spells it differently? Tell us: the atlas grows with you.</p>
</section>

<nav class="links" aria-label="Read also">
  <a href="/en/cymbium-yeet.html">Cymbium (yeet), the sea snail →</a>
  <a href="/en/senegalese-food.html">Senegalese food: the dishes to know →</a>
  <a href="/en/thieboudienne-recipe.html">Thieboudienne recipe →</a>
  <a href="/en/shop.html">Our shop →</a>
  <a href="/atlas-poissons-wolof.html" hreflang="fr">Version française →</a>
</nav>
</div>

<footer class="site-footer">
  <p>Louma by Seggfaye &mdash; Authentic Senegalese food from the Îles du Saloum</p>
  <p style="margin-top:.3rem;"><a href="https://wa.me/33652650395">WhatsApp</a> &middot; <a href="https://www.tiktok.com/@seggfaye">TikTok</a> &middot; <a href="https://www.youtube.com/@loumaseggfaye">YouTube</a></p>
</footer>

{script}</body>
</html>
'''
os.makedirs(os.path.join(REPO, 'en'), exist_ok=True)
open(os.path.join(REPO, 'en', 'wolof-fish-names.html'), 'w', encoding='utf-8').write(html)
print('en/wolof-fish-names.html écrit :', len(cards), 'cartes,', len(html), 'octets')
