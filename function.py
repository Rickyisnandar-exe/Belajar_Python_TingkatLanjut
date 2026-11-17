def my_funtion() :
    x = str(input("masukkan nama anda   :"))
    print(f"nama saya adalah {x}")

def input_angka():
    x = int(input("masukkan angka :"))
    print(x)


# my_funtion()

print("1.  Mulai")
my_funtion()
print("2.  Input")
input_angka()

def tambah(angka1, angka2):
    hasil = angka1 + angka2
    return hasil

total = tambah(10, 20)
print(total)
print(total * 2)

def nama(nama):
    print(f"{nama} isnandar")

nama("ricky")

def negara(country="indonesia"):
    print(f"saya andalah warga negara {country}")


negara()
negara("india")

def pesan(nama, sapaan="selamat pagi pak"):
    print(f"{sapaan}, {nama}")

pesan("budi")
pesan("budi", "selamat malam pak")

def ubahT(*kids):
    print("nama saya adalah :" + kids[0])
    print("nama kedua saya adalah :" + kids[1])
    print("semua nama saya adalah :", kids)
    print(type(kids))

ubahT("ahmad", "saika", "ganjar")

def ubahD(**hasil):
    print(type(hasil))
    print("nama saya adalah", hasil["rnama"])
    print("umur saya adalah", hasil["umur"])
    print("semuanya datanya adalah", hasil)


ubahD(lnama= "ricky", umur= 20, rnama= "isnandar")

def function():
    x = 3000
    print(x)

function()

def function1():
    x = 2000
    return x

hasil = function1()
print(hasil)

def enclosing():
    x =3000
    def panggil():
        print(x)
    panggil()
enclosing()

y = 300

def cetak():
    print(y)


cetak()
y = 300

def cetak():
    y = 200
    print(y)


cetak()
print(y)


x = 20000
def global1():
    global x
    print(x)

global1()
print(x)

def myfunction():
    x = "maret"

    def fungsi2():
        nonlocal x
        x = "agustus"
    fungsi2()
    return x

myfunction()
print(myfunction())

x = "global"
def enclosing():
    x = "enclosing"
    def local():
        x = "local"
        print("local :", x)
    local()
    print("enclosing :", x)
enclosing()
print("global :", x)