import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# # ----------------- Get User Input -----------------
# REPO_NAME = input("Enter Repository Name: ").strip()
# DESCRIPTION = input("Enter Repository Description: ").strip()

# # Ask for Private/Public input and convert to Boolean
# while True:
#     private_input = input("Do you want the repository to be private? (yes/no): ").strip().lower()
#     if private_input in ['yes', 'y']:
#         PRIVATE = True
#         break
#     elif private_input in ['no', 'n']:
#         PRIVATE = False
#         break
#     else:
#         print("Please enter 'yes' or 'no'.")

# ----------------- Get Repo Details from Environment -----------------
REPO_NAME = os.getenv("REPO_NAME")
DESCRIPTION = os.getenv("DESCRIPTION")
PRIVATE_STR = os.getenv("PRIVATE", "true").lower()
PRIVATE = PRIVATE_STR == "true"

# ----------------- Get GitHub Credentials from Environment -----------------
USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")

# Sanity check
if not USERNAME or not TOKEN:
    print("❌ Missing GITHUB_USERNAME or GITHUB_TOKEN in environment.")
    exit(1)

# ----------------- Repo Configuration -----------------
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
