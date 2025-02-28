from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import requests

# Path to the client secret file you downloaded
CLIENT_SECRET_FILE = "/home/waleedashir6/PersonaMHC/client_secret_1023019439641-vimd6415ki8ra48n04irnhuj4331ccdi.apps.googleusercontent.com.json"

# Scopes required for the Generative Language API
SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]

# Authenticate and get credentials
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
creds = flow.run_local_server(port=0)

# Make API request with authenticated credentials
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/text-bison-001:generateText"
headers = {
    "Authorization": f"Bearer {creds.token}",
    "Content-Type": "application/json",
}

data = {
    "prompt": {
        "text": "Tell me a short story about AI."
    }
}

response = requests.post(API_URL, json=data, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.text)
