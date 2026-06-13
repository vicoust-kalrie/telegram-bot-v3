import requests

# Harga crypto
url = "https://api.coingecko.com/api/v3/simple/price?ids=solana,ripple,ethereum&vs_currencies=usd"

data = requests.get(url).json()

sol_harga = data["solana"]["usd"]
xrp_harga = data["ripple"]["usd"]
eth_harga = data["ethereum"]["usd"]

# Portfolio
sol_jumlah = 1
xrp_jumlah = 25
eth_jumlah = 0.005

sol_value = sol_jumlah * sol_harga
xrp_value = xrp_jumlah * xrp_harga
eth_value = eth_jumlah * eth_harga

total_usd = sol_value + xrp_value + eth_value

# Kurs perkiraan USD ke IDR
usd_to_idr = 16000

total_idr = total_usd * usd_to_idr

print("\n=== MY PORTFOLIO ===")
print(f"SOL : {sol_jumlah} = ${sol_value:.2f}")
print(f"XRP : {xrp_jumlah} = ${xrp_value:.2f}")
print(f"ETH : {eth_jumlah} = ${eth_value:.2f}")

print("\n====================")
print(f"TOTAL USD : ${total_usd:.2f}")
print(f"TOTAL IDR : Rp {total_idr:,.0f}")
