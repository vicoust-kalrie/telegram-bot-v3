import os

portfolio = {}

# Load data dari file
if os.path.exists("portfolio.txt"):
    with open("portfolio.txt", "r") as file:
        for baris in file:
            coin, jumlah = baris.strip().split("=")
            portfolio[coin] = float(jumlah)

while True:
    print("\n=== PORTFOLIO MANAGER PRO ===")
    print("1. Lihat Portfolio")
    print("2. Tambah Coin")
    print("3. Update Coin")
    print("4. Hapus Coin")
    print("5. Simpan")
    print("6. Keluar")

    pilihan = input("Pilih: ")

    if pilihan == "1":

        if len(portfolio) == 0:
            print("Portfolio kosong.")
        else:
            for coin, jumlah in portfolio.items():
                print(f"{coin} = {jumlah}")

    elif pilihan == "2":

        coin = input("Nama Coin: ").upper()
        jumlah = float(input("Jumlah: "))

        portfolio[coin] = jumlah

        print("Coin berhasil ditambahkan!")

    elif pilihan == "3":

        coin = input("Coin yang mau diupdate: ").upper()

        if coin in portfolio:

            jumlah_baru = float(input("Jumlah baru: "))
            portfolio[coin] = jumlah_baru

            print("Coin berhasil diupdate!")

        else:

            print("Coin tidak ditemukan!")

    elif pilihan == "4":

        coin = input("Coin yang mau dihapus: ").upper()

        if coin in portfolio:

            del portfolio[coin]

            print("Coin berhasil dihapus!")

        else:

            print("Coin tidak ditemukan!")

    elif pilihan == "5":

        with open("portfolio.txt", "w") as file:
            for coin, jumlah in portfolio.items():
                file.write(f"{coin}={jumlah}\n")

        print("Portfolio berhasil disimpan!")

    elif pilihan == "6":

        print("Sampai jumpa!")
        break

    else:

        print("Pilihan tidak valid!")
