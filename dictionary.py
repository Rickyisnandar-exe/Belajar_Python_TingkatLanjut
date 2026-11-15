thisDic = {
    "brand" : "ford",
    "model" : "mustang",
    "tahun" : 1928
}

print(thisDic)
print(len(thisDic))
print(type(thisDic))

print(thisDic["brand"])
print(thisDic["model"])

d = {"z": 1, "a": 2, "m": 3}
print(list(d.keys()))
print(list(d.values()))

chrome = {
    "brand" : "Toyota",
    "model" : "invova",
    "electric" : False,
    "tahun" : 2019,
    "warna" : ["merah", "putih", "hitam"]
}

print(chrome)
print(len(chrome))

print(chrome["warna"][1])

print(chrome.get("color", "hitam"))
# print(chrome.get["color"])

thisDic["brand"] = "Suzuki"
print(thisDic)

thisDic.update({"tahun" : 2020})
print(thisDic)

thisDic["pembayaran"] = "cash"
print(thisDic)

thisDic.update({"pembayaran" : "kredit"})

print(thisDic)

thisDic.update({"pembayaran" : "kredit", "model" : "Innova", "brand" : "Toyota"})

print(thisDic)

user = {}
user["nama"] = "budi"
user["kelas"] = 12
user["alamat"] = "jayapura"
print(user)


chrome = {
    "brand" : "Toyota",
    "model" : "invova",
    "electric" : False,
    "tahun" : 2019,
    "warna" : ["merah", "putih", "hitam"]
}

terambil = chrome.pop("model")
print(terambil)
print(chrome)

d = {"brand": "Ford"}
print(d.pop("color", "tidak ada"))
print(d.pop("color", None))


ambil = thisDic.popitem()
print(ambil)
print(thisDic)

del thisDic["model"]
print(thisDic)

thisDic.clear()
print(thisDic)

PromoHari= {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for x in PromoHari:
    print(x)

for i in PromoHari:
    print(PromoHari[i])

for y in PromoHari.values():
    print(y)

for w in PromoHari.keys():
    print(w)

for z, k in PromoHari.items():
    print(z, k)

dicBaru = PromoHari.copy()
print(dicBaru)

dicBaru["model"] = "inova"
print(dicBaru)
print(dicBaru == PromoHari)
print(dicBaru == PromoHari)

dicbaruSekali = dict(PromoHari)
print(dicbaruSekali)

myFamily = {
    "ayah" : {
        "nama" : "wanto",
        "umur" : 19
    },
    "ibu" : {
        "nama" : "sulis",
        "umur" : 20
    },
    "anak" : {
        "nama" : "ahmad",
        "umur" : 19
    }
}

print(myFamily)
print(len(myFamily))
print(myFamily["anak"])
print(myFamily["ayah"]["nama"])