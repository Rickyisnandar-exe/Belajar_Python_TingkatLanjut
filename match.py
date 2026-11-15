
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
