buah = ["apel", "mangga", "jeruk"]

for x in buah:
    if x == "mangga":
        continue
    print(x)

for y in "banana":
    print(y)

for x in range(10):
    print(x)
print("")
for x in range(1, 20):
    print(x)
print("")
for x in range(0,20,3):
    print(x)
print("")
for x in range(30, 25, -1):
    print(x)
print("")

for i in range(6):
    print(i)
else:
    print("selesai")

angka = [3, 7, 12, 5]
target = 7

for n in angka:
    if n == target:
        print("Ketemu!")
        break
else:
    print("Tidak ditemukan")

adj = ["merah", "biru", "kuning"]
buah = ["apple", "jeruk", "pepaya"]

for x in adj:
    for y in buah:
        print(x, y)

for x in range(0, 1, 2):
    pass