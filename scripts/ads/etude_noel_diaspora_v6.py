"""Étude v6 (09/11/2026) — reprise des seeds fin d'année de la v5, avec le volume MOIS PAR MOIS
(12 derniers mois) pour lire la vraie demande de décembre, et 2 géos en plus pour la diaspora :
francophone (Belgique, Suisse, Canada) et anglophone (États-Unis, Royaume-Uni, Canada).
Sort mots_cles_noel_diaspora_v6.csv"""
import csv
import time
from google.ads.googleads.client import GoogleAdsClient

YAML = "/Users/laminefaye/Projets/mes sites web/scripts/ads/google-ads.yaml"
OUT = "/Users/laminefaye/Projets/mes sites web/scripts/ads/mots_cles_noel_diaspora_v6.csv"
CUSTOMER_ID = "8288734405"
FRENCH, ENGLISH = "languageConstants/1010", "languageConstants/1000"
GEO = {"FR": ["2250"], "BE-CH-CA": ["2056", "2756", "2124"], "US-UK-CA": ["2840", "2826", "2124"]}

SEEDS_FR = {
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
SEEDS_EN = {
    "christmas": ["african christmas food", "senegalese christmas dinner", "west african christmas recipes",
                  "nigerian christmas food", "jollof rice christmas"],
    "gifts": ["african food gift box", "african spice gift set", "african snacks gift"],
    "buy-online": ["buy dried fish online", "african grocery online", "senegalese food online",
                   "buy stockfish online", "dried shrimp african"],
}
RUNS = [("FR", FRENCH, SEEDS_FR), ("BE-CH-CA", FRENCH, SEEDS_FR), ("US-UK-CA", ENGLISH, SEEDS_EN)]

client = GoogleAdsClient.load_from_storage(YAML)
svc = client.get_service("KeywordPlanIdeaService")
COMP = client.enums.KeywordPlanCompetitionLevelEnum
MOIS = client.enums.MonthOfYearEnum

rows = []
for geo, lang, seeds_map in RUNS:
    for cluster, seeds in seeds_map.items():
        req = client.get_type("GenerateKeywordIdeasRequest")
        req.customer_id = CUSTOMER_ID
        req.language = lang
        req.geo_target_constants.extend(f"geoTargetConstants/{g}" for g in GEO[geo])
        req.keyword_plan_network = client.enums.KeywordPlanNetworkEnum.GOOGLE_SEARCH
        req.keyword_seed.keywords.extend(seeds)
        for essai in range(5):  # quota Google : 1 requête toutes les quelques secondes
            try:
                ideas = list(svc.generate_keyword_ideas(request=req)); break
            except Exception as e:
                if "429" not in str(e) and "RESOURCE_EXHAUSTED" not in str(e): raise
                time.sleep(10)
        time.sleep(6)
        for idea in ideas:
            m = idea.keyword_idea_metrics
            mois = {f"{v.year}-{MOIS(v.month).value - 1:02d}": v.monthly_searches for v in m.monthly_search_volumes}
            rows.append({
                "geo": geo, "cluster": cluster, "mot_cle": idea.text,
                "volume_mensuel": m.avg_monthly_searches,
                "decembre_2025": mois.get("2025-12", ""),
                "pic_mois": max(mois, key=mois.get) if mois else "",
                "concurrence": COMP(m.competition).name,
                "seed": idea.text.lower() in {s.lower() for s in seeds},
            })

rows.sort(key=lambda r: (r["geo"], -(r["volume_mensuel"] or 0)))
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
print(f"{len(rows)} lignes → {OUT}")
