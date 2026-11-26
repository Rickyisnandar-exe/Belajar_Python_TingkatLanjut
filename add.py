class Barang:
    def __init__(self, nama, harga, stock=10):
        self.nama = nama
        self.harga = harga
        self.stock = stock

    def __add__(self, other):
        return self.harga + other.harga

    def __str__(self):
        return f"nama : {self.nama} | harga : {self.harga} | stock : {self.stock}"

Barang1 = Barang("kopi gula", 12000, 25)
Barang2 = Barang("kopi susu", 20000)

print(Barang1 + Barang2)