import requests

url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": "bitcoin",
    "vs_currencies": "usd",
    "include_24hr_change": "true",
}

response = requests.get(url, params=params, timeout=10)

if response.status_code == 200:
    btc = response.json()["bitcoin"]
    price = btc["usd"]
    change = btc["usd_24h_change"]
    direction = "UP" if change >= 0 else "DOWN"

    print("Bitcoin (BTC)")
    print("-" * 30)
    print(f"Current price: ${price:,.2f}")
    print(f"24h change:    {direction} {abs(change):.2f}%")
else:
    print("Request failed. Status:", response.status_code)
