import requests
import json

url = "https://gentle-recreation-production-4113.up.railway.app/call"
payload = {
    "agent_id": "8bc7f91d-a25c-4ae6-b5d0-9248160095f2",
    "recipient_phone_number": "+919840489664"
}

headers = {"Content-Type": "application/json"}

try:
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
