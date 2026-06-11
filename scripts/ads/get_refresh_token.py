from google_auth_oauthlib.flow import InstalledAppFlow

flow = InstalledAppFlow.from_client_secrets_file(
    "/Users/laminefaye/Projets/mes sites web/scripts/ads/client_secret.json",
    scopes=["https://www.googleapis.com/auth/adwords"],
)
creds = flow.run_local_server(port=8765, prompt="consent", access_type="offline", open_browser=False)
with open("/Users/laminefaye/Projets/mes sites web/scripts/ads/refresh_token.txt", "w") as f:
    f.write(creds.refresh_token or "")
print("REFRESH_TOKEN_OK")
