"""Récupère les VRAIES données Bing Webmaster Tools pour seggfaye.com
et écrit scripts/seo/bing-data.md + bing-queries.csv (locaux, gitignorés).

Prérequis : clé API Bing dans ~/.bing_webmaster_key, hors du dépôt
(créée par ~/Desktop/Coller-cle-Bing.command).
"""
import os
import csv
import re
import datetime
import requests

BASE = os.path.dirname(os.path.abspath(__file__))
KEY_FILE = os.path.expanduser("~/.bing_webmaster_key")
API = "https://ssl.bing.com/webmaster/api.svc/json/"

with open(KEY_FILE) as f:
    KEY = f.read().strip()


def call(method, **params):
    r = requests.get(API + method, params={"apikey": KEY, **params}, timeout=30)
    r.raise_for_status()
    return r.json().get("d", [])


def day(value):
    # Bing renvoie les dates au format "/Date(1729382400000)/"
    ms = int(re.search(r"-?\d+", value).group())
    return datetime.date.fromtimestamp(ms / 1000)


sites = [s["Url"] for s in call("GetUserSites")]
site = next((s for s in sites if "seggfaye.com" in s and "guide" not in s), sites[0])

traffic = sorted(call("GetRankAndTrafficStats", siteUrl=site), key=lambda r: day(r["Date"]))
queries = call("GetQueryStats", siteUrl=site)
pages = call("GetPageStats", siteUrl=site)


def total(rows, key):
    out = {}
    for r in rows:
        k = r[key]
        o = out.setdefault(k, {"clics": 0, "impr": 0, "pos": []})
        o["clics"] += r["Clicks"]
        o["impr"] += r["Impressions"]
        if r.get("AvgImpressionPosition", -1) > 0:
            o["pos"].append(r["AvgImpressionPosition"])
    return sorted(out.items(), key=lambda kv: -kv[1]["impr"])


q_tot = total(queries, "Query")
p_tot = total(pages, "Query")  # GetPageStats renvoie l'URL dans le champ "Query"


def pos(o):
    return round(sum(o["pos"]) / len(o["pos"]), 1) if o["pos"] else "-"


with open(os.path.join(BASE, "bing-queries.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["requete", "clics", "impressions", "position"])
    for k, o in q_tot:
        w.writerow([k, o["clics"], o["impr"], pos(o)])

lines = [
    "# Données Bing RÉELLES — " + site, "",
    f"Généré le {datetime.date.today().isoformat()}. Source : API Bing Webmaster Tools.", "",
    "## Trafic par semaine", "", "| semaine du | clics | impr |", "|---|---|---|",
]
weeks = {}
for r in traffic:
    d = day(r["Date"])
    w0 = d - datetime.timedelta(days=d.weekday())
    c, i = weeks.get(w0, (0, 0))
    weeks[w0] = (c + r["Clicks"], i + r["Impressions"])
for w0, (c, i) in sorted(weeks.items()):
    lines.append(f"| {w0} | {c} | {i} |")
for label, rows in (("requêtes", q_tot), ("pages", p_tot)):
    lines += ["", f"## Top {label} (tri impressions)", "",
              f"| {label} | clics | impr | pos |", "|---|---|---|---|"]
    for k, o in rows[:40]:
        lines.append(f"| {k} | {o['clics']} | {o['impr']} | {pos(o)} |")

with open(os.path.join(BASE, "bing-data.md"), "w") as f:
    f.write("\n".join(lines) + "\n")

print(f"OK — {site} : {len(q_tot)} requêtes, {len(p_tot)} pages -> bing-data.md + bing-queries.csv")
