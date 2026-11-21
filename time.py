import datetime

sekarang = datetime.datetime.now()
print(f"waktu sekarang adalah :{sekarang}")

print(f"Tahun sekarang adalah : {sekarang.year}")
print(f"Bulan sekarang adalah : {sekarang.month}")
print(f"Hari sekarang adalah : {sekarang.day}")

hari_proklamasi = datetime.datetime(1945, 8, 17)
print(f"hari proklamasi kemerdekaan indonesia adalah :{hari_proklamasi}")

format_struk = sekarang.strftime("%A, %d %B %Y - %H:%M:%S")
print(format_struk)

print(f"Hari proklamasi jatuh pada :{hari_proklamasi.strftime("%A")}")