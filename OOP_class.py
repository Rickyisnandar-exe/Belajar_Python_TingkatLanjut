class menu_kantin:
    kategori = "Ayam goreng"
    harga = 20000

print(menu_kantin())

menu1 = menu_kantin()
menu2 = menu_kantin()
print(menu1)
print(menu2)

menu2.harga = 25000
menu1.kategori = "Nasi Goreng"

print(f"Menu 1 > kategori : {menu1.kategori }, harga : {menu1.harga:,}")
print(f"Menu 2 > kategori : {menu2.kategori }, harga : {menu2.harga:,}")

# del menu1
# print(menu1.harga)
class fitur_baru:
    pass

print(f"Program OOP pertama berhasil jalan!")


class Mahasiswa:
    kampus = "Universitas Pamulang"
    semester = 1

mhs1 = Mahasiswa()
mhs2 = Mahasiswa()



