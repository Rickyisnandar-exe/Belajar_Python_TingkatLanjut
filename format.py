barang = "Kopi susu"
harga = 18000
qty = 4

print(f"item : {barang.upper()} | total : {harga * qty:,}")

nilai_ujian = 87.6543
tingkat_kehadiran = 0.925

print(f"nilai ujian anda : {nilai_ujian:.2f} | kehadiran : {tingkat_kehadiran:.1%}")

stok = 2
print(f"stock :{stok} | ({'segera ristock!' if stok < 5 else "aman"})")