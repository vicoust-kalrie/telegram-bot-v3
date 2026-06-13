Xwhile True:
    print("\n=== KALKULATOR ===")
    print("Ketik 'keluar' untuk berhenti")

    operator = input("Operator (+, -, *, /, %, ^): ")

    if operator == "keluar":
        break

    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if operator == "+":
        hasil = angka1 + angka2
    elif operator == "-":
        hasil = angka1 - angka2
    elif operator == "*":
        hasil = angka1 * angka2
    elif operator == "/":
        hasil = angka1 / angka2
    elif operator == "%":
        hasil = angka1 % angka2
    elif operator == "^":
        hasil = angka1 ** angka2
    else:
        print("Operator tidak valid!")
        continue

    print("Hasil =", hasil)




