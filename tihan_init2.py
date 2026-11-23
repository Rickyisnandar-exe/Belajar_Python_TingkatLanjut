class Barang:
        def __init__(self, nama, harga, stok=4):
                self.nama = nama
                self.harga = harga
                self.stok = stok

        def tampilkan_info(self):
                print(f"nama barang :{self.nama}, harga : {self.harga}, stock :{self.stok}")

        def label_harga(self):
            return f"nama barang : {self.nama}, harga : {self.harga:,}"

        def cetak_struk(self):
                label = self.label_harga()
                print(f"STRUK :{label}")

barang3 = Barang("ayam panggang", 12000, 25)
Barang4 = Barang("ayam marinasi", 8000)

barang3.tampilkan_info()
Barang4.label_harga()
barang3.cetak_struk()