"""Teste si l'accès Basic à l'API Google Ads est accordé.

Tente un GenerateKeywordIdeas minimal. Tant que le niveau du token est
"compte test", l'API renvoie DEVELOPER_TOKEN_NOT_APPROVED.
"""
import sys

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

YAML = "/Users/laminefaye/Projets/mes sites web/scripts/ads/google-ads.yaml"
CUSTOMER_IDS = ["7694854348", "8288734405"]  # compte classique d'abord, MCC en secours
FR = "geoTargetConstants/2250"  # France
FRENCH = "languageConstants/1010"

client = GoogleAdsClient.load_from_storage(YAML)
svc = client.get_service("KeywordPlanIdeaService")

for cid in CUSTOMER_IDS:
    req = client.get_type("GenerateKeywordIdeasRequest")
    req.customer_id = cid
    req.language = FRENCH
    req.geo_target_constants.append(FR)
    req.keyword_plan_network = client.enums.KeywordPlanNetworkEnum.GOOGLE_SEARCH
    req.keyword_seed.keywords.append("poisson séché")
    try:
        resp = svc.generate_keyword_ideas(request=req)
        ideas = list(resp)
        print(f"ACCES_OK customer={cid} idees={len(ideas)}")
        for idea in ideas[:5]:
            m = idea.keyword_idea_metrics
            print(f"  {idea.text} | vol/mois={m.avg_monthly_searches}")
        sys.exit(0)
    except GoogleAdsException as e:
        codes = [err.error_code for err in e.failure.errors]
        msgs = [err.message for err in e.failure.errors]
        print(f"customer={cid} ERREUR: {codes} {msgs}")

print("ACCES_PAS_ENCORE_ACCORDE (ou autre blocage, voir erreurs ci-dessus)")
sys.exit(1)
