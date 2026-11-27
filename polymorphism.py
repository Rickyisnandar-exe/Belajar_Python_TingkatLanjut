# class Hewan():
#     def suara(self):
#         print("....")

# class Kucing(Hewan):
#     def suara(self):
#         print("Meong")

# class Anjing(Hewan):
#     def suara(self):
#         print("guk guk")

# class Ikan(Hewan):
#     pass

# for h in (Kucing(), Anjing(), Ikan()):
#     h.suara()


class Notifikasi():
    def kirim(self, pesan):
        print(f"[UMUM] pesan dari : {pesan}")
    
class NotifWa(Notifikasi):
    def kirim(self, pesan):
        print(f"[WhatsApp] centang biru ke nomor tujuan : '{pesan}'")

class NotifEmail(Notifikasi):
    def kirim(self, pesan):
        print(f"[Email] Mengirim subjek dan ibox ke : '{pesan}'")

class NotifLog(Notifikasi):
    pass


Daftar_notif = [
    NotifWa(),
    NotifEmail(),
    NotifLog(),

]

for x in Daftar_notif:
    x.kirim("kode verivikasi kamu : 8881")