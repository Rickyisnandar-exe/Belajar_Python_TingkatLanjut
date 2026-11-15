number = 15
if number > 0:
    print(f"emang bener sih?")


umur = 17
punya_ktp = True

if umur >= 17 and punya_ktp:
    print("boleh buat sim")

role = "admin"
if role == "admin" or role == "moderator" :
    print("belom hapus kometar")

login = False
if not login:
    print("silakan login dulu")

score = int(input("masukkan nilai :"))

if score >= 80:
    print("lulus")
elif score >= 70:
    print("remedial")
elif score >= 60:
    print("ujian ulang")
else:
    print("tidak lulus")

a = 10
b = 20

if a >= 10: print("sayang akuuu")
print("A") if a > b else print("B")

x = 15

if x > 10 :
    print("a")
    if x > 20 :
        print("ab")
    else:
        print("cd")
else:
    print("b")

age = 15
sim_punya =  False

if age >= 17:
    if sim_punya:
        print("boleh mengemudi")
    else:
        print("belom boleh mengemudi")
else:
    print("buat sim dulu")
score = 60
attendance = 80
submitted =False

if score > 60:
    if attendance > 90:
        if submitted :
            print("anda lulus")
        else:
            print("anda tidak lulus")
    else:
        print("anda nilai anda harus diatas 90")
else:
    print("anda remdial dibawah 60")


if score > 40:
    pass

day = 4
match day :
    case 1:
        print("senin")
    case 2:
        print("selasa")
    case 3:
        print("rabu")
    case 4:
        print("kamis")
    case 5:
        print("jumat")
    case 6:
        print("sabtu")
    case 7:
        print("minggu")

day = 6
match day:
    case 1:
        print("hari ini senin")
    case 2:
        print("hari ini selasa")
    case _:
        print("hari selalu minggu")

match day:
    case 1|2|3|4:
        print("hari selau kerja")
    case _:
        print("weekend")

month = 4
match day:
    case 1|2|3|4|5|6 if month == 5:
        print("bulan gajian")
    case 1|2|3|4|5|6 if month == 4:
        print("minggu full kerja")
    case _:
        print("bukan karyawan kok minta gaji")
