import re

log_server = "User admin login dari IP 192.168.1.45 pada jam 20:40 dengan kode status 200"

semua_angka = re.findall(r"\d+", log_server)
print(f"semua angka ditemukan : {semua_angka}")

print("")

cek_awal = re.search(r"^User", log_server)
if cek_awal:
    print(f"validd!! text diawali dengan : {cek_awal.group()}")
    print(f"posisi inedxnya : {cek_awal.span()}")
else:
    print("tidak ada yang cocok")

daftar_kata = re.split(r"\s", log_server)
print(f"jumlah kata : {len(daftar_kata)}")

log_tersensor = re.sub(r"\d", "*",log_server)
print(f"log tersensor :{log_tersensor}")