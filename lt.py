class Barang:
    def __init__(self, nama, harga, stock=10):
        self.nama = nama
        self.harga = harga
        self.stock = stock

    def __lt__(self, other):
        return self.harga < other.harga

    def __str__(self):
        return f"nama : {self.nama} | harga : {self.harga} | stok : {self.stock}"


Barang1 = Barang("kopi", 2000, 20)
Barang2 = Barang("gula", 3000)
barang3 = Barang("Roti", 12000)

print(Barang1 < Barang2)
print(Barang1)
print(Barang2)

urut = sorted([Barang1, Barang2, barang3])
for b in urut:
    print("-", b)