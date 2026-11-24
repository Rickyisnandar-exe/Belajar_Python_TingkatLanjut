class Barang:
    def __init__(self, nama, harga, stok=10):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def __str__(self):
        return f"Nama : {self.nama}, harga : {self.harga}, Stok : {self.stok}"

Barang1 = Barang("ayam goreng", 13000, 20)
Barang2 = Barang("Ayam Panggang", 15000)

print(Barang1)
print(Barang2)

text = str(Barang2)
print(f"cetak struk : {text}")

daftar = [Barang1, Barang2]

for b in daftar:
    print("--", b)