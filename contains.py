class keranjang:

    def __init__(self):
        self.item = []

    def tambah(self, nama_barang):
        self.item.append(nama_barang)

    def __contains__(self, nama_barang):
        return nama_barang in self.item

k = keranjang()
k.tambah("kopi")
k.tambah("gula")

print("gula" in k)
print("roti" in k)
print("gula" not in k)
