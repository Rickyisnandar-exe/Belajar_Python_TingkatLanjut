class Barang:
    def __init__(self, nama, harga, stock=10):
        self.nama = nama
        self.harga = harga
        self.stock = stock

    def info(self):
        print(f"nama : {self.nama} | kelas : {self.harga} | stock : {self.stock}")

class Makanan(Barang):
    def __init__(self, nama, kadaluarsa, harga, stock=10):
        super().__init__(nama, harga, stock)
        self.kadaluarsa = kadaluarsa

    def info(self):
        super().info()
        print(f" Kadaluarsa : {self.kadaluarsa}")

class Elektronik(Barang):
    pass

roti = Makanan("Roti bakar", "13-02-2007", 20000)
kabel = Elektronik("usb", 2000, 20)

roti.info()
kabel.info()
