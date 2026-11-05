<<<<<<< HEAD
#text
nama = "ricky isnandar"
kota = "belitang"
umur = 19

print(nama.upper())
print(nama.lower())
print(len(nama))
print('halo' + (nama))

b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-8:-1])

a = "Hello, World!"
print(a.upper())
print(a.lower())

a = "   Hello, World!   "
print(a.strip())
print(a.strip())

a = "Hello, World!"
print(a.replace("H", "J"))
print(a.replace("l", "L"))

a = "Hello, World!"
print(a.split(","))

nama = "  budi santoso  "
nama_bersih = nama.strip().title()
print(nama_bersih)

jawaban = "YA"
if jawaban.lower() == "ya":
    print("setuju")

harga = "Rp15.000"
angka_asli = harga.replace("Rp","").replace(".", "")
print(angka_asli)

a = "Hello"
b = "World"
print(a + b)

c = a + " " + b
print(c)

depan = "Budi"
belakang = "Santoso"
print(depan + belakang)
print(depan + " " + belakang)
print("hallo nama saya " + depan)

print("ha" * 20)
print("-" * 20)

nama = "Budi"
umur = 1234567.891

print(f"nama saya adalah {nama}, dan umur saya {umur} tahun")
print(f"saya ubah nama saya {nama.lower()}")

print(f"nama saya adalah {umur:.2f}")
print(f"nama saya adalah {umur:,.2f}")
print(f"nama saya adalah {umur:.2f}")
print(f"nama saya adalah {umur:.1%}")

total = 1250000
rata_rata = 85.7345

print(f"total penjualan saya adalah {total:,}")
print(f"rata_nilaya adalah {rata_rata:.2f}")

print('Hallo i\'am ricky si paling data')
print("hallo nama saya ricky salam Kenal,\"hallo\"")
print("hallo nama saya \\ricky\\ salam Kenal,\"hallo\"")

# print(input("masukkan nama anda\t:"))
# print(input("masukkan nama anda\n:"))
# print(input("masukkan nama anda :"))
nama = "rICKY isnandar"
print(f"{nama.title()}")
print(f"{nama.capitalize()}")

a = "   halo   "
print(a.strip())
print(a.lstrip())
print(a.rstrip())

a = "belajar python itu asyik, python seru"
print(a.find("python"))
print(a.find("java"))
print(a.count("python"))
print(a.startswith("python"))
print("belajar_sql.pdf".endswith(".pdf"))

kata = "saya, suka, python"
kalimat = kata.split(",")
print(kalimat)

kalimat_1 = "-".join(kalimat)
print(f"{kalimat_1}")

angka = "123"
print(angka.isdigit())
angka_1 = "hallo"
print(angka_1.isalpha())
angka_2 = "budi123"
print(angka_2.isalnum())

print("menu".center(20, "-"))
print("menu".ljust(20) + "|")
print("menu".rjust(10))
=======
#text
nama = "ricky isnandar"
kota = "belitang"
umur = 19

print(nama.upper())
print(nama.lower())
print(len(nama))
print('halo' + (nama))

b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-8:-1])

a = "Hello, World!"
print(a.upper())
print(a.lower())

a = "   Hello, World!   "
print(a.strip())
print(a.strip())

a = "Hello, World!"
print(a.replace("H", "J"))
print(a.replace("l", "L"))

a = "Hello, World!"
print(a.split(","))

nama = "  budi santoso  "
nama_bersih = nama.strip().title()
print(nama_bersih)

jawaban = "YA"
if jawaban.lower() == "ya":
    print("setuju")

harga = "Rp15.000"
angka_asli = harga.replace("Rp","").replace(".", "")
print(angka_asli)

a = "Hello"
b = "World"
print(a + b)

c = a + " " + b
print(c)

depan = "Budi"
belakang = "Santoso"
print(depan + belakang)
print(depan + " " + belakang)
print("hallo nama saya " + depan)

print("ha" * 20)
print("-" * 20)

nama = "Budi"
umur = 1234567.891

print(f"nama saya adalah {nama}, dan umur saya {umur} tahun")
print(f"saya ubah nama saya {nama.lower()}")

print(f"nama saya adalah {umur:.2f}")
print(f"nama saya adalah {umur:,.2f}")
print(f"nama saya adalah {umur:.2f}")
print(f"nama saya adalah {umur:.1%}")

total = 1250000
rata_rata = 85.7345

print(f"total penjualan saya adalah {total:,}")
print(f"rata_nilaya adalah {rata_rata:.2f}")

print('Hallo i\'am ricky si paling data')
print("hallo nama saya ricky salam Kenal,\"hallo\"")
print("hallo nama saya \\ricky\\ salam Kenal,\"hallo\"")

# print(input("masukkan nama anda\t:"))
# print(input("masukkan nama anda\n:"))
# print(input("masukkan nama anda :"))
nama = "rICKY isnandar"
print(f"{nama.title()}")
print(f"{nama.capitalize()}")

a = "   halo   "
print(a.strip())
print(a.lstrip())
print(a.rstrip())

a = "belajar python itu asyik, python seru"
print(a.find("python"))
print(a.find("java"))
print(a.count("python"))
print(a.startswith("python"))
print("belajar_sql.pdf".endswith(".pdf"))

kata = "saya, suka, python"
kalimat = kata.split(",")
print(kalimat)

kalimat_1 = "-".join(kalimat)
print(f"{kalimat_1}")

angka = "123"
print(angka.isdigit())
angka_1 = "hallo"
print(angka_1.isalpha())
angka_2 = "budi123"
print(angka_2.isalnum())

print("menu".center(20, "-"))
print("menu".ljust(20) + "|")
print("menu".rjust(10))
>>>>>>> 98bc725337da4ba6f2039626ec96f8ac154dd0a7
print("47".zfill(5))