class Barang:
    def __init__(self, nama, harga, stock=10):
        self.nama = nama
        self.harga = harga
        self.stock = stock

    def __eq__(self, other):
        return self.nama == other.nama and self.harga == other.harga

Barang1 = Barang("kopi", 12000, 20)
Barang2 = Barang("kopi", 12000, 12)
Barang3 = Barang("roti", 12000)

print(Barang1 == Barang2)
print(Barang2 == Barang3)
print(Barang1 is Barang2)
