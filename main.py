import random
print("       Selamat datang di TIMEZONE")
def garis():
    print('='*40)
def daftar_menu():
    while True:
        menu = input("""============= Daftar Menu ==============
    1. Tebak Angka
    2. Batu Gunting Kertas
    3. Rolling number
    4. Tukar hadiah
    5. Keluar
    Silahkan pilih menu: """)
        if menu.isdigit():
            menu = int(menu)
            if menu == 1:
                game1()
            elif menu == 2:
                game2()
            elif menu == 3:
                game3()
            elif menu == 4:
                tukar_hadiah()
            elif menu == 5:
                keluar()
            else:
                print("Input tidak valid !")
        else:
            print("Input tidak valid !")
            garis()
def game1():
    print("============= TEBAK ANGKA ==============")
    input ("Tekan ENTER untuk mulai: ")
    tiket = 1
    while True:
        angka_acak = random.randint(0,9)
        garis()
        while True:
            user_pilih = input("""Tekan Q untuk keluar. 
Tebak angka antara 0 sampai 9: """)
            if user_pilih.isdigit():
                user_pilih = int(user_pilih)
            elif user_pilih.lower() == 'q':
                daftar_menu()
            else:                                                                                                                                                                                                                                                                                                                                                                                                                                         
                print("Input tidak valid !")
                continue
            if user_pilih == angka_acak:
                print("Tebakan benar angka adalah:",angka_acak)
                while True:
                    lanjut = input("""Apakah anda ingin lanjut bermain ?
                        (y/t): """)
                    if lanjut.lower() == "y":
                        tiket += 1
                        break
                    elif lanjut.lower() == "t":
                        print(f"Terimakasih. kamu dapat: {tiket} tiket.")
                        input("Tekan ENTER untuk keluar: ")
                        garis()
                        daftar_menu()
                    else:
                        print("Input tidak valid !")
                break         
            elif user_pilih > angka_acak:
                print("SALAH ! Angka terlalu besar")
            else:
                print("SALAH ! Angka terlalu kecil")
def game2():
    user_menang = 0
    com_menang = 0
    seri = 0
    options = ["batu", "gunting", "kertas"]
    print("========== BATU GUNTING KERTAS ==========")
    input ("Tekan ENTER untuk mulai: ")
    while True:
        user_pilih = input("""Ketik Batu/Gunting/Kertas atau tekan Q
untuk keluar: """).lower()
        if user_pilih == "q":
            break
        if user_pilih not in options:
            print("Input tidak valid !")
            continue
        com_pilih = options[random.randint(0, 2)]
        print("    Komputer : ", com_pilih + ".")
        if user_pilih == "batu" and com_pilih == "gunting":
            print("    Kamu menang!")
            user_menang += 1
        elif user_pilih == "gunting" and com_pilih == "kertas":
            print("    Kamu menang!")
            user_menang += 1
        elif user_pilih == "kertas" and com_pilih == "batu":
            print("    Kamu menang!")
            user_menang += 1
        elif user_pilih == com_pilih:
            print("    Hasil seri")
            seri += 1
        else:
            print("    Kamu kalah!")
            com_menang += 1
    print(f"""Perolehan skor :
    Kamu     = {user_menang} kali menang.
    Komputer = {com_menang} kali menang.
    Seri     = {seri} kali.
    Kamu dapat : {user_menang} tiket.""")
    input("Tekan ENTER untuk keluar: ")
    garis()
    daftar_menu()
def game3():
    print("========== ROOLING NUMBER ==========")
    tiket = 0
    while True:
        roll = input("""Tekan ENTER untuk roll atau
tekan Q untuk keluar: """).lower()
        if roll == "q":
            garis()
            print(f"Terimakasih. Kamu dapat: {tiket} tiket.")
            input("Tekan ENTER untuk keluar: ")
            garis()
            daftar_menu()
        angka1 = random.randint(0,9)
        angka2 = random.randint(0,9)
        angka3 = random.randint(0,9)
        print('             *',angka1,angka2,angka3,'*')
        if angka1 != angka2 and angka2 != angka3 and angka1 != angka3:
            print("Tidak ada angka yang sama. poin + 1",)
            tiket += 1
            print("Total poin: ",tiket)
        elif angka1 == angka2 == angka3:
            print("Jackpot. Poin + 5")
            tiket += 5
            print("Total poin: ",tiket)
        else:
            print("Dua angka sama. Poin + 2")
            tiket += 2
            print("Total poin: ",tiket)
def tukar_hadiah():
    barang = []
    tiket = []
    total_tiket = 0
    print("""============ Daftar Barang ============
    1. Mac Book Pro 16" = 10 tiket
    2. Iphone 13 Pro    = 7 tiket
    3. Ipad Pro         = 5 tiket
    4. Apple Watch S7   = 3 tiket
    5. Airtag           = 2 tiket""")
    garis()
    while True:
        nama_barang = input("    Silahkan pilih barang: ")
        if nama_barang.isdigit():
            nama_barang = int(nama_barang)
        else:
            print("Input tidak valid !")
        if nama_barang == 1:
            barang.append('Mac Book Pro 16" ')
            tiket.append(10)
            total_tiket += 10
        elif nama_barang == 2:
            barang.append('Iphone 13 Pro    ')
            tiket.append(7)
            total_tiket += 7
        elif nama_barang == 3:
            barang.append('Ipad Pro         ')
            tiket.append(5)
            total_tiket += 5
        elif nama_barang == 4:
            barang.append('Apple Watch S7   ')
            tiket.append(3)
            total_tiket += 3
        elif nama_barang == 5:
            barang.append('Airtag           ')
            tiket.append(2)
            total_tiket += 2
        while True:
            lanjut = input("Lanjut tukar hadiah ? (Y/T): ").lower()
            if lanjut.isdigit():
                print("Input tidak valid !")
            elif lanjut == 'y':
                break
            else:
                while True:
                    garis()
                    for i,j in zip(barang,tiket):
                        print(i,':',j,'Tiket')
                    garis()
                    print("Total             :",total_tiket,'Tiket')
                    user_tiket = input("""Tekan Q untuk keluar atau
Masukkan tiket anda: """)
                    if user_tiket.isdigit():
                        user_tiket = int(user_tiket)
                        if user_tiket < total_tiket:
                            print(f"Tiket kurang !")
                        else:
                            garis()
                            print("Selamat, hadiah yang kamu dapat :")
                            for k in barang:
                                print(k)
                            garis()
                            while True:
                                keluar = input("Tekan Q untuk keluar: ").lower()
                                if keluar == "q":
                                    daftar_menu()
                                else:
                                    print("Input tidak valid !")
                    elif user_tiket.lower() == "q":
                        daftar_menu()
                    elif user_tiket.lower() != "q":
                        print("Input tidak valid !")
                    else:
                        print("Input tidak valid !")
def keluar():
    print("""Terimakasih sudah bermain di TIMEZONE.
Silahkan datang kembali.""")
    quit()
daftar_menu()