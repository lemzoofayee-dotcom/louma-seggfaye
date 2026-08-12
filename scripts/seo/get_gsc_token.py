"""Autorise l'accès LECTURE à Google Search Console (à lancer UNE seule fois).

Réutilise le client OAuth du projet Google Cloud 'louma-ads-api'
(scripts/ads/client_secret.json). Ouvre le navigateur -> se connecter avec le
compte Google PROPRIÉTAIRE de la propriété seggfaye.com dans Search Console ->
le jeton est sauvé dans scripts/seo/gsc_token.json (gitignoré, jamais commité).
"""
import os
from google_auth_oauthlib.flow import InstalledAppFlow

BASE = os.path.dirname(os.path.abspath(__file__))
CLIENT = os.path.join(BASE, "..", "ads", "client_secret.json")
TOKEN = os.path.join(BASE, "gsc_token.json")
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]

flow = InstalledAppFlow.from_client_secrets_file(CLIENT, SCOPES)
creds = flow.run_local_server(port=0, prompt="consent")
with open(TOKEN, "w") as f:
    f.write(creds.to_json())
print("OK — jeton Search Console sauvé dans", TOKEN)
