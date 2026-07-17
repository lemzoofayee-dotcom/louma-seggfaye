// Génère flux-google-shopping.xml (racine du site) depuis produits.js
// Usage : node scripts/google-shopping/generer_flux.js
// Format : RSS 2.0 + namespace g: (Google Merchant Center, fiches gratuites)
const fs = require('fs');
const path = require('path');

const repo = path.join(__dirname, '..', '..');
const code = fs.readFileSync(path.join(repo, 'produits.js'), 'utf8');
const windowStub = {};
const documentStub = { addEventListener() {}, querySelector() { return null; }, querySelectorAll() { return []; } };
const PRODUITS = new Function('window', 'document', code + '\nreturn PRODUITS;')(windowStub, documentStub);

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

const CATEGORIES = {
  mer: 'Poissons séchés & fruits de mer',
  epices: 'Épices & condiments',
  cereales: 'Céréales & farines',
  beurres: 'Pâtes & beurres',
  frais: 'Poissons frais'
};

const warnings = [];
const items = PRODUITS.map(p => {
  const fiche = path.join(repo, 'produits', `${p.id}.html`);
  if (!fs.existsSync(fiche)) warnings.push(`fiche manquante : produits/${p.id}.html`);
  if (!p.image) warnings.push(`image absente : ${p.id}`);
  else if (!fs.existsSync(path.join(repo, p.image))) warnings.push(`image introuvable : ${p.id} → ${p.image}`);

  const poids = (p.unite || '').replace(/^par\s+/i, '');
  const title = `${p.nom}${p.nomLocal && p.nomLocal.toLowerCase() !== p.nom.toLowerCase() ? ` (${p.nomLocal})` : ''}${poids ? ` — ${poids}` : ''}`;
  const description = p.description
    || `${p.nom} — produit sénégalais authentique sélectionné par Louma by Seggfaye.${p.origine ? ` Origine : ${p.origine}.` : ''}`;

  return `  <item>
    <g:id>${esc(p.id)}</g:id>
    <g:title>${esc(title)}</g:title>
    <g:description>${esc(description)}</g:description>
    <g:link>https://seggfaye.com/produits/${esc(p.id)}.html</g:link>
    <g:image_link>https://seggfaye.com/${esc(p.image)}</g:image_link>
    <g:price>${p.prix.toFixed(2)} EUR</g:price>
    <g:availability>${p.stock ? 'in_stock' : 'out_of_stock'}</g:availability>
    <g:condition>new</g:condition>
    <g:brand>Louma by Seggfaye</g:brand>
    <g:identifier_exists>false</g:identifier_exists>
    <g:product_type>${esc(CATEGORIES[p.categorie] || p.categorie)}</g:product_type>
    <g:google_product_category>Food, Beverages &amp; Tobacco &gt; Food Items</g:google_product_category>
  </item>`;
});

const xml = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0">
<channel>
  <title>Louma by Seggfaye — Catalogue produits</title>
  <link>https://seggfaye.com</link>
  <description>Marché africain authentique en ligne : guedj, poissons séchés, épices et céréales du Sénégal.</description>
${items.join('\n')}
</channel>
</rss>
`;

fs.writeFileSync(path.join(repo, 'flux-google-shopping.xml'), xml);
console.log(`${PRODUITS.length} produits écrits dans flux-google-shopping.xml (${PRODUITS.filter(p => p.stock).length} in_stock, ${PRODUITS.filter(p => !p.stock).length} out_of_stock)`);
if (warnings.length) { console.log('\n⚠️ AVERTISSEMENTS :'); warnings.forEach(w => console.log(' - ' + w)); }
else console.log('Aucun avertissement : fiches + images toutes présentes.');
