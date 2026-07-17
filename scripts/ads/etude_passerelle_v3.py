"""Étude v3 (17/07/2026) — filon SÉRIE PASSERELLE : plats français connus ↔ cousins sénégalais.
Mesure les volumes FR des requêtes génériques + des noms sénégalais candidats.
⚠ Les noms sénégalais listés ici servent à MESURER — leur usage en contenu reste à valider par Lamine.
Sort mots_cles_passerelle_v3.csv"""
import csv
from google.ads.googleads.client import GoogleAdsClient

YAML = "/Users/laminefaye/Projets/mes sites web/scripts/ads/google-ads.yaml"
OUT = "/Users/laminefaye/Projets/mes sites web/scripts/ads/mots_cles_passerelle_v3.csv"
CUSTOMER_ID = "8288734405"
FR = "geoTargetConstants/2250"
FRENCH = "languageConstants/1010"

SEEDS = {
    "passerelle-fr": [
        "pain perdu", "riz au lait", "bouillie de mil", "porridge de mil",
        "beignet africain", "beignets sénégalais", "yaourt aux céréales",
        "dessert sénégalais", "goûter africain", "crème de mil",
    ],
    "cousins-senegalais": [
        "sombi", "sombi riz au lait", "lakh", "lakh sénégalais", "ngalakh",
        "thiakry", "ciakri", "dégué", "fondé sénégalais", "mbourou fass",
        "caakiri", "beignet banane",
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
