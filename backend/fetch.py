import requests

url = "https://pro-api.coingecko.com/api/v3/simple/price"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)
