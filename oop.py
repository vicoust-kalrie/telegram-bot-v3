class Coin:

    def __init__(self, nama, jumlah, harga):
        self.nama = nama
        self.jumlah = jumlah
        self.harga = harga

    def nilai(self):
        return self.jumlah * self.harga

btc = Coin("BTC", 0.01, 100000)

print("Nilai:", btc.nilai())
