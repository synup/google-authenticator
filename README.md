# Google Authenticator

A simple Python Flask app that performs Google OAuth 2.0 authentication and displays the token response (access token, refresh token, etc.).

## Prerequisites

- Python 3.8+
- A Google Cloud project with OAuth 2.0 credentials

## Google Cloud Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project (or select an existing one)
3. Navigate to **APIs & Services > Credentials**
4. Create an **OAuth 2.0 Client ID** (Application type: Web application)
5. Add `http://localhost:8080/callback` as an **Authorized redirect URI**
6. Enable any APIs required by your scopes (e.g., Google Business Profile API)

## Installation

```bash
git clone <repo-url>
cd google-authenticator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```
GOOGLE_CLIENT_ID=your-client-id
GOOGLE_CLIENT_SECRET=your-client-secret
GOOGLE_SCOPE=email,profile,https://www.googleapis.com/auth/plus.business.manage
GOOGLE_ACCESS_TYPE=offline
```

## Usage

```bash
source venv/bin/activate
python app.py
```

Open http://localhost:8080 in your browser. You will be redirected to Google's consent screen. After granting access, the callback page displays the full JSON token response from Google, including:

- `access_token`
- `refresh_token` (only on first consent or when `prompt=consent` is set)
- `expires_in`
- `token_type`
- `scope`
- `id_token`

## Project Structure

```
├── .env                # OAuth credentials (not committed)
├── .gitignore
├── app.py              # Flask app with OAuth flow
├── requirements.txt    # Python dependencies
├── CLAUDE.md           # Notes for Claude Code
└── README.md
```
