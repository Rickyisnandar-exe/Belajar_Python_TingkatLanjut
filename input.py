import math

nama = str(input(f"masukkan nama anda   :"))
print(f"hallo nama saya {nama}")


while True:
    data = (input(f"masukkan angka  :"))
    try:
        angka = float(data)
        if angka < 0:
            print("angka tidak boleh minus")
            continue
        break
    except ValueError:
        print("input salah harap masukkan angka atau huruf")


akar = math.sqrt(angka)
print(f"akar quadrat dari {angka} adalah {akar:.2f}")