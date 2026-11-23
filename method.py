class Barang:
    toko = "Ricky Isnandar"

    def __init__(self, nama, harga, stock=10):
        self.nama = nama
        self.harga = harga
        self.stock = stock

    def jual(self, jumlah):
        if jumlah <= self.stock:
            self.stock -= jumlah
            print(f"Terjual :{jumlah} {self.nama}. stok sisa: {self.stock}")
        else:
            print(f"stok : {self.nama} tidak cukup!!!")
            