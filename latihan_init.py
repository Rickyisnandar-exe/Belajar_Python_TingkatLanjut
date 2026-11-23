class Barang:
    def __init__(self, nama, harga, stock=10):
        self.nama = nama
        self.harga = harga
        self.stock = stock

Barang1 = Barang("Kopi susu gula aren", 15000, 25)
Barang2 = Barang("Kopi susu luwak white coffe", 18000)


print(f"nama barang : {Barang1.nama} | harga : {Barang1.harga:,} | stock : {Barang1.stock}")
print(f"nama barang : {Barang2.nama} | harga : {Barang2.harga:,} | stock : {Barang2.stock}")
