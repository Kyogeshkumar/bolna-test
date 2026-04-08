import requests
import json

try:
    response = requests.get("http://localhost:4040/api/tunnels")
    data = response.json()
    for tunnel in data['tunnels']:
        print(f"{tunnel['name']}: {tunnel['public_url']}")
except Exception as e:
    print(f"Error: {e}")
