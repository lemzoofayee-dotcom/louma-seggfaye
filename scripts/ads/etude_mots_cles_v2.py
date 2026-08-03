"""Étude v2 (12/07/2026) — seeds élargies post-découvertes. Sort mots_cles_resultats_v2.csv"""
import csv, sys
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

YAML = "/Users/laminefaye/Projets/mes sites web/scripts/ads/google-ads.yaml"
OUT = "/Users/laminefaye/Projets/mes sites web/scripts/ads/mots_cles_resultats_v2.csv"
CUSTOMER_ID = "8288734405"
FR = "geoTargetConstants/2250"
FRENCH = "languageConstants/1010"

SEEDS = {
    "cymbium-yeet": [
        "cymbium", "yeet", "yett", "yet sénégalais", "cymbium séché",
        "escargot de mer sénégal", "volute de mer", "yeet cuisine",
    ],
    "guedj-poisson": [
        "guedj", "guedj beurre", "guedj kong", "kong fumé", "poisson kong",
        "courbine séchée", "kethiakh", "ketiakh", "guedj yass", "tambadiang",
        "poisson séché sénégalais", "poisson fumé sénégal",
    ],
    "condiments": [
        "soumbala", "netetou", "nététou", "néré", "graine de néré",
        "sauce netetou", "yokhos", "yoxos", "huitres séchées sénégal",
    ],
    "boissons-fruits": [
        "bouye", "jus de bouye", "pain de singe", "poudre de baobab",
        "ditakh", "ditax", "tamarin jus", "bissap blanc", "bissap rouge",
        "oseille de guinée",
    ],
    "recettes-plats": [
        "caldou", "thiebou wekh", "borokhé", "domoda", "thiébou yapp",
        "mbakhalou saloum", "recette caldou", "soupou kandja", "lakh sénégalais",
    ],
    "achat-diaspora": [
        "où acheter guedj", "acheter netetou", "acheter bissap",
        "acheter poisson séché", "épicerie sénégalaise en ligne",
        "produits africains livraison", "épicerie africaine paris",
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
                "cluster": cluster, "mot_cle": idea.text,
                "volume_mensuel": m.avg_monthly_searches,
                "concurrence": COMP(m.competition).name,
                "cpc_bas_eur": round(m.low_top_of_page_bid_micros / 1e6, 2),
                "cpc_haut_eur": round(m.high_top_of_page_bid_micros / 1e6, 2),
            })
        print(f"{cluster}: OK ({len(rows)} cumulés)")
    except GoogleAdsException as e:
        for err in e.failure.errors:
            print(f"{cluster}: ERREUR {err.error_code} — {err.message}")
        sys.exit(1)

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
for r in uniques[:25]:
    print(f"  {r['volume_mensuel']:>7}/mois | {r['mot_cle']} ({r['concurrence']}) cpc {r['cpc_bas_eur']}-{r['cpc_haut_eur']}€")
