import requests
import os

def baca_portfolio():
    portfolio = {}

    if os.path.exists("portfolio.txt"):
        with open("portfolio.txt", "r") as file:
            for baris in file:
                coin, jumlah = baris.strip().split("=")
                portfolio[coin] = float(jumlah)

    return portfolio


def ambil_harga():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=solana,ripple,ethereum&vs_currencies=usd"

    data = requests.get(url).json()

    return {
        "SOL": data["solana"]["usd"],
        "XRP": data["ripple"]["usd"],
        "ETH": data["ethereum"]["usd"]
    }


def hitung_total(portfolio, harga):
    total = 0

    print("\n=== MY PORTFOLIO ===\n")

    for coin, jumlah in portfolio.items():

        if coin in harga:

            nilai = jumlah * harga[coin]
            total += nilai

            print(f"{coin} = {jumlah} (${nilai:.2f})")

    print("\n====================")
    print(f"TOTAL USD = ${total:.2f}")


portfolio = baca_portfolio()
harga = ambil_harga()

hitung_total(portfolio, harga)
