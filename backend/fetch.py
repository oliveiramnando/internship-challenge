import requests

url = "https://api.coingecko.com/api/v3/simple/price"

def getCoinSummary(coin: str) -> dict | None:
    params = {
            "ids": coin.lower(),
            "vs_currencies": "usd",
            "include_market_cap": "true",
            "include_24hr_vol": "true", 
            "include_24hr_change": "true",
            "include_last_updated_at": "true"
        }
    headers = {"accept": "application/json"}

    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    info = data.get(coin.lower())

    if not info:
        return None

    return {
        "name": coin.capitalize(),
        "symbol": coin.upper(),
        "usd": info["usd"],
        "usd_market_cap": info["usd_market_cap"],
        "usd_24h_vol": info["usd_24h_vol"],
        "usd_24h_change": info["usd_24h_change"],
        "last_updated_at": info["last_updated_at"] 
    }
