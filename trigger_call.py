import requests
import json

url = "https://gentle-recreation-production-4113.up.railway.app/call"
payload = {
    "agent_id": "a57555b0-b83f-4c47-9d1c-77db73b21059",
    "recipient_phone_number": "+919840489664"
}

headers = {"Content-Type": "application/json"}

try:
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
