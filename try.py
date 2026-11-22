try:
    masukkan = int(input("masukkkan angka   :"))
    if masukkan < 0:
        raise ValueError("harga tidak boleh minus")
    hasil = 100 / masukkan
except ValueError as b:
    print("EROR:", b)
except ZeroDivisionError:
    print("tidak bisa membagi dengan 0!")
except Exception as e:
    print("terjadi error lainnya", e)
else:
    print("sukses hasilnya", hasil)
finally:
    print("proses pengecekan selesai")