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
    nomLocal: "Cipakh",
    categorie: "mer",
    prix: 6.00,
    unite: "par 100g",
    prixAncien: null,
    badge: "Bestseller",
    image: "crevettes-saloum-1.jpg",
    gallery: ["crevettes-saloum-1.jpg", "crevettes-saloum-2.jpg", "crevettes-saloum-3.jpg"],
    description: "Pêche artisanale nocturne en duo dans les Îles du Saloum, cuisson à la vapeur, décortiquage à la main, puis séchage au soleil pendant 2 jours. Une méthode 100% traditionnelle, sans additif.",
    origine: "Îles du Saloum, Foundiougne — Région de Fatick",
    goutPlus: "Aucune sensation de sable sous la dent : la zone argileuse du Saloum garantit une qualité bien supérieure aux crevettes sablonneuses qu'on trouve ailleurs.",
    conseil: "Réhydrater à l'eau tiède (jamais chaude) pour préserver le goût. Condiment polyvalent : se marie avec presque tous les plats sénégalais.",
    stock: true,
    nouveaute: false
  },
  {
    id: "yoxos",
    nom: "Yoxos",
    nomLocal: "Huîtres séchées",
    categorie: "mer",
    prix: 6.00,
    unite: "par 100g",
    prixAncien: null,
    badge: null,
    image: "yoxos-saloum-1.jpg",
    gallery: ["yoxos-saloum-1.jpg", "yoxos-saloum-2.jpg", "yoxos-saloum-3.jpg"],
    description: "Cueillette à la main par les femmes du Saloum, sur les racines des palétuviers en pleine mangrove. Bouillies, décoquillées à la main, séchées au soleil. Méthode traditionnelle préservée de génération en génération.",
    origine: "Mangrove des Îles du Saloum, Foundiougne — système matriarcal",
    goutPlus: "Chair séchée allongée/ovale (à ne pas confondre avec le pagne/coques dont la chair est arrondie). Récolte respectueuse, repos biologique de 6 mois par an.",
    conseil: "Condiment aromatique pour rehausser tous les plats traditionnels. Réhydrater à l'eau tiède avant cuisson.",
    stock: true,
    nouveaute: false
  },
  {
    id: "pagne",
    nom: "Pagne (coques)",
    nomLocal: "Pagne",
    categorie: "mer",
    prix: 6.00,
    unite: "par 100g",
    prixAncien: null,
    badge: null,
    image: "pagne-conv.jpg",
    description: "Coques cueillies à la main par les femmes dans la vase de la mangrove — ramassées ou récupérées en plongeant. Bouillies, décoquillées à la main, essorées au filet puis séchées au soleil 2 à 3 jours. Zéro machine, 100% artisanal.",
    origine: "Mangrove des Îles du Saloum — système matriarcal",
    goutPlus: "Goût agréable de fruits de mer. Chair séchée arrondie (à ne pas confondre avec les yokhos/huîtres dont la chair est allongée). Cueillette limitée : repos biologique de 6 mois par an.",
    conseil: "Frais : parfait en sauce spaghetti comme en Italie. Séché : dans tous les thieb et le riz blanc. Réhydrater à l'eau tiède avant cuisson.",
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
    nomLocal: "Guedj Yass",
    categorie: "mer",
    prix: 6.00,
    unite: "par 100g",
    prixAncien: 7.00,
    badge: null,
    image: "guedj-yass-1.jpg",
    gallery: ["guedj-yass-1.jpg", "guedj-yass-3.jpg", "guedj-yass-5.jpg", "guedj-yass-2.jpg", "guedj-yass-4.jpg"],
    description: "Guedj de yass (sardinelle plate), séché au soleil selon la méthode traditionnelle sénégalaise. Poisson plat à chair fine, goût prononcé et texture ferme. Un classique de la cuisine sénégalaise.",
    origine: "Sénégal — Pêche artisanale côtière",
    goutPlus: "Le yass séché a un goût intense et salé qui relève puissamment les sauces. Sa forme plate permet un séchage uniforme et une conservation optimale.",
    conseil: "Idéal dans le thiéboudienne, le riz au poisson et les sauces à base de tomate. Casser en morceaux avant d'ajouter à la cuisson.",
    stock: true,
    nouveaute: false
  },
  {
    id: "guej-beurre",
    nom: "Guej Beurre",
    nomLocal: "Guedj Berr",
    categorie: "mer",
    prix: 4.00,
    unite: "par 100g",
    prixAncien: 6.00,
    badge: null,
    image: "guedji-beurre.jpg",
    description: "Le guedj le plus connu de la diaspora. Fait à partir de courbine (Berr), un poisson à chair blanche et grasse. Séchage traditionnel au soleil. Goût doux et polyvalent — il passe partout.",
    origine: "Sénégal — Pêche artisanale côtière",
    goutPlus: "Sa texture grasse et sa saveur douce en font le guedj le plus accessible. Idéal pour débuter si vous ne connaissez pas encore le guedj.",
    conseil: "Se marie avec presque tous les plats sénégalais. Incontournable dans le thiéboudienne.",
    stock: true,
    nouveaute: false
  },
  {
    id: "guej-beur-casamance",
    nom: "Guej Beur Casamance",
    nomLocal: "Guedj Berr bi Casamance",
    categorie: "mer",
    prix: 12.00,
    unite: "par 300g",
    prixAncien: 18.00,
    badge: "Casamance",
    image: "guedji-beur_casamance.jpg",
    description: "Même poisson que le Guedj Beurre (courbine/Berr), mais avec un séchage suivi d'un fumage au bois selon la technique casamançaise. Le résultat est un goût beaucoup plus complexe et profond.",
    origine: "Casamance — Région sud du Sénégal",
    goutPlus: "Le fumage au bois casamançais apporte une dimension fumée unique. C'est la version premium du Guedj Beurre — 3× le prix, mais un goût incomparable.",
    conseil: "Idéal pour les sauces qui demandent de la profondeur. À utiliser avec parcimonie, le goût est plus intense que le Beurre classique.",
    stock: true,
    nouveaute: false
  },
  {
    id: "guej-sol",
    nom: "Guej Sole",
    nomLocal: "Guedj Sole",
    categorie: "mer",
    prix: 4.00,
    unite: "par 100g",
    prixAncien: 6.00,
    badge: null,
    image: "guedj-sole-1.jpg",
    gallery: ["guedj-sole-1.jpg", "guedj-sole-2.jpg", "guedj-sole-3.jpg", "guedj-sole-4.jpg"],
    description: "Guedj de sole, un poisson plat à chair délicate. Séchage traditionnel au soleil. Sa finesse en fait un guedj apprécié pour les sauces légères et parfumées.",
    origine: "Sénégal — Pêche artisanale côtière",
    goutPlus: "Plus doux que le kong ou le beurre, le guedj de sole apporte une saveur subtile sans dominer le plat. Parfait pour ceux qui préfèrent un goût moins intense.",
    conseil: "Se marie bien avec les sauces claires et le riz blanc. Réhydrater avant cuisson pour une texture plus tendre.",
    stock: true,
    nouveaute: false
  },
  {
    id: "guej-kong",
    nom: "Guej Kong",
    nomLocal: "Guedj Kong",
    categorie: "mer",
    prix: 3.00,
    unite: "par 100g",
    prixAncien: 5.00,
    badge: null,
    image: "guedj-kong-1.jpg",
    gallery: ["guedj-kong-1.jpg", "guedj-kong-3.jpg", "guedj-kong-2.jpg", "guedj-kong-4.jpg"],
    description: "Guedj de mâchoiron (Kong). Avec le Beurre, c'est l'un des 2 guedj les plus connus de la diaspora. Goût prononcé, idéal pour les plats traditionnels.",
    origine: "Sénégal — Pêche artisanale côtière",
    goutPlus: "Le kong a un goût puissant et caractéristique qui donne du corps aux sauces. C'est le guedj que la diaspora reconnaît les yeux fermés.",
    conseil: "Incontournable dans le thiéboudienne et les plats en sauce. Un petit morceau suffit pour parfumer tout le plat.",
    stock: true,
    nouveaute: false
  },
  {
    id: "guej-tambajang",
    nom: "Guej Tambajang",
    nomLocal: "Guedj Tambajang",
    categorie: "mer",
    prix: 3.00,
    unite: "par 100g",
    prixAncien: 5.00,
    badge: null,
    image: "guedj-tambajang-1.jpg",
    gallery: ["guedj-tambajang-1.jpg", "guedj-tambajang-3.jpg", "guedj-tambajang-2.jpg"],
    description: "Guedj de tambajang, petit poisson séché entier. Très utilisé comme condiment dans la cuisine sénégalaise pour son goût concentré et sa praticité.",
    origine: "Sénégal — Pêche artisanale côtière",
    goutPlus: "Sa petite taille permet un séchage complet qui concentre intensément les saveurs. Le tambajang est le guedj du quotidien, celui qu'on ajoute dans presque tout.",
    conseil: "Ajouter entier ou émietter dans les sauces en début de cuisson. Excellent dans les soupes, le domoda et les plats de riz.",
    stock: true,
    nouveaute: false
  },
  {
    id: "guej-toumboulan",
    nom: "Guej Toumboulan",
    nomLocal: "Toumboulane",
    categorie: "mer",
    prix: 3.00,
    unite: "par 100g",
    prixAncien: 5.00,
    badge: "Rare",
    image: "guedji-toumboulane.jpg",
    description: "Cartilages séchés d'ailerons de raies ou de requin (Gaindé Guéth = Lion de la mer). Très très rare — difficile à obtenir. Accélérateur de goût pour les condiments.",
    origine: "Sénégal — Pêche artisanale",
    goutPlus: "Son secret : il épaissit la sauce grâce à un effet gélatine naturel. Une sauce épaisse = signe d'un bon thiéboudienne. C'est le guedj des connaisseurs.",
    conseil: "À ajouter dans les sauces pour épaissir et intensifier le goût. Un tout petit morceau suffit.",
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
    nomLocal: "Pack bi Saloum",
    categorie: "mer",
    prix: 60.00,
    unite: "par kg",
    prixAncien: null,
    badge: "Pack 4 produits",
    image: "packsaloum-sachetdebout1.jpg",
    description: "4 trésors des Îles du Saloum réunis : Tuffa + Yokhos + Cipakh (crevettes) + Pagne (coques). Ces 4 produits ne sont jamais disponibles en même temps — cette rareté justifie le pack.",
    origine: "Îles du Saloum — Patrimoine UNESCO",
    goutPlus: "Chaque produit vient de la même zone (mangrove du Saloum) mais avec des goûts totalement différents. Ensemble, ils couvrent tous les plats traditionnels.",
    conseil: "Le cadeau parfait pour quelqu'un qui connaît la cuisine sénégalaise. Ou pour découvrir 4 saveurs du Saloum d'un coup.",
    stock: true,
    nouveaute: false
  },

  // ──────────────────────────────────────
  //  🌿 ÉPICES & CONDIMENTS
  // ──────────────────────────────────────
  {
    id: "netetu-dom",
    nom: "Netetu Dom",
    nomLocal: "Netetou",
    categorie: "epices",
    prix: 5.00,
    unite: "par 100g",
    prixAncien: 6.00,
    badge: null,
    image: "netetou-dome.jpg",
    description: "Graines de néré bouillies, fermentées puis séchées. Condiment emblématique de la cuisine ouest-africaine. Origine principale : Mali et Casamance (Sédhiou/Kolda). Circuit court, emballé sous vide pour neutraliser l'odeur.",
    origine: "Mali & Casamance (Sédhiou, Kolda) — Circuit court",
    goutPlus: "Le netetou est un exhausteur de goût naturel. Sous vide = pas d'odeur au transport, mais tout le goût une fois en cuisine.",
    conseil: "Émietter dans les sauces en début de cuisson. Indispensable dans le mafé et de nombreux plats sénégalais.",
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
    nomLocal: "Bissap",
    categorie: "epices",
    prix: 5.00,
    unite: "par 150g",
    prixAncien: 6.00,
    badge: "Bissap",
    image: "Bissap-rouge.jpg",
    description: "Fleurs d'hibiscus séchées, couleur rouge intense. La base du jus de bissap, boisson emblématique du Sénégal — un goût acidulé que la diaspora compare au Vimto.",
    origine: "Kaolack / Keur Madiabel — Sénégal",
    goutPlus: "Son acidité naturelle rafraîchit sans sucre ajouté. Effet gélifiant naturel (mucilage) unique au bissap de qualité.",
    conseil: "Infuser à froid ou à chaud. Ajouter sucre, menthe, fleur d'oranger selon le goût. Se conserve 3-4 jours au frigo.",
    stock: true,
    nouveaute: false
  },
  {
    id: "bissap-blanc",
    nom: "Bissap Blanc",
    nomLocal: "Bissap bu weex",
    categorie: "epices",
    prix: 5.00,
    unite: "par 200g",
    prixAncien: 6.00,
    badge: "Bissap",
    image: "Bissap-blanc.jpg",
    description: "Variété blanche du bissap, plus douce que la rouge. Utilisée autant en jus qu'en cuisine. Son acidité n'influence pas la couleur des plats.",
    origine: "Kaolack / Keur Madiabel — Sénégal",
    goutPlus: "Plus polyvalent que le rouge : même acidité mais sans colorer. Effet gélifiant naturel (mucilage) pour épaissir les sauces.",
    conseil: "En jus : infusion douce, goût plus subtil. En cuisine : dans les sauces où la couleur rouge n'est pas souhaitée.",
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
  {
    id: "maad-fruit",
    nom: "Maad Fruit",
    categorie: "epices",
    prix: 10.00,
    unite: "par kg",
    prixAncien: null,
    badge: "Fruit",
    image: "maad-fruit.jpg",
    stock: true,
    nouveaute: true,
    maxKg: 3
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
    image: "thiere1.jpg",
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
    nom: "Thiakry",
    categorie: "cereales",
    prix: 18.00,
    unite: "par kg",
    prixAncien: null,
    badge: "Couscous",
    image: "thiakry1.jpg",
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

  const nomEsc = p.nom.replace(/'/g, "\\'");
  const imgEsc = (p.image || '').replace(/'/g, "\\'");
  const btnHtml = p.stock
    ? `<button class="btn-sm" onclick="cartSystem.add({name:'${nomEsc}',price:${p.prix},unit:'${p.unite}',img:'${imgEsc}',cat:'${p.categorie}'})">🛒 Ajouter</button>`
    : `<span class="btn-sm" style="opacity:.35;cursor:not-allowed;pointer-events:none;">Indisponible</span>`;

  return `
<div class="prod-card reveal${!p.stock ? ' out-of-stock' : ''}" data-cat="${p.categorie}" data-id="${p.id}">
  <div class="prod-img-shell" onclick="openProdModal('${p.id}')">
    <div class="prod-img-core">${imgContent}</div>
    <div class="prod-img-overlay">${p.nom}</div>
    ${badgeHtml}
  </div>
  <div class="prod-body">
    <div class="prod-name" onclick="openProdModal('${p.id}')" style="cursor:pointer;">${p.nom}</div>
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

// Expose globalement pour la fiche produit modal
window.PRODUITS = PRODUITS;

document.addEventListener('DOMContentLoaded', renderProduits);
