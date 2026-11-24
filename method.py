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

    def tambah(self, jumlah):
        self.stock += jumlah
        print(f"stock : {self.nama}, jadi : {self.stock}")

    def total_harga(self, jumlah):
        return self.harga*jumlah

    def __str__(self):
        return f"nama :{self.nama}, harga :{self.harga}, stock : {self.stock}"

barang1 = Barang("kopi susu jahe", 12000, 20)

print(barang1)
barang1.jual(50)
barang1.jual(30)
barang1.tambah(10)
print(f"total harga : {barang1.total_harga(3)}")
print(barang1)