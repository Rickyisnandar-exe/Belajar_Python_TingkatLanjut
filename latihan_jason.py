import json

respon_api = '{"Produk" : "Kopi Susu", "Harga" : 18000, "Tersedia" : true}'

data_produk = json.loads(respon_api)
print(f"nama produk :{data_produk["Produk"]}")
print(f"harga produk : {data_produk["Harga"]}")
print(type(data_produk))



transaksi = {
    "kasir": "Ricky",
    "items": ["Kopi Susu", "Roti Bakar"],
    "lunas": True,
    "catatan": None
}
jason_rapi = json.dumps(transaksi, indent=4, sort_keys=True)
print("\n hasil Json Rapi :")
print(jason_rapi)

data_mentah = '{"nama" : "rina", "member" : true, "point" : 12000}'
ubah_json = json.loads(data_mentah)
print(type(data_mentah))
print(f"nama membernya :{ubah_json["nama"]}")
print(f"point membernya :{ubah_json["point"]}")

order = {
    "id": 1,
    "menu": ["Kopi Susu", "Roti Bakar"],
    "diskon": None
}

urutkan = json.dumps(order, indent=4, sort_keys=True)
print("\n ini adalah ututanya :")
print(urutkan)
