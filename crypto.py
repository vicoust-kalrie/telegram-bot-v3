import requests

while True:
    print("\n=== CRYPTO TRACKER ===")
    print("1. Bitcoin (BTC)")
    print("2. Ethereum (ETH)")
    print("3. Solana (SOL)")
    print("4. Keluar")

    pilih = input("Pilih: ")

    if pilih == "4":
        break

    if pilih == "1":
        coin = "bitcoin"
    elif pilih == "2":
        coin = "ethereum"
    elif pilih == "3":
        coin = "solana"
    else:
        print("Pilihan tidak valid!")
        continue

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"

    data = requests.get(url).json()

    harga = data[coin]["usd"]

    print(f"\nHarga {coin.upper()}: ${harga}")
