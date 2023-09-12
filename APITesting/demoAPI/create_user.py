import requests
import json
payload = {
    "name": "Arun",
    "job": "Automation lead"
        }
print(type(payload))

response = requests.post("https://reqres.in/api/users?page=2", data=payload)
print(response.json())
assert response.json()['name'] == "Arun", "wrong name created"
