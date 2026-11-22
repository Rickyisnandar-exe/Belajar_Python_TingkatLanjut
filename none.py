voucher_diskon = None
print("isi variablenya adalah :", voucher_diskon)
print("type nya adalah  :", type(voucher_diskon))

if voucher_diskon is None:
    print("maka pembeli tidak menggunkaan diskon")
else:
    print("status voucer aktif!!")


print("apakh ini benar None",bool(voucher_diskon))

def salam(nama):
    return f"hallo, {nama} salam kenal ya!"

hasil_fungsi = salam("ricky")
print("nilai kembalian fungsi adalah :", hasil_fungsi)
