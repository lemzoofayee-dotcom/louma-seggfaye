#!/usr/bin/env node
// generate-fish.mjs
// Génère le carrousel TikTok "Noms Wolof - Les Poissons" Part 1
// Usage : node scripts/generate-fish.mjs (depuis la racine du projet)

import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PROJECT_ROOT = path.resolve(__dirname, '..');

// 1. Charger FAL_KEY depuis .env
const envContent = await fs.readFile(path.join(PROJECT_ROOT, '.env'), 'utf8');
const FAL_KEY = envContent.match(/FAL_KEY=(.+)/)?.[1]?.trim();

if (!FAL_KEY || FAL_KEY === 'REMPLIR_ICI') {
  console.error('❌ FAL_KEY manquante ou non remplie dans .env');
  process.exit(1);
}

// 2. Charger la liste des poissons
const listPath = path.join(__dirname, 'poissons-list.json');
const items = JSON.parse(await fs.readFile(listPath, 'utf8'));

// 3. Préparer le dossier de sortie
const OUTPUT_DIR = path.join(PROJECT_ROOT, 'assets/poissons-wolof/part1');
await fs.mkdir(OUTPUT_DIR, { recursive: true });

// 4. Construire les prompts selon le type de slide
const buildPrompt = (item) => {
  const styleBase = 'Vertical 9:16 TikTok educational poster, light grey marble background, scattered fresh seafood decoration on top edge (octopus tentacle, lemon halves, red chili peppers, fresh parsley sprigs), clean editorial style, professional studio lighting, high resolution photography';

  if (item.type === 'cover') {
    return `${styleBase}. Center: large elegant blue ribbon banner with white script text "${item.title}". Below the banner: small rectangular cards arranged in a 3x4 grid, each card showing a different colorful fresh fish (silver, red, grey, brown). Subtitle text "${item.subtitle}" in bold letters. Bright clean composition, eye-catching cover slide.`;
  }

  if (item.type === 'cta') {
    return `${styleBase}. Center: large bold uppercase white text "${item.title}" displayed prominently on a dark navy blue ribbon banner. Below: bold black text "${item.subtitle}". Decorative pointing finger or arrow emoji. Engaging call-to-action design, vibrant and bold.`;
  }

  // Type fish
  return `${styleBase}. Center: clean white card with rounded corners centered in frame, containing a top-down photograph of a single ${item.fishDescription}. Below the fish on the same card: large bold uppercase blue display text "${item.wolof}" in centered position, then smaller uppercase black text "${item.francais}" below. Educational poster style, single fish clearly visible, clean white card surface, high quality food photography.`;
};

// 5. Appel fal.ai pour une image
const FLUX_DEV_COST = 0.025; // USD par image

async function generateImage(prompt) {
  const response = await fetch('https://fal.run/fal-ai/flux/dev', {
    method: 'POST',
    headers: {
      'Authorization': `Key ${FAL_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      prompt,
      image_size: { width: 1080, height: 1920 },
      num_inference_steps: 28,
      guidance_scale: 3.5,
      enable_safety_checker: false,
    }),
  });

  if (!response.ok) {
    const errText = await response.text();
    throw new Error(`fal.ai ${response.status}: ${errText.slice(0, 200)}`);
  }

  const data = await response.json();
  const imageUrl = data.images?.[0]?.url;
  if (!imageUrl) throw new Error('Pas d\'URL image dans la réponse fal.ai');

  // Télécharger l'image
  const imgResponse = await fetch(imageUrl);
  if (!imgResponse.ok) throw new Error(`Download failed: ${imgResponse.status}`);
  const buffer = Buffer.from(await imgResponse.arrayBuffer());
  return buffer;
}

// 6. Boucle principale
console.log(`\n🐟 Carrousel "Noms Wolof - Les Poissons" Part 1`);
console.log(`📦 ${items.length} slides à générer`);
console.log(`💰 Coût estimé : $${(items.length * FLUX_DEV_COST).toFixed(2)}`);
console.log(`📁 Sortie : ${OUTPUT_DIR}\n`);

let totalCost = 0;
let success = 0;
let failed = 0;

for (let i = 0; i < items.length; i++) {
  const item = items[i];
  const num = `[${String(i + 1).padStart(2, '0')}/${items.length}]`;
  const filename = `${item.slug}.png`;
  const outputPath = path.join(OUTPUT_DIR, filename);

  process.stdout.write(`${num} ${item.slug.padEnd(20)} `);

  try {
    const buffer = await generateImage(buildPrompt(item));
    await fs.writeFile(outputPath, buffer);
    totalCost += FLUX_DEV_COST;
    success++;
    console.log(`✅ téléchargé (${(buffer.length / 1024).toFixed(0)} KB)`);
  } catch (err) {
    failed++;
    console.log(`❌ ${err.message}`);
  }
}

// 7. Résumé final
console.log(`\n${'═'.repeat(50)}`);
console.log(`✅ Réussi : ${success}/${items.length}`);
if (failed) console.log(`❌ Échoué : ${failed}/${items.length}`);
console.log(`💰 Coût total : $${totalCost.toFixed(2)}`);
console.log(`📁 Images dans : ${OUTPUT_DIR}`);
console.log(`${'═'.repeat(50)}\n`);

if (failed > 0) {
  console.log(`💡 Pour relancer uniquement les échecs, supprime les fichiers réussis du dossier et relance le script.\n`);
}
