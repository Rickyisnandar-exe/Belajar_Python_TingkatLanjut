class Barang:
    def __init__(self, nama, harga, stock=10):
        self.nama = nama
        self.harga = harga
        self.stock = stock

    def __str__(self):
        return f"Nama Barang : {self.nama} | Harga : {self.harga} | Stock : {self.stock}"

    def __repr__(self):
        return f"Barang(nama={self.nama!r}, harga={self.harga}, stock={self.stock})"

Barang1 = Barang("kopi susu madu", 15000, 20)
Barang2 = Barang("kopi zero sugar", 12000)

print(Barang1)
print(repr(Barang2))
print([Barang1, Barang2])