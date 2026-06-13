from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import os

TOKEN = "8821027234:AAEKA97j1CWGX9lg1uq8jlY3kOgryBcn2AE"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo Haykal! Bot aktif 🔥")


async def btc(update: Update, context: ContextTypes.DEFAULT_TYPE):

    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    data = requests.get(url).json()

    harga = data["bitcoin"]["usd"]

    await update.message.reply_text(f"Harga BTC: ${harga}")


async def market(update: Update, context: ContextTypes.DEFAULT_TYPE):

    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,ripple&vs_currencies=usd"

    data = requests.get(url).json()

    btc = data["bitcoin"]["usd"]
    eth = data["ethereum"]["usd"]
    sol = data["solana"]["usd"]
    xrp = data["ripple"]["usd"]

    pesan = f"""📈 MARKET

BTC : ${btc}
ETH : ${eth}
SOL : ${sol}
XRP : ${xrp}
"""

    await update.message.reply_text(pesan)


async def portfolio(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not os.path.exists("portfolio.txt"):
        await update.message.reply_text("portfolio.txt tidak ditemukan!")
        return

    portfolio_data = {}

    with open("portfolio.txt", "r") as file:
        for baris in file:
            coin, jumlah = baris.strip().split("=")
            portfolio_data[coin] = float(jumlah)

    url = "https://api.coingecko.com/api/v3/simple/price?ids=solana,ripple,ethereum&vs_currencies=usd"

    data = requests.get(url).json()

    harga = {
        "SOL": data["solana"]["usd"],
        "XRP": data["ripple"]["usd"],
        "ETH": data["ethereum"]["usd"]
    }

    total = 0

    pesan = "💰 MY PORTFOLIO\n\n"

    for coin, jumlah in portfolio_data.items():

        if coin in harga:

            nilai = jumlah * harga[coin]
            total += nilai

            pesan += f"{coin} = ${nilai:.2f}\n"

    pesan += f"\nTOTAL = ${total:.2f}"

    await update.message.reply_text(pesan)


async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) != 2:
        await update.message.reply_text("Contoh: /add XRP 50")
        return

    coin = context.args[0].upper()
    jumlah_tambah = float(context.args[1])

    portfolio_data = {}

    if os.path.exists("portfolio.txt"):

        with open("portfolio.txt", "r") as file:
            for baris in file:
                c, j = baris.strip().split("=")
                portfolio_data[c] = float(j)

    if coin in portfolio_data:
        portfolio_data[coin] += jumlah_tambah
    else:
        portfolio_data[coin] = jumlah_tambah

    with open("portfolio.txt", "w") as file:
        for c, j in portfolio_data.items():
            file.write(f"{c}={j}\n")

    await update.message.reply_text(
        f"✅ Berhasil menambahkan {jumlah_tambah} {coin}"
    )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("btc", btc))
app.add_handler(CommandHandler("market", market))
app.add_handler(CommandHandler("portfolio", portfolio))
app.add_handler(CommandHandler("add", add))

print("Bot sedang berjalan...")

app.run_polling()
