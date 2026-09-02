"""Récupère les VRAIES données Google Search Console (90 jours) pour seggfaye.com
et écrit scripts/seo/gsc-data.md (lu par la routine SEO) + gsc-queries.csv.

Propriété = propriété DOMAINE -> 'sc-domain:seggfaye.com' (couvre aussi le guide).
Prérequis : avoir lancé get_gsc_token.py une fois (crée gsc_token.json).
"""
import os
import csv
import datetime
import requests
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

BASE = os.path.dirname(os.path.abspath(__file__))
TOKEN = os.path.join(BASE, "gsc_token.json")
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
SITE = "sc-domain:seggfaye.com"
API = (
    "https://searchconsole.googleapis.com/webmasters/v3/sites/"
    + requests.utils.quote(SITE, safe="")
    + "/searchAnalytics/query"
)

creds = Credentials.from_authorized_user_file(TOKEN, SCOPES)
if not creds.valid:
    creds.refresh(Request())

end = datetime.date.today()
start = end - datetime.timedelta(days=90)


def query(dimension, limit=200):
    body = {
        "startDate": start.isoformat(),
        "endDate": end.isoformat(),
        "dimensions": dimension if isinstance(dimension, list) else [dimension],
        "rowLimit": limit,
    }
    r = requests.post(
        API, headers={"Authorization": f"Bearer {creds.token}"}, json=body, timeout=30
    )
    r.raise_for_status()
    return r.json().get("rows", [])


queries = query("query")
pages = query("page")
page_queries = query(["page", "query"], 5000)

with open(os.path.join(BASE, "gsc-page-queries.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["page", "requete", "clics", "impressions", "ctr_pct", "position"])
    for row in sorted(page_queries, key=lambda r: -r["impressions"]):
        w.writerow([
            row["keys"][0], row["keys"][1], row["clicks"], row["impressions"],
            round(row["ctr"] * 100, 2), round(row["position"], 1),
        ])

with open(os.path.join(BASE, "gsc-queries.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["requete", "clics", "impressions", "ctr_pct", "position"])
    for row in sorted(queries, key=lambda r: -r["impressions"]):
        w.writerow([
            row["keys"][0], row["clicks"], row["impressions"],
            round(row["ctr"] * 100, 2), round(row["position"], 1),
        ])


def md_table(rows, label):
    out = [f"## Top {label} (90 j, tri impressions)", "",
           f"| {label} | clics | impr | CTR% | pos |", "|---|---|---|---|---|"]
    for row in sorted(rows, key=lambda r: -r["impressions"])[:40]:
        out.append(
            f"| {row['keys'][0]} | {row['clicks']} | {row['impressions']} "
            f"| {round(row['ctr']*100,2)} | {round(row['position'],1)} |"
        )
    return "\n".join(out)


with open(os.path.join(BASE, "gsc-data.md"), "w") as f:
    f.write("# Données GSC RÉELLES — seggfaye.com (propriété Domaine)\n\n")
    f.write(f"Généré le {end.isoformat()} — période {start} → {end}. "
            "Source : API Search Console (données réelles). "
            "⚠️ Routine : utiliser CES chiffres, ne PAS deviner le positionnement.\n\n")
    f.write(md_table(queries, "requete") + "\n\n")
    f.write(md_table(pages, "page") + "\n")

print(f"OK — {len(queries)} requêtes, {len(pages)} pages -> gsc-data.md + gsc-queries.csv")
