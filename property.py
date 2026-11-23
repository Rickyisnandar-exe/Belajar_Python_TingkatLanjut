class Barang:
    toko = "Sumber Jaya Makmur"

    def __init__(self, nama, harga, stock=10):
        self.nama = nama
        self.harga = harga
        self.stock = stock

barang1 = Barang("Kopi susu gula aren", 20000, 13)
barang2 = Barang("Susu Jahe", 13000)

print(Barang.toko)
print(barang1.nama, barang2.harga)

barang1.harga = 17000
print(barang1.harga)

Barang.toko = "TOKO RICKY JAYA"
print(barang1.toko, barang2.toko)

barang1.diskon = 10
print(barang1.diskon)

del barang2.stock