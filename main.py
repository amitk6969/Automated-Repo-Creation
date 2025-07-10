import requests
import json
import os
from dotenv import load_dotenv

# ----------------- Load Environment Variables -----------------
load_dotenv()  # Loads variables from a .env file

# Get GitHub credentials from environment
USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")

# Sanity check
if not USERNAME or not TOKEN:
    print("❌ Missing USERNAME or TOKEN in .env file.")
    exit(1)

# ----------------- Repo Configuration -----------------
REPO_NAME = "my-new-repo"  
DESCRIPTION = "This repository was created using an automated Python script."
PRIVATE = True  # True = private repo, False = public
AUTO_INIT = True
GITIGNORE_TEMPLATE = "Python"

# ----------------- Headers and Payload -----------------
headers = {
    "Authorization": f"Bearer {TOKEN}",  # For fine-grained tokens use 'Bearer'
    "Accept": "application/vnd.github+json"
}

data = {
    "name": REPO_NAME,
    "description": DESCRIPTION,
    "private": PRIVATE,
    "auto_init": AUTO_INIT,
    "gitignore_template": GITIGNORE_TEMPLATE
}

# GitHub API endpoint to create repo
url = "https://api.github.com/user/repos"

# ----------------- Send the Request -----------------
response = requests.post(url, headers=headers, json=data)

# ----------------- Handle the Response -----------------
if response.status_code == 201:
    print(f"✅ Repository '{REPO_NAME}' created successfully!")
    print("🔗 URL:", response.json().get('html_url'))
else:
    print(f"❌ Failed to create repository. Status code: {response.status_code}")
    print("🔎 Error details:")
    print(json.dumps(response.json(), indent=2))
