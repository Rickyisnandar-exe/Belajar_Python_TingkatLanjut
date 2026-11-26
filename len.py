class Keranjang:

    def __init__(self):
        self.item = []

    def tambah(self, nama_barang):
        self.item.append(nama_barang)

    def __len__(self):
        return len(self.item)

k = Keranjang()
print(len(k))

k.tambah("kopi")
k.tambah("gula")
k.tambah("teh")
k.tambah("teh")
k.tambah("teh")
k.tambah("teh")

print(len(k))