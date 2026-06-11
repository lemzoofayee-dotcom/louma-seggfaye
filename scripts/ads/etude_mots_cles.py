"""Étude de mots-clés Louma via l'API Google Ads (KeywordPlanIdeaService).

À lancer quand l'accès Basic est accordé (sinon DEVELOPER_TOKEN_NOT_APPROVED —
vérifier avec check_access.py). Sort un CSV trié par volume :
scripts/ads/mots_cles_resultats.csv

NB : si l'API refuse le MCC (compte manager), il faudra un compte client
Google Ads classique sous le MCC — à créer sans campagne ni carte.
"""
import csv
import sys

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

YAML = "/Users/laminefaye/Projets/mes sites web/scripts/ads/google-ads.yaml"
OUT = "/Users/laminefaye/Projets/mes sites web/scripts/ads/mots_cles_resultats.csv"
CUSTOMER_ID = "8288734405"  # MCC Louma Manager
FR = "geoTargetConstants/2250"
FRENCH = "languageConstants/1010"

# ~50 graines par cluster (ratisser large : variantes FR + wolof)
SEEDS = {
    "guedj-poisson": [
        "guedj", "guedj sénégalais", "poisson séché", "poisson séché sénégalais",
        "poisson fumé africain", "acheter guedj", "poisson séché africain",
        "kethiakh", "sardinelle fumée", "produit halieutique séché",
    ],
    "fruits-de-mer": [
        "yeet", "cymbium", "huîtres séchées", "crevettes séchées",
        "crevettes séchées cuisine", "escargot de mer séché",
    ],
    "condiments": [
        "netetou", "soumbala", "nététou", "pâte d'arachide", "tiguadegue",
        "purée de piment africain",
    ],
    "boissons-cereales": [
        "bissap", "jus de bissap", "fleur d'hibiscus séchée", "kinkeliba",
        "fonio", "thiakry", "couscous de mil", "thiéré", "niébé", "mil sénégalais",
    ],
    "epicerie-en-ligne": [
        "épicerie africaine", "épicerie africaine en ligne", "épicerie sénégalaise",
        "produits africains en ligne", "boutique africaine en ligne",
        "produits sénégalais france", "produits exotiques sénégal",
        "épicerie exotique en ligne", "beurre de karité alimentaire",
    ],
    "recettes": [
        "recette thieboudienne", "recette mafé", "recette yassa poulet",
        "soupoukandja", "bassi salté", "recette sénégalaise",
        "cuisine sénégalaise", "plat sénégalais", "mbakhal saloum",
    ],
}

client = GoogleAdsClient.load_from_storage(YAML)
svc = client.get_service("KeywordPlanIdeaService")
COMP = client.enums.KeywordPlanCompetitionLevelEnum

rows = []
for cluster, seeds in SEEDS.items():
    req = client.get_type("GenerateKeywordIdeasRequest")
    req.customer_id = CUSTOMER_ID
    req.language = FRENCH
    req.geo_target_constants.append(FR)
    req.keyword_plan_network = client.enums.KeywordPlanNetworkEnum.GOOGLE_SEARCH
    req.keyword_seed.keywords.extend(seeds)
    try:
        for idea in svc.generate_keyword_ideas(request=req):
            m = idea.keyword_idea_metrics
            rows.append({
                "cluster": cluster,
                "mot_cle": idea.text,
                "volume_mensuel": m.avg_monthly_searches,
                "concurrence": COMP(m.competition).name,
                "cpc_bas_eur": round(m.low_top_of_page_bid_micros / 1e6, 2),
                "cpc_haut_eur": round(m.high_top_of_page_bid_micros / 1e6, 2),
            })
        print(f"{cluster}: OK")
    except GoogleAdsException as e:
        for err in e.failure.errors:
            print(f"{cluster}: ERREUR {err.error_code} — {err.message}")
        sys.exit(1)

# dédoublonner (un même mot-clé peut sortir de plusieurs clusters)
seen, uniques = set(), []
for r in sorted(rows, key=lambda r: -r["volume_mensuel"]):
    if r["mot_cle"] not in seen:
        seen.add(r["mot_cle"])
        uniques.append(r)

with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(uniques[0].keys()))
    w.writeheader()
    w.writerows(uniques)

print(f"\n{len(uniques)} mots-clés uniques → {OUT}")
print("\nTop 20 par volume :")
for r in uniques[:20]:
    print(f"  {r['volume_mensuel']:>7}/mois | {r['mot_cle']} ({r['concurrence']})")
