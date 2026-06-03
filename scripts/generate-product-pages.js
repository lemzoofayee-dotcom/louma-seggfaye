#!/usr/bin/env node
/**
 * Générateur de pages produits SEO — Louma by Seggfaye
 * Lit produits.js et génère /produits/[slug].html pour chaque produit
 * Usage : node scripts/generate-product-pages.js
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const OUT_DIR = path.join(ROOT, 'produits');

// Charger produits.js (extraire le tableau PRODUITS)
const src = fs.readFileSync(path.join(ROOT, 'produits.js'), 'utf8');
// Couper avant le code browser (fonctions DOM + window + document)
const dataOnly = src
  .split(/\nfunction\s+build/)[0]  // couper avant buildWhatsAppUrl/buildProdCard
  .replace('const PRODUITS', 'var PRODUITS');
const extractProduits = new Function(`${dataOnly}; return PRODUITS;`);
const PRODUITS = extractProduits();

const CAT_LABELS = {
  mer: 'Fruits de mer',
  epices: 'Épices & Condiments',
  cereales: 'Céréales & Farines',
  beurres: 'Pâtes & Beurres',
  frais: 'Poissons Frais'
};

// Descripteur commercial FR par catégorie — injecté dans <title> + meta description
// pour se positionner sur les recherches à fort volume (le wolof n'a pas de graphie fixe).
const CAT_SEO = {
  mer:      'Produit halieutique séché du Sénégal',
  frais:    'Poisson frais du Sénégal',
  epices:   'Épice et condiment sénégalais',
  cereales: 'Céréale et farine africaine',
  beurres:  'Pâte et beurre africain du Sénégal'
};

// Mapping catégorie produit -> slug de la page catégorie (pour le maillage interne)
const CAT_PAGES = {
  mer: 'produits-halieutiques',
  epices: 'epices-condiments',
  cereales: 'cereales-farines',
  beurres: 'pates-beurres',
  frais: 'poissons-frais'
};

// Variantes orthographiques par produit (clé = morceau de l'id) — pour RATISSER LARGE
// dans les meta keywords uniquement (capte toutes les graphies cherchées sur Google).
const KEYWORD_VARIANTS = {
  'guej':       ['guedj', 'guej', 'guedji'],
  'yoxos':      ['yoxos', 'yokhos', 'yokhoss', 'huitres sechees', 'huitres de mangrove'],
  'tuffa':      ['tuffa', 'touffa', 'escargot de mer seche'],
  'yeet':       ['yeet', 'yett', 'yet', 'cymbium', 'maggi africain'],
  'kongfume':   ['kong fume', 'kongfume', 'kong fumé'],
  'toumboulan': ['toumboulan', 'toumboulane'],
  'beur':       ['guedj beurre', 'guedj berr', 'courbine sechee'],
  'pagne':      ['pagne', 'coques sechees'],
  'crevettes':  ['crevettes sechees', 'cipakh'],
  'keciax':     ['keciax', 'kethiakh', 'ketiakh', 'poisson seche fermente', 'guedj kethiakh'],
};

function buildKeywords(p, catLabel) {
  const set = new Set();
  const add = v => { if (v) set.add(String(v).toLowerCase().trim()); };
  add(p.nom);
  add(p.nomLocal);
  for (const [root, vars] of Object.entries(KEYWORD_VARIANTS)) {
    if (p.id.includes(root)) vars.forEach(add);
  }
  // Termes commerciaux FR à fort volume : le wolof n'a pas de graphie fixe,
  // donc on se positionne sur les recherches descriptives françaises (= les clics).
  const BY_CAT = {
    mer:      ['produit halieutique seche', 'produits halieutiques senegal', 'mollusque seche', 'fruits de mer seches', 'poisson seche senegalais'],
    frais:    ['poisson frais senegal', 'poisson congele africain', 'produits halieutiques'],
    epices:   ['epices africaines', 'condiments africains'],
    cereales: ['cereales africaines', 'farines africaines'],
    beurres:  ['pate d arachide', 'beurre africain', 'huile de palme'],
  };
  const COMMON = ['produit senegalais', 'produits exotiques senegal', 'produits exotiques africains',
                  'epicerie africaine en ligne', 'iles du saloum', 'cuisine senegalaise'];
  [catLabel, ...(BY_CAT[p.categorie] || []), ...COMMON].forEach(add);
  return [...set].join(', ');
}

function slugify(str) {
  return str.toLowerCase()
    .normalize('NFD').replace(/[̀-ͯ]/g, '')
    .replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

function escapeHtml(s) {
  if (!s) return '';
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function generatePage(p, allProducts) {
  const catLabel = CAT_LABELS[p.categorie] || p.categorie;
  const keywords = buildKeywords(p, catLabel);
  const catPage = CAT_PAGES[p.categorie];
  const catUrl = catPage ? `/categories/${catPage}.html` : '/#produits';

  // Produits similaires : jusqu'à 4 autres produits de la même catégorie (maillage interne statique)
  const similaires = (allProducts || [])
    .filter(x => x.categorie === p.categorie && x.id !== p.id && x.stock !== false)
    .slice(0, 4);
  const similairesHtml = similaires.length ? `
      <div class="detail-block">
        <h2>Produits similaires</h2>
        <div class="similar-grid">
          ${similaires.map(s => `<a class="similar-card" href="/produits/${s.id}.html">
            <img src="/${escapeHtml(s.image || 'logosite.webp')}" alt="${escapeHtml(s.nom)}" loading="lazy">
            <span>${escapeHtml(s.nom)}</span>
          </a>`).join('\n          ')}
        </div>
        <p style="margin-top:1rem;"><a href="${catUrl}">Voir toute la catégorie ${escapeHtml(catLabel)} →</a></p>
      </div>` : '';
  const seoDesc = CAT_SEO[p.categorie] || catLabel;
  // Titre = nom + descripteur commercial FR (le nomLocal reste en H1/sous-titre/JSON-LD)
  const title = `${p.nom} — ${seoDesc} | Louma by Seggfaye`;
  // Meta description = descripteur commercial en tête (pour le snippet Google) + storytelling.
  // Le texte VISIBLE de la fiche garde p.description brut (storytelling intact).
  const rawDesc = p.description
    ? `${seoDesc} — ${p.description}`
    : `${p.nom} — ${seoDesc}. Livraison France & Europe.`;
  const desc = rawDesc.replace(/\n/g, ' ').substring(0, 160);
  const prix = p.prix ? p.prix.toFixed(2) : '';
  const image = p.image || 'logosite.jpg';
  const ogImage = `https://seggfaye.com/${image}`;

  // Gallery
  const galleryHtml = (p.gallery && p.gallery.length > 1)
    ? p.gallery.map((img, i) => `
        <img src="/${escapeHtml(img)}" alt="${escapeHtml(p.nom)} — photo ${i+1}"
             class="gallery-thumb${i===0?' active':''}" loading="lazy"
             onclick="document.getElementById('main-img').src=this.src;document.querySelectorAll('.gallery-thumb').forEach(t=>t.classList.remove('active'));this.classList.add('active');">`
    ).join('\n        ')
    : '';

  // Sections optionnelles
  const origineHtml = p.origine ? `
      <div class="detail-block">
        <h2>Origine</h2>
        <p>${escapeHtml(p.origine)}</p>
      </div>` : '';

  const goutHtml = p.goutPlus ? `
      <div class="detail-block">
        <h2>Pourquoi c'est différent</h2>
        <p>${escapeHtml(p.goutPlus)}</p>
      </div>` : '';

  const conseilHtml = p.conseil ? `
      <div class="detail-block">
        <h2>Comment l'utiliser</h2>
        <p>${escapeHtml(p.conseil)}</p>
      </div>` : '';

  const stockBadge = p.stock === false
    ? '<span class="badge badge-rupture">Rupture</span>'
    : (p.badge ? `<span class="badge badge-${slugify(p.badge)}">${escapeHtml(p.badge)}</span>` : '');

  const prixAncienHtml = p.prixAncien
    ? `<span class="prix-ancien">${p.prixAncien.toFixed(2)}€</span>` : '';

  return `<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${escapeHtml(title)}</title>
<meta name="description" content="${escapeHtml(desc)}">
<meta name="keywords" content="${escapeHtml(keywords)}">
<link rel="canonical" href="https://seggfaye.com/produits/${p.id}.html">
<!-- Open Graph -->
<meta property="og:title" content="${escapeHtml(title)}">
<meta property="og:description" content="${escapeHtml(desc)}">
<meta property="og:image" content="${ogImage}">
<meta property="og:url" content="https://seggfaye.com/produits/${p.id}.html">
<meta property="og:type" content="product">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="Louma by Seggfaye">
<meta property="product:price:amount" content="${prix}">
<meta property="product:price:currency" content="EUR">
<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${escapeHtml(title)}">
<meta name="twitter:description" content="${escapeHtml(desc)}">
<meta name="twitter:image" content="${ogImage}">
<!-- Schema Product JSON-LD -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "${p.nom}${p.nomLocal ? ` (${p.nomLocal})` : ''}",
  "description": ${JSON.stringify(p.description || desc)},
  "image": "${ogImage}",
  "brand": {
    "@type": "Brand",
    "name": "Louma by Seggfaye"
  },
  "offers": {
    "@type": "Offer",
    "price": "${prix}",
    "priceCurrency": "EUR",
    "availability": "https://schema.org/${p.stock !== false ? 'InStock' : 'OutOfStock'}",
    "seller": {
      "@type": "Organization",
      "name": "Louma by Seggfaye",
      "url": "https://seggfaye.com"
    }
  },
  "category": "${catLabel}"
}
</script>
<!-- Schema BreadcrumbList -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://seggfaye.com/"},
    {"@type": "ListItem", "position": 2, "name": "${catLabel}", "item": "https://seggfaye.com${catUrl}"},
    {"@type": "ListItem", "position": 3, "name": "${p.nom}"}
  ]
}
</script>
<link href="https://fonts.googleapis.com" rel="preconnect">
<link crossorigin href="https://fonts.gstatic.com" rel="preconnect">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root {
  --bg: #100d08; --bg-2: #161210; --card: #1a1612;
  --gold: #c9a84c; --cream: #f1e8d8; --muted: #8a7e6a;
  --border: rgba(201,168,76,.12); --border-hi: rgba(201,168,76,.35);
}
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:'Plus Jakarta Sans',system-ui,sans-serif; background:var(--bg); color:var(--cream); line-height:1.7; }
a { color:var(--gold); text-decoration:none; }
a:hover { text-decoration:underline; }

.breadcrumb { padding:1rem 1.5rem; font-size:.8rem; color:var(--muted); max-width:900px; margin:0 auto; }
.breadcrumb a { color:var(--muted); }
.breadcrumb span { color:var(--gold); }

.product-page { max-width:900px; margin:0 auto; padding:0 1.5rem 4rem; }
.product-hero { display:grid; grid-template-columns:1fr 1fr; gap:2.5rem; margin-bottom:2.5rem; }
@media(max-width:700px) { .product-hero { grid-template-columns:1fr; } }

.product-gallery { display:flex; flex-direction:column; gap:.6rem; }
#main-img { width:100%; border-radius:.8rem; border:1px solid var(--border); aspect-ratio:1; object-fit:cover; }
.gallery-thumbs { display:flex; gap:.5rem; }
.gallery-thumb { width:64px; height:64px; border-radius:.4rem; border:2px solid transparent; object-fit:cover; cursor:pointer; opacity:.6; transition:all .2s; }
.gallery-thumb.active, .gallery-thumb:hover { border-color:var(--gold); opacity:1; }

.product-info { display:flex; flex-direction:column; gap:1rem; }
.product-cat { font-size:.72rem; font-weight:700; letter-spacing:.2em; text-transform:uppercase; color:var(--gold); }
h1 { font-family:'Playfair Display',serif; font-size:2.2rem; font-weight:900; line-height:1.15; color:var(--cream); }
.nom-local { font-family:'Playfair Display',serif; font-style:italic; font-weight:400; font-size:1.1rem; color:var(--gold); opacity:.7; }
.product-desc { font-size:.95rem; color:var(--muted); line-height:1.8; }
.prix-block { display:flex; align-items:baseline; gap:.8rem; margin:.5rem 0; }
.prix { font-size:1.8rem; font-weight:800; color:var(--cream); }
.prix-unite { font-size:.8rem; color:var(--muted); }
.prix-ancien { font-size:1rem; color:var(--muted); text-decoration:line-through; }
.badge { display:inline-block; padding:.25rem .7rem; border-radius:2rem; font-size:.68rem; font-weight:700; letter-spacing:.08em; text-transform:uppercase; }
.badge-bestseller { background:var(--gold); color:var(--bg); }
.badge-nouveau { background:#2a5a3a; color:#7ddf9b; }
.badge-rupture { background:#5a2a2a; color:#df7d7d; }

.btn-wa { display:inline-flex; align-items:center; gap:.5rem; padding:.9rem 2rem; background:#25D366; color:#fff; font-weight:700; font-size:.95rem; border-radius:.6rem; border:none; cursor:pointer; transition:transform .15s; }
.btn-wa:hover { transform:translateY(-2px); text-decoration:none; }

.detail-block { padding:1.5rem 0; border-top:1px solid var(--border); }
.detail-block h2 { font-family:'Playfair Display',serif; font-size:1.2rem; font-weight:700; color:var(--cream); margin-bottom:.5rem; }
.detail-block p { font-size:.9rem; color:var(--muted); }

.back-link { display:inline-flex; align-items:center; gap:.4rem; padding:1rem 0; font-size:.85rem; color:var(--gold); }

.similar-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:1rem; margin-top:1rem; }
@media(max-width:600px) { .similar-grid { grid-template-columns:repeat(2,1fr); } }
.similar-card { display:flex; flex-direction:column; gap:.5rem; font-size:.8rem; color:var(--cream); }
.similar-card img { width:100%; aspect-ratio:1; object-fit:cover; border-radius:.5rem; border:1px solid var(--border); transition:border-color .2s; }
.similar-card:hover { text-decoration:none; }
.similar-card:hover img { border-color:var(--gold); }

footer { text-align:center; padding:2rem; font-size:.75rem; color:var(--muted); border-top:1px solid var(--border); }
footer .footer-links { margin-top:.6rem; }
footer .footer-links a { color:var(--muted); margin:0 .4rem; }
</style>
</head>
<body>

<nav class="breadcrumb">
  <a href="/">Accueil</a> › <a href="${catUrl}">${catLabel}</a> › <span>${escapeHtml(p.nom)}</span>
</nav>

<main class="product-page">
  <div class="product-hero">
    <div class="product-gallery">
      <img id="main-img" src="/${escapeHtml(image)}" alt="${escapeHtml(p.nom)}${p.nomLocal ? ` — ${escapeHtml(p.nomLocal)}` : ''} — Louma by Seggfaye">
      ${galleryHtml ? `<div class="gallery-thumbs">${galleryHtml}</div>` : ''}
    </div>

    <div class="product-info">
      <div class="product-cat">${escapeHtml(catLabel)}</div>
      ${stockBadge}
      <h1>${escapeHtml(p.nom)}</h1>
      ${p.nomLocal ? `<div class="nom-local">${escapeHtml(p.nomLocal)}</div>` : ''}
      ${p.description ? `<p class="product-desc">${escapeHtml(p.description)}</p>` : ''}
      <div class="prix-block">
        ${prixAncienHtml}
        <span class="prix">${prix}€</span>
        ${p.unite ? `<span class="prix-unite">${escapeHtml(p.unite)}</span>` : ''}
      </div>
      ${p.stock !== false
        ? `<a class="btn-wa" href="https://wa.me/33652650395?text=${encodeURIComponent(`Bonjour, je voudrais commander : ${p.nom}`)}" target="_blank">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 0C5.373 0 0 5.373 0 12c0 2.120.553 4.113 1.519 5.845L.038 23.382a.5.5 0 00.608.608l5.537-1.481A11.955 11.955 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 22c-1.946 0-3.79-.566-5.34-1.544l-.382-.233-3.29.88.88-3.29-.233-.382A9.96 9.96 0 012 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10z"/></svg>
            Commander sur WhatsApp
           </a>`
        : '<p style="color:#df7d7d;font-weight:600;">Temporairement en rupture de stock</p>'}
    </div>
  </div>
${origineHtml}${goutHtml}${conseilHtml}${similairesHtml}
  <a class="back-link" href="${catUrl}">← Retour à ${catLabel}</a>
</main>

<footer>
  <p>Louma by Seggfaye — Votre marché africain authentique</p>
  <p class="footer-links"><a href="/">Accueil</a> · <a href="${catUrl}">${catLabel}</a> · <a href="/blog/">Blog</a></p>
  <p style="margin-top:.3rem;"><a href="https://wa.me/33652650395">WhatsApp</a> · <a href="https://www.tiktok.com/@seggfaye">TikTok</a></p>
</footer>

</body>
</html>`;
}

// Générer toutes les pages
if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR, { recursive: true });

let count = 0;
const sitemapEntries = [];

for (const p of PRODUITS) {
  const html = generatePage(p, PRODUITS);
  const filePath = path.join(OUT_DIR, `${p.id}.html`);
  fs.writeFileSync(filePath, html, 'utf8');
  count++;
  sitemapEntries.push(`  <url>\n    <loc>https://seggfaye.com/produits/${p.id}.html</loc>\n    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>`);
}

// Mettre à jour sitemap.xml
const sitemapPath = path.join(ROOT, 'sitemap.xml');
let sitemap = fs.readFileSync(sitemapPath, 'utf8');
// Supprimer anciennes entrées produits s'il y en a
sitemap = sitemap.replace(/\n  <!-- PRODUITS -->[^]*<!-- \/PRODUITS -->\n/g, '');
// Insérer avant </urlset>
const productBlock = `\n  <!-- PRODUITS -->\n${sitemapEntries.join('\n')}\n  <!-- /PRODUITS -->\n`;
sitemap = sitemap.replace('</urlset>', `${productBlock}</urlset>`);
fs.writeFileSync(sitemapPath, sitemap, 'utf8');

console.log(`✅ ${count} pages produits générées dans /produits/`);
console.log(`✅ sitemap.xml mis à jour (${3 + count} URLs)`);
