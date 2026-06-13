import requests

# Baca portfolio dari file
portfolio = {}

with open("portfolio.txt", "r") as file:
    for baris in file:
        nama, jumlah = baris.strip().split("=")
        portfolio[nama] = float(jumlah)

# Ambil harga crypto
url = "https://api.coingecko.com/api/v3/simple/price?ids=solana,ripple,ethereum&vs_currencies=usd"

data = requests.get(url).json()

harga = {
    "SOL": data["solana"]["usd"],
    "XRP": data["ripple"]["usd"],
    "ETH": data["ethereum"]["usd"]
}

total = 0

print("\n=== MY PORTFOLIO ===")

for coin in portfolio:
    nilai = portfolio[coin] * harga[coin]
    total += nilai
    print(f"{coin}: {portfolio[coin]} = ${nilai:.2f}")

print("\n====================")
print(f"TOTAL USD: ${total:.2f}")
