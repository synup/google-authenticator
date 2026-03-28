import os
import json
import urllib.parse

from dotenv import load_dotenv
from flask import Flask, redirect, request

import requests

load_dotenv()

app = Flask(__name__)

CLIENT_ID = os.environ["GOOGLE_CLIENT_ID"]
CLIENT_SECRET = os.environ["GOOGLE_CLIENT_SECRET"]
SCOPE = os.environ["GOOGLE_SCOPE"]
ACCESS_TYPE = os.environ["GOOGLE_ACCESS_TYPE"]
REDIRECT_URI = "http://localhost:8080/callback"

GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"


@app.route("/")
def index():
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": SCOPE.replace(",", " "),
        "access_type": ACCESS_TYPE,
        "prompt": "consent",
    }
    auth_url = f"{GOOGLE_AUTH_URL}?{urllib.parse.urlencode(params)}"
    return redirect(auth_url)


@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        error = request.args.get("error", "unknown error")
        return f"<h1>Error</h1><pre>{error}</pre>", 400

    token_response = requests.post(
        GOOGLE_TOKEN_URL,
        data={
            "code": code,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "redirect_uri": REDIRECT_URI,
            "grant_type": "authorization_code",
        },
    )

    token_data = token_response.json()
    formatted = json.dumps(token_data, indent=2)

    return f"""
    <h1>Google OAuth Response</h1>
    <pre style="background:#f4f4f4;padding:16px;border-radius:8px;font-size:14px;">{formatted}</pre>
    """


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
