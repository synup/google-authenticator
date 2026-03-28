# Google Authenticator

Simple Python Flask app that performs Google OAuth 2.0 authentication and displays the raw token response (access token, refresh token, etc.).

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Then open http://localhost:8080 — it redirects to Google's consent screen. After granting access, the callback page displays the full token JSON from Google.

## Configuration

All credentials are stored in `.env` (not committed to git):
- `GOOGLE_CLIENT_ID` — OAuth client ID
- `GOOGLE_CLIENT_SECRET` — OAuth client secret
- `GOOGLE_SCOPE` — Comma-separated scopes
- `GOOGLE_ACCESS_TYPE` — Set to `offline` to receive a refresh token

## Key Details

- Redirect URI: `http://localhost:8080/callback` (must be registered in Google Cloud Console)
- `prompt=consent` is set to force the consent screen so Google always returns a refresh token
- The callback page renders the full JSON response from Google's token endpoint
