import requests

while True:
    print("\n=== PORTFOLIO MANAGER ===")
    print("1. Lihat Portfolio")
    print("2. Tambah Coin")
    print("3. Keluar")

    pilihan = input("Pilih: ")

    if pilihan == "1":

        portfolio = {}

        try:
            with open("portfolio.txt", "r") as file:
                for baris in file:
                    nama, jumlah = baris.strip().split("=")
                    portfolio[nama] = float(jumlah)
        except:
            print("Portfolio kosong.")
            continue

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

    elif pilihan == "2":

        coin = input("Coin (SOL/XRP/ETH): ").upper()
        jumlah = input("Jumlah: ")

        with open("portfolio.txt", "a") as file:
            file.write(f"{coin}={jumlah}\n")

        print("Coin berhasil ditambahkan!")

    elif pilihan == "3":
        break

    else:
        print("Pilihan tidak valid!")
