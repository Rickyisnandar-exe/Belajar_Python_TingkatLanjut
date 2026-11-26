class Pengunjung:

    def __init__(self):
        self.jumlah = 0

    def __call__(self):
        self.jumlah += 1
        return self.jumlah

class Diskon:

    def __init__(self, persen):
        self.persen = persen

    def __call__(self, harga):
        return harga - (harga * self.persen // 100)

counter =  Pengunjung()
print(counter())
print(counter())
print(counter())

diskon20 = Diskon(20)
diskon50 = Diskon(50)

print(diskon20(150000))
print(diskon50(200000))