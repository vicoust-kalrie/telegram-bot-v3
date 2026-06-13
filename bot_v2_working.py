from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import os

TOKEN = "8821027234:AAEKA97j1CWGX9lg1uq8jlY3kOgryBcn2AE"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo Haykal! Bot aktif 🔥")

async def eth(update: Update, context: ContextTypes.DEFAULT_TYPE):

    data = requests.get(
        "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    ).json()

    await update.message.reply_text(
        f"ETH = ${data['ethereum']['usd']}"
    )


async def sol(update: Update, context: ContextTypes.DEFAULT_TYPE):

    data = requests.get(
        "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd"
    ).json()

    await update.message.reply_text(
        f"SOL = ${data['solana']['usd']}"
    )


async def xrp(update: Update, context: ContextTypes.DEFAULT_TYPE):

    data = requests.get(
        "https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd"
    ).json()

    await update.message.reply_text(
        f"XRP = ${data['ripple']['usd']}"
    )


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


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("btc", btc))
app.add_handler(CommandHandler("eth", eth))
app.add_handler(CommandHandler("sol", sol))
app.add_handler(CommandHandler("xrp", xrp))
app.add_handler(CommandHandler("market", market))
app.add_handler(CommandHandler("portfolio", portfolio))

print("Bot sedang berjalan...")

app.run_polling()
# TEST NANO
 
