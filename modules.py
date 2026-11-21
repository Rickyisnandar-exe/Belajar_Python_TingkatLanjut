info = {
    "nama": "Kopi Senja",
    "pajak": 0.1
}

def hitung_total(harga, jumlah):
    return harga * jumlah

def sapa_pelanggan(nama):
    return f"hallo {nama}, selamat datang di toko{info['nama']}!"