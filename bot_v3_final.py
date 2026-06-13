from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import os
import sqlite3

TOKEN = "8821027234:AAEKA97j1CWGX9lg1uq8jlY3kOgryBcn2AE"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo Haykal! Bot aktif 🔥")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):

    pesan = """
📚 DAFTAR COMMAND

/start
/help

/fear 

/btc
/eth
/sol
/xrp

/market
/portfolio

/add COIN JUMLAH
/remove COIN JUMLAH
"""

    await update.message.reply_text(pesan)

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

async def fear(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:

        data = requests.get(
            "https://api.alternative.me/fng/"
        ).json()

        nilai = data["data"][0]["value"]
        status = data["data"][0]["value_classification"]

        await update.message.reply_text(
            f"😱 Fear & Greed Index\n\nNilai : {nilai}\nStatus : {status}"
        )

    except:

        await update.message.reply_text(
            "Gagal mengambil data Fear & Greed."
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

    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM portfolio")

    data_portfolio = cursor.fetchall()

    conn.close()

    data = requests.get(
        "https://api.coingecko.com/api/v3/simple/price?ids=solana,ripple,ethereum&vs_currencies=usd"
    ).json()

    harga = {
        "SOL": data["solana"]["usd"],
        "XRP": data["ripple"]["usd"],
        "ETH": data["ethereum"]["usd"]
    }

    total = 0

    pesan = "💰 MY PORTFOLIO (SQLITE)\n\n"

    for coin, jumlah in data_portfolio:

        if coin in harga:

            nilai = jumlah * harga[coin]

            total += nilai

            pesan += f"{coin} = ${nilai:.2f}\n"

    pesan += f"\nTOTAL = ${total:.2f}"

    await update.message.reply_text(pesan)

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:

        coin = context.args[0].upper()
        jumlah = float(context.args[1])

        conn = sqlite3.connect("portfolio.db")
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE portfolio SET jumlah = jumlah + ? WHERE coin = ?",
            (jumlah, coin)
        )

        conn.commit()
        conn.close()

        await update.message.reply_text(
            f"✅ Berhasil menambah {jumlah} {coin}"
        )

    except:

        await update.message.reply_text(
            "Format: /add XRP 10"
        )

async def remove(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:

        coin = context.args[0].upper()
        jumlah = float(context.args[1])

        conn = sqlite3.connect("portfolio.db")
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE portfolio SET jumlah = jumlah - ? WHERE coin = ?",
            (jumlah, coin)
        )

        conn.commit()
        conn.close()

        await update.message.reply_text(
            f"✅ Berhasil mengurangi {jumlah} {coin}"
        )

    except:

        await update.message.reply_text(
            "Format: /remove XRP 5"
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_cmd))
app.add_handler(CommandHandler("fear", fear))
app.add_handler(CommandHandler("btc", btc))
app.add_handler(CommandHandler("eth", eth))
app.add_handler(CommandHandler("sol", sol))
app.add_handler(CommandHandler("xrp", xrp))
app.add_handler(CommandHandler("market", market))
app.add_handler(CommandHandler("portfolio", portfolio))
app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("remove", remove))
print("Bot sedang berjalan...")

app.run_polling()
# TEST NANO
 
