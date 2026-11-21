data_kasir = [
    "NAMA_PRODUK | HARGA",   # Indeks 0 (Header)
    "Kopi Susu   | 15000",   # Indeks 1
    "Roti Bakar  | 12000",   # Indeks 2
    "Es Teh      | 5000"     # Indeks 3
]
print(data_kasir)
print(type(data_kasir))
print(len(data_kasir))

petunjuk_data = iter(data_kasir)
print(petunjuk_data)
print(type(petunjuk_data))

header = next(petunjuk_data)
print("Header Dilewati :", header)
print("_" * 25)

for baris in petunjuk_data:
    print("memproses :", baris)

buah = ("apel", "pisang", "ceri")
print(buah)
it_buah = iter(buah)

print("iter == 1")
print(next(it_buah))
print(next(it_buah))
print(next(it_buah))

kata = "HAI"
ubah = iter(kata)
print(next(ubah))
print(next(ubah))
print(next(ubah))

print("")
for baris in "KODE":
    print(baris)

buah = [10, 20]
def __next__(self):
    if self.buah <= 3:
        x = self.buah
        self.buah += 1
        return x
    else:
        raise StopIteration

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)    # 1 sampai 20, lalu berhenti sendiri