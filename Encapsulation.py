class Barang():

    def __init__(self, nama, harga, stock=10):
        self.nama = nama
        self.harga =harga
        self.__stock = stock

    def get_stock(self):
        return self.__stock

    def set_stock(self, stock):
        if stock >= 0:
            self.__stock = stock
        else:
            print("stock tidak boleh minus")

    def jual(self, jumlah):
        if self.__cek(jumlah):
            self.__stock -= jumlah
            print(f"Terjual {jumlah} {self.nama}. sisa stock :{self.__stock}")
        else:
            print("stock nggak cukup")

    def __cek(self, jumlah):
        return 0 < jumlah <= self.__stock

b = Barang("kopi", 1500, 20)

print(b.get_stock())
b.set_stock(-5)
print(b.get_stock())
b.set_stock(50)
print(b.get_stock())
b.jual(20)
b.jual(50)