import modules as rt
from modules import sapa_pelanggan
import platform

print(sapa_pelanggan("ricky"))

subtotal = rt.hitung_total(15000, 2)
total_bayar = subtotal + (subtotal * rt.info["pajak"])
print(f"total bayar termasuk pajak adalah : Rp.{int(total_bayar)}")

print("sistem operasi laptop ini pakai : ", platform.system())
print("isi modul di modulus adalah :", dir(rt))