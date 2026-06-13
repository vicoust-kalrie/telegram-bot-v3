try:
    with open("tugas.txt", "r") as file:
        tugas = file.read().splitlines()
except:
    tugas = []

while True:
    print("\n=== TO-DO LIST ===")
    print("1. Lihat tugas")
    print("2. Tambah tugas")
    print("3. Hapus tugas")
    print("4. Keluar")

    pilihan = input("Pilih: ")

    if pilihan == "1":
        if len(tugas) == 0:
            print("Belum ada tugas.")
        else:
            nomor = 1
            for item in tugas:
                print(f"{nomor}. {item}")
                nomor += 1

    elif pilihan == "2":
        tugas_baru = input("Masukkan tugas: ")
        tugas.append(tugas_baru)

        with open("tugas.txt", "w") as file:
            for item in tugas:
                file.write(item + "\n")

        print("Tugas berhasil ditambahkan!")

    elif pilihan == "3":
        if len(tugas) == 0:
            print("Tidak ada tugas untuk dihapus.")
        else:
            nomor = int(input("Nomor tugas yang mau dihapus: "))
            tugas.pop(nomor - 1)

            with open("tugas.txt", "w") as file:
                for item in tugas:
                    file.write(item + "\n")

            print("Tugas berhasil dihapus!")

    elif pilihan == "4":
        print("Sampai jumpa!")
        break

    else:
        print("Pilihan tidak valid!")
