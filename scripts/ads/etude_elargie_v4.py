"""Étude v4 (30/09/2026) — seeds ÉLARGIES : fêtes, cadeaux diaspora, conservation, poisson.
Demandée par l'analyse hebdo cloud (4 semaines sans nouveau mot-clé).
Sort mots_cles_elargie_v4.csv"""
import csv
from google.ads.googleads.client import GoogleAdsClient

YAML = "/Users/laminefaye/Projets/mes sites web/scripts/ads/google-ads.yaml"
OUT = "/Users/laminefaye/Projets/mes sites web/scripts/ads/mots_cles_elargie_v4.csv"
CUSTOMER_ID = "8288734405"
FR = "geoTargetConstants/2250"
FRENCH = "languageConstants/1010"

SEEDS = {
    "fetes": [
        "repas tabaski", "recette tabaski", "recette korité", "plat de fête africain",
        "repas de noël africain", "recette ramadan africaine", "menu mariage sénégalais",
        "buffet africain",
    ],
    "cadeaux-diaspora": [
        "cadeau gourmand africain", "coffret produits africains", "colis alimentaire afrique",
        "épicerie fine africaine", "produits du sénégal en france", "box cuisine africaine",
    ],
    "conservation": [
        "conserver poisson séché", "poisson séché odeur", "dessaler poisson séché",
        "poisson séché bienfaits", "comment cuisiner poisson séché", "poisson fumé africain",
        "poisson salé séché", "crevettes séchées recette",
    ],
    "poisson-frais": [
        "thiof", "poisson capitaine", "tilapia", "sardinelle", "poisson braisé",
        "poisson africain", "carton de poisson",
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
    for idea in svc.generate_keyword_ideas(request=req):
        m = idea.keyword_idea_metrics
        rows.append({
            "cluster": cluster, "mot_cle": idea.text,
            "volume_mensuel": m.avg_monthly_searches,
            "concurrence": COMP(m.competition).name,
        })

rows.sort(key=lambda r: -(r["volume_mensuel"] or 0))
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["cluster", "mot_cle", "volume_mensuel", "concurrence"])
    w.writeheader()
    w.writerows(rows)
print(f"{len(rows)} mots-clés → {OUT}")

# Affiche les cibles exactes + le top général
cibles = {s.lower() for seeds in SEEDS.values() for s in seeds}
print("\n=== SEEDS EXACTES ===")
for r in rows:
    if r["mot_cle"].lower() in cibles:
        print(f"{r['volume_mensuel']:>8}  {r['concurrence']:<8}  {r['mot_cle']}")
print("\n=== TOP 20 IDÉES ===")
for r in rows[:20]:
    print(f"{r['volume_mensuel']:>8}  {r['concurrence']:<8}  {r['mot_cle']}  [{r['cluster']}]")
