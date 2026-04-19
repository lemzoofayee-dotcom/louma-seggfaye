// ═══════════════════════════════════════════════════
//  LOUMA by Seggfaye — Catalogue produits
//  Pour modifier un produit : changer les valeurs ici
//  stock: true = disponible | false = rupture de stock
//  nouveaute: true = badge "Nouveau" affiché
// ═══════════════════════════════════════════════════

const PRODUITS = [

  // ──────────────────────────────────────
  //  🐟 FRUITS DE MER
  // ──────────────────────────────────────
  {
    id: "crevettes-sechees",
    nom: "Crevettes séchées",
    categorie: "mer",
    prix: 6.00,
    unite: "par 100g",
    prixAncien: null,
    badge: "Bestseller",
    image: "crevettesechees.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "yoxos",
    nom: "Yoxos (huîtres secs)",
    categorie: "mer",
    prix: 6.00,
    unite: "par 100g",
    prixAncien: null,
    badge: null,
    image: "yohos.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "pagne",
    nom: "Pagne (coques)",
    categorie: "mer",
    prix: 6.00,
    unite: "par 100g",
    prixAncien: null,
    badge: null,
    image: "pagne-conv.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "tuffa",
    nom: "Tuffa",
    categorie: "mer",
    prix: 6.00,
    unite: "par 100g",
    prixAncien: null,
    badge: null,
    image: "tuffa.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "yeet-maggi",
    nom: "Yeet Maggi",
    categorie: "mer",
    prix: 6.00,
    unite: "par 100g",
    prixAncien: null,
    badge: null,
    image: "yeet.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "guej-yass",
    nom: "Guej Yass",
    categorie: "mer",
    prix: 6.00,
    unite: "par 100g",
    prixAncien: 7.00,
    badge: null,
    image: "guedj-yass.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "guej-beurre",
    nom: "Guej Beurre",
    categorie: "mer",
    prix: 4.00,
    unite: "par 100g",
    prixAncien: 6.00,
    badge: null,
    image: "guedji-beurre.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "guej-beur-casamance",
    nom: "Guej Beur Casamance",
    categorie: "mer",
    prix: 12.00,
    unite: "par 300g",
    prixAncien: 18.00,
    badge: "Casamance",
    image: "guedji-beur_casamance.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "guej-sol",
    nom: "Guej Sole",
    categorie: "mer",
    prix: 4.00,
    unite: "par 100g",
    prixAncien: 6.00,
    badge: null,
    image: "guedji-sole-retouche.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "guej-kong",
    nom: "Guej Kong",
    categorie: "mer",
    prix: 3.00,
    unite: "par 100g",
    prixAncien: 5.00,
    badge: null,
    image: "Guedji-kong.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "guej-tambajang",
    nom: "Guej Tambajang",
    categorie: "mer",
    prix: 3.00,
    unite: "par 100g",
    prixAncien: 5.00,
    badge: null,
    image: "guedji-tambajang-retouche.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "guej-toumboulan",
    nom: "Guej Toumboulan",
    categorie: "mer",
    prix: 3.00,
    unite: "par 100g",
    prixAncien: 5.00,
    badge: null,
    image: "guedji-toumboulane.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "guerte-tooy",
    nom: "Guerte Tooy",
    categorie: "cereales",
    prix: 8.00,
    unite: "par kg",
    prixAncien: null,
    badge: null,
    image: "guerte-toye.jpg",
    stock: false,
    nouveaute: false
  },
  {
    id: "kongfume",
    nom: "Kongfume",
    categorie: "mer",
    prix: 30.00,
    unite: "par 500g",
    prixAncien: 35.00,
    badge: "Fumé",
    image: "kong-fume-sec.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "kongfume-gambie",
    nom: "Kongfume Gambie",
    categorie: "mer",
    prix: 30.00,
    unite: "par 500g",
    prixAncien: null,
    badge: "Gambie",
    image: "kong-fume1.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "pack-saloum",
    nom: "Pack Saloum",
    categorie: "mer",
    prix: 60.00,
    unite: "par kg",
    prixAncien: null,
    badge: "Pack 4 produits",
    image: "packsaloum-sachetdebout1.jpg",
    stock: true,
    nouveaute: false
  },

  // ──────────────────────────────────────
  //  🌿 ÉPICES & CONDIMENTS
  // ──────────────────────────────────────
  {
    id: "netetu-dom",
    nom: "Netetu Dom",
    categorie: "epices",
    prix: 5.00,
    unite: "par 100g",
    prixAncien: 6.00,
    badge: null,
    image: "netetou-dome.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "netetu-barre",
    nom: "Netetu Barre",
    categorie: "epices",
    prix: 5.00,
    unite: "par 100g",
    prixAncien: 6.00,
    badge: null,
    image: "netetou-barre.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "netetu-mix",
    nom: "Netetu Mix",
    categorie: "epices",
    prix: 15.00,
    unite: "par 200g",
    prixAncien: 20.00,
    badge: "Mix",
    image: "netetou-mixte.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "netetu-poudre",
    nom: "Netetu simple poudre",
    categorie: "epices",
    prix: 5.00,
    unite: "par 100g",
    prixAncien: 6.00,
    badge: null,
    image: "netetou-poudre.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "sauce-netetu-beugeuc",
    nom: "Sauce Netetu Beugeuc",
    categorie: "epices",
    prix: 10.00,
    unite: "250g",
    prixAncien: null,
    badge: "Sauce",
    image: "sauce-netetou.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "beugeuc-feuille-bissap",
    nom: "Beugeuc Feuille Bissap",
    categorie: "epices",
    prix: 10.00,
    unite: "300g",
    prixAncien: 15.00,
    badge: "Bissap",
    image: "beugeuth-bissap2.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "keciax",
    nom: "Keciax",
    categorie: "epices",
    prix: 3.00,
    unite: "par 100g",
    prixAncien: 5.00,
    badge: null,
    image: "Guedji-kethiakh.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "bissap-rouge",
    nom: "Bissap Rouge",
    categorie: "epices",
    prix: 5.00,
    unite: "par 150g",
    prixAncien: 6.00,
    badge: "Bissap",
    image: "Bissap-rouge.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "bissap-blanc",
    nom: "Bissap Blanc",
    categorie: "epices",
    prix: 5.00,
    unite: "par 200g",
    prixAncien: 6.00,
    badge: "Bissap",
    image: "Bissap-blanc.jpg",
    stock: false,
    nouveaute: false
  },
  {
    id: "bouye-baobab",
    nom: "Bouye (poudre baobab)",
    categorie: "epices",
    prix: 6.00,
    unite: "par 200g",
    prixAncien: null,
    badge: "Baobab",
    image: "poudre-baobab.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "puree-piment",
    nom: "Purée Piment Fort",
    categorie: "epices",
    prix: 10.00,
    unite: "200g",
    prixAncien: 12.00,
    badge: "Piment",
    image: "kani-puree.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "maad-confi",
    nom: "Maad Confi",
    categorie: "epices",
    prix: 25.00,
    unite: "par kg",
    prixAncien: null,
    badge: "Confiture",
    image: "maad-confi2.jpg",
    stock: true,
    nouveaute: false
  },

  // ──────────────────────────────────────
  //  🌾 CÉRÉALES & FARINES
  // ──────────────────────────────────────
  {
    id: "thiere-champion",
    nom: "Thiéré (couscous de mil)",
    categorie: "cereales",
    prix: 18.00,
    unite: "par kg",
    prixAncien: null,
    badge: "🏆 Champion du Monde",
    image: "thiackry.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "arraw-dugup",
    nom: "Arraw Dugup (mil)",
    categorie: "cereales",
    prix: 18.00,
    unite: "par kg",
    prixAncien: null,
    badge: "Mil",
    image: "arraw.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "ciakri",
    nom: "Ciakri",
    categorie: "cereales",
    prix: 18.00,
    unite: "par kg",
    prixAncien: null,
    badge: "Couscous",
    image: "thiackry.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "sankal-duggup",
    nom: "Sankal Duggup",
    categorie: "cereales",
    prix: 9.00,
    unite: "500g",
    prixAncien: null,
    badge: null,
    image: "sankal.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "niebe-saloum",
    nom: "Niebe Saloum",
    categorie: "cereales",
    prix: 5.00,
    unite: "250g",
    prixAncien: 6.00,
    badge: "Saloum",
    image: "niebe-saloum.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "guerte-noflay",
    nom: "Guerte Noflay",
    categorie: "cereales",
    prix: 5.00,
    unite: "par 250g",
    prixAncien: 7.00,
    badge: "Poudre arachide",
    image: "Guerte-noflay.jpg",
    stock: true,
    nouveaute: false
  },

  // ──────────────────────────────────────
  //  🫙 PÂTES & BEURRES
  // ──────────────────────────────────────
  {
    id: "tiguadegue-500",
    nom: "Tiguadegue (pâte d'arachide)",
    categorie: "beurres",
    prix: 12.00,
    unite: "500g",
    prixAncien: null,
    badge: "Pâte arachide",
    image: "tiagadegue.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "tigadegue-250",
    nom: "Tigadégué",
    categorie: "beurres",
    prix: 6.00,
    unite: "par 250g",
    prixAncien: null,
    badge: "Pâte arachide",
    image: "tiagadegue.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "diwnior-500",
    nom: "Diwnior (beurre clarifié)",
    categorie: "beurres",
    prix: 20.00,
    unite: "par 0,5L",
    prixAncien: 25.00,
    badge: "Beurre vache",
    image: "diwnior.jpg",
    stock: false,
    nouveaute: false
  },
  {
    id: "diwnior-1l",
    nom: "Diwnior (beurre clarifié)",
    categorie: "beurres",
    prix: 40.00,
    unite: "par 1L",
    prixAncien: null,
    badge: "Beurre vache",
    image: "diwnior.jpg",
    stock: false,
    nouveaute: false
  },
  {
    id: "diwtir-pure",
    nom: "Diwtir Pure",
    categorie: "beurres",
    prix: 25.00,
    unite: "par 1L",
    prixAncien: 30.00,
    badge: "Huile",
    image: "diwtir.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "lem-miel",
    nom: "Lem miel Pure",
    categorie: "beurres",
    prix: 25.00,
    unite: "1,5L",
    prixAncien: 27.00,
    badge: "Miel",
    image: "lem-pure.jpg",
    stock: true,
    nouveaute: false
  },

  // ──────────────────────────────────────
  //  🐠 POISSONS FRAIS (cartons 5kg)
  // ──────────────────────────────────────
  {
    id: "thiof-decoupe",
    nom: "Thiof découpé",
    categorie: "frais",
    prix: 55.00,
    unite: "carton 5kg",
    prixAncien: null,
    badge: "Carton 5kg",
    image: "thiof.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "diargne-colafil",
    nom: "Diarégne Colafil",
    categorie: "frais",
    prix: 49.00,
    unite: "carton 5kg",
    prixAncien: null,
    badge: "Carton 5kg",
    image: "sompate2.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "beurre-capitaine",
    nom: "Beurre (Capitaine)",
    categorie: "frais",
    prix: 45.00,
    unite: "carton 5kg",
    prixAncien: null,
    badge: "Carton 5kg",
    image: "thiof4.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "chanchar-dieye",
    nom: "Chanchar (Diéye)",
    categorie: "frais",
    prix: 25.00,
    unite: "carton 5kg",
    prixAncien: null,
    badge: "Carton 5kg",
    image: "yakh4.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "poisson-eau-douce",
    nom: "Poisson Eau Douce",
    categorie: "frais",
    prix: 10.00,
    unite: "carton 5kg",
    prixAncien: null,
    badge: "Carton 5kg",
    image: "sompate3.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "yaye-boye",
    nom: "Yaye Boye",
    categorie: "frais",
    prix: 7.50,
    unite: "/ kilo",
    prixAncien: null,
    badge: "Au kilo",
    image: "yaboye.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "poisson-sompate",
    nom: "Poisson Sompate",
    categorie: "frais",
    prix: 45.00,
    unite: "carton 5kg",
    prixAncien: null,
    badge: "Carton 5kg",
    image: "sompate.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "tilapia-rouge",
    nom: "Tilapia Rouge",
    categorie: "frais",
    prix: 22.00,
    unite: "carton 5kg",
    prixAncien: null,
    badge: "Carton 5kg",
    image: "yakh.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "seude-baracouda",
    nom: "Seude Baracouda",
    categorie: "frais",
    prix: 40.00,
    unite: "carton 5kg",
    prixAncien: null,
    badge: "Carton 5kg",
    image: "seude.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "yakh-carpe-rouge",
    nom: "Yakh (Carpe Rouge)",
    categorie: "frais",
    prix: 60.00,
    unite: "carton 5kg",
    prixAncien: null,
    badge: "Carton 5kg",
    image: "yakh2.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "iler-bi",
    nom: "Iler Bi (Plapla)",
    categorie: "frais",
    prix: 45.00,
    unite: "carton 5kg",
    prixAncien: null,
    badge: "Carton 5kg",
    image: "iler.jpg",
    stock: true,
    nouveaute: false
  },
  {
    id: "melange-poisson-10kg",
    nom: "Mélange de Poisson 10kg",
    categorie: "frais",
    prix: 110.00,
    unite: "carton 10kg",
    prixAncien: null,
    badge: "⭐ Best Deal",
    image: "melange-poisson.jpg",
    stock: true,
    nouveaute: false
  }

];

// ═══════════════════════════════════════════════════
//  Générateur de cartes produits
// ═══════════════════════════════════════════════════

function formatPrix(prix) {
  return prix.toFixed(2).replace('.', ',') + ' €';
}

function buildWhatsAppUrl(nom) {
  const msg = encodeURIComponent('Bonjour, je souhaite commander : ' + nom);
  return 'https://wa.me/33652650395?text=' + msg;
}

function buildProdCard(p) {
  const imgContent = p.image
    ? `<img alt="${p.nom}" src="${p.image}" style="width:100%;height:100%;object-fit:cover;"/>`
    : `<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;font-size:3rem;">📦</div>`;

  let badgeHtml = '';
  if (!p.stock) {
    badgeHtml = `<div class="prod-badge" style="background:#c0392b;color:#fff;">Rupture de stock</div>`;
  } else if (p.nouveaute) {
    badgeHtml = `<div class="prod-badge" style="background:#2ecc71;color:#fff;">Nouveau</div>`;
  } else if (p.badge) {
    const isSpecial = p.badge === '⭐ Best Deal';
    const style = isSpecial ? ' style="background:#c9a84c;color:#100d08;"' : '';
    badgeHtml = `<div class="prod-badge"${style}>${p.badge}</div>`;
  }

  const prixAncienHtml = p.prixAncien
    ? `<span class="prod-price-old">${formatPrix(p.prixAncien)}</span>`
    : '';

  const btnHtml = p.stock
    ? `<a class="btn-sm" href="${buildWhatsAppUrl(p.nom)}" target="_blank">Commander →</a>`
    : `<span class="btn-sm" style="opacity:.35;cursor:not-allowed;pointer-events:none;">Indisponible</span>`;

  return `
<div class="prod-card reveal${!p.stock ? ' out-of-stock' : ''}">
  <div class="prod-img-shell">
    <div class="prod-img-core">${imgContent}</div>
    <div class="prod-img-overlay">${p.nom}</div>
  </div>
  <div class="prod-body">
    ${badgeHtml}<div class="prod-name">${p.nom}</div>
    <div class="prod-footer">
      <div class="prod-price">${formatPrix(p.prix)} <small>${p.unite}</small>${prixAncienHtml}</div>
      ${btnHtml}
    </div>
  </div>
</div>`.trim();
}

function renderProduits() {
  const categories = ['mer', 'epices', 'cereales', 'beurres', 'frais'];
  categories.forEach(cat => {
    const grid = document.querySelector(`#cat-${cat} .cat-grid`);
    if (!grid) return;
    const produitsCat = PRODUITS.filter(p => p.categorie === cat);
    grid.innerHTML = produitsCat.map(buildProdCard).join('');
  });

  // Re-observer les nouvelles cartes pour les animations reveal
  if (window._revealObserver) {
    document.querySelectorAll('.prod-card.reveal').forEach(el => {
      window._revealObserver.observe(el);
    });
  }
}

document.addEventListener('DOMContentLoaded', renderProduits);
