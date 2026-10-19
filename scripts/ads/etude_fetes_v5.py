"""Étude v5 (19/10/2026) — seeds FIN D'ANNÉE : Noël/réveillon africain, cadeaux et colis diaspora,
achat en ligne. Demandée au point du 19/10 (routine Ads à vide depuis le 30/09).
Sort mots_cles_fetes_v5.csv"""
import csv
from google.ads.googleads.client import GoogleAdsClient

YAML = "/Users/laminefaye/Projets/mes sites web/scripts/ads/google-ads.yaml"
OUT = "/Users/laminefaye/Projets/mes sites web/scripts/ads/mots_cles_fetes_v5.csv"
CUSTOMER_ID = "8288734405"
FR = "geoTargetConstants/2250"
FRENCH = "languageConstants/1010"

SEEDS = {
    "noel-reveillon": [
        "repas de noël africain", "menu réveillon africain", "recette noël sénégalaise",
        "plat africain pour le nouvel an", "thieboudienne noël", "recette réveillon poisson",
        "entrée africaine de fête", "pastels sénégalais",
    ],
    "cadeaux-colis": [
        "cadeau gourmand africain", "panier garni africain", "colis alimentaire sénégal",
        "cadeau noël africain", "coffret épices africaines", "idée cadeau sénégal",
    ],
    "achat-en-ligne": [
        "épicerie africaine en ligne", "produits sénégalais en ligne", "acheter poisson séché",
        "acheter crevettes séchées", "épicerie sénégalaise", "livraison produits africains",
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
