import requests

iss_url = "http://api.open-notify.org/iss-now.json"

response_from_iss = requests.get(url=iss_url)

response_from_iss.raise_for_status()

data = response_from_iss.json()

print(data)