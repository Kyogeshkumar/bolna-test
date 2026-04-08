import requests
import json

url = "https://gentle-recreation-production-4113.up.railway.app/call"
payload = {
    "agent_id": "ae5ee10b-436a-4e62-983d-1ff724a7a7df",
    "recipient_phone_number": "+919840489664"
}

headers = {"Content-Type": "application/json"}

try:
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
