tebakan_benar = 999
while True:
    angka = int(input("Tebak angka: "))
    if angka == tebakan_benar:
        print("Tebakan anda benar!")
        break
    else:
        print("Tebakan anda salah, coba lagi.")