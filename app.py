# MENGIMPOR MODUL
import getpass
import os
from datetime import datetime
from functions import welcome, siubsielibrary, jeda, detailbuku, KembalikanBuku, daftarbuku, pinjambuku

# ====== FUNGSI MENU ======
def MenuPertama():
    jeda(1)
    siubsielibrary(60, "Pendaftaran Akun pada layanan SIUBSI E-library")
    print("\nBerikut syarat-syarat yang perlu diperhatikan sebelum anda mendaftarkan akun pada Layanan 'SIUBSI E-library'")
    print("""
[-] Data yang dimasukkan tidak boleh ada yang kosong.
[-] Tidak boleh mengandung karakter ',' dalam pengisian data.
[-] Maksimum karakter adalah sebagai berikut: Nama (20), Username (15), Password (30).""")
    print("\n\n[Pesan] Masukkan Username dan Password untuk akun anda.")
    Name = input("Masukkan nama anda: ")
    Username = input("Masukkan Username: ")
    Password = getpass.getpass("Masukkan Password: ")
    print("\nMohon tunggu sebentar...")
    jeda(1)
    registerUser(Name, Username, Password)

def MenuKedua():
    jeda(1)
    siubsielibrary(60, '"Prosesi masuk dengan menginput'.center(60) + '\n' + '\'Username & Password\' pada layanan SIUBSI E-Library"')
    print("\n[Pesan] Masukkan Username dan Password akun anda dengan benar.")
    Username = input("Masukkan Username anda: ")
    Password = getpass.getpass("Masukkan Password anda: ")
    masuk(Username, Password)

def MenuKetiga():
    jeda(1)
    os.system("cls")

    siubsielibrary(60, "Daftar Buku yang sedang dipinjam\n")
    if os.stat("Data/peminjaman.txt").st_size == 0:
        return print("Tidak ada buku yang sedang dipinjam saat ini.")

    Name = input("Masukkan nama anda: ")
    Kodebuku = ""
    Judulbuku = ""
    file = open("Data/peminjaman.txt", "r")

    print("="*125)
    print(f"{'Nama peminjam':<20}\tKode Buku\t{'Waktu pinjam':<18}\tJudul Buku")
    print("-"*125)
    for line in file:
        if Name in line:
            a, b, c, d = line.split("#")
            a == Name
            b == Kodebuku
            c == Judulbuku
            dt = datetime.fromtimestamp(float(d)).strftime("%d-%m-%y %H:%M:%S")
            print(f"{a:<20}\t{b:<10}\t{dt:<18}\t{c}")
    else:
        print(f"Nama {Name} tidak ditemukan")
    print("="*125)
    file.close()

    print("\n[1]. Lihat detail buku\n[2]. Exit")
    Pilihan = input("Pilih menu [1|2]: ")
    if Pilihan == "1":
        Kodebukunya = input("Masukkan kode buku untuk ditampilkan detailnya: ")
        detailbuku(Kodebukunya)
    elif Pilihan == "2":
        exit()
    else:
        print(f"Pilihan {Pilihan} tidak ditemukan.")

def MenuKeempat():
    Name = input("Masukkan nama lengkap anda: ")
    Kodebuku = input("Masukkan Kodebuku yang ingin dikembalikan: ")
    KembalikanBuku(Name, Kodebuku)

# ====== FUNGSI USER REGISTER ======
def inputUser(Name, Username, Password):
    file = open("Data/users.txt", "a")
    file.write(f"{Name},{Username},{Password}\n")
    file.close()

def registerUser(Name, Username, Password):
    file = open("Data/users.txt", "r")
    if os.stat("Data/users.txt").st_size != 0:
        for i in file:
            a, b, c = i.split(",")
            pass

        if Username == b:
            print("Username tidak tersedia, silahkan pilih yang lain.")
            jeda(2)
            mulai()
            akses(opsi)

    if Name is "" or Username is "" or Password is "":
        print("Pendaftaran akun gagal, data yang dimasukkan tidak boleh ada yang kosong.")
        jeda(2)
        mulai()
        akses(opsi)
    elif "," in Name or "," in Username or "," in Password:
        print("Pendaftaran akun gagal, tidak boleh mengandung ',' dalam pengisian data.")
        jeda(2)
        mulai()
        akses(opsi)
    elif len(Name) > 20 or len(Username) > 15 or len(Password) > 30:
        print("Pendaftaran akun gagal, data yang dimasukkan ada yang telah melibihi batas maksimum karakter.")
        jeda(2)
        mulai()
        akses(opsi)
    else:
        inputUser(Name, Username, Password)
        print(f"[Pesan] Berhasil membuat akun.")
        jeda(1)
        siubsielibrary(60, "Proses masuk pada layanan SIUBSI E-library")
        print(f"\n[Pesan] Selamat datang {Name}.\n")

        Uname = input("Masukkan Username anda: ")
        PW = getpass.getpass("Masukkan Password anda: ")
        if Uname == Username and PW == Password:
            masuk(Username, Password)
        else:
            print("Data yang anda masukkan tidak sesuai, silahkan masuk ulang!")
            jeda(2)
            mulai()
            akses(opsi)

# ====== FUNGSI USER AKSES ======
def akses(opsi):
    global Username
    global Name
    if opsi == "1":
        MenuPertama()
    elif opsi == "2":
        MenuKedua()
    elif opsi == "3":
        MenuKetiga()
    elif opsi == "4":
        MenuKeempat()
    else:
        print(f"Menu {opsi} tidak diketahui.")

# ====== FUNGSI USER LOGIN ======
def masuk(Username, Password):
    Sukses = False
    file = open("Data/users.txt", "r")
    for i in file:
        a, b, c = i.split(",")
        c = c.strip()

        if b == Username and c == Password:
            Sukses = True
            break
    file.close()
    if (Sukses):
        print("\n[Pesan] Mengidentifikasi akun...")
        jeda(1)
        print("[Pesan] Berhasil masuk.")
        os.system("cls")
        daftarbuku(1)
        while True:
            Halaman = input(
                "\nPilih nomor untuk dialihkan ke halaman nomor tersebut, Masukkan 'menu' agar dialihkan ke Menu buku, Masukkan 'exit' untuk keluar dari program.\n[1|2|menu]: ")
            if Halaman == "1":
                os.system("cls")
                daftarbuku(1)
            elif Halaman == "2":
                os.system("cls")
                daftarbuku(2)
            elif Halaman == "menu":
                print("\n"+"="*30 +
                      "\n[1]. Pinjam buku\n[2]. Lihat detail buku\n[3]. Exit")
                RedirectMenuBuku = input("Masukkan pilihan [1|2|3]: ")

                if RedirectMenuBuku == "1":
                    Kodebuku = input("Masukkan kode buku: ")
                    pinjambuku(a, Kodebuku)
                elif RedirectMenuBuku == "2":
                    Pilihan = input(
                        "\nMasukkan Kode Buku ('exit' untuk keluar program): ")
                    if Pilihan == "exit":
                        print("keluar program...")
                        jeda(2)
                        exit()
                    else:
                        detailbuku(Pilihan)
                elif RedirectMenuBuku == "3":
                    exit()
                else:
                    print(f"Pilihan {RedirectMenuBuku} tidak ditemukan")
            elif Halaman == "exit":
                jeda(1)
                exit()
            else:
                print("Nomor Halaman tidak tersedia.")

    else:
        print(f"\nGagal masuk, Periksa kembali data yang anda masukkan, apakah tersedia atau tidak.")
        jeda(3)
        mulai()
        akses(opsi)

# ====== FUNGSI MEMULAI PROGRAM ======
def mulai():
    global opsi
    welcome()
    print("[1] Daftar (Silahkan pilih menu ini jika anda belum mempunyai akun)")
    print("[2] Masuk (Silahkan pilih menu ini jika anda sudah mempunyai akun)")
    print("[3] Tampilkan Buku yang sedang dipinjam")
    print("[4] Kembalikan buku")
    opsi = input("Masukkan pilihan [1|2|3|4]: ")
    if opsi != "1" and opsi != "2" and opsi != "3" and opsi != "4":
        mulai()

# ====== MEMANGGIL FUNGSI MEMULAI PROGRAM BESERTA AKSES-NYA ======
mulai()
akses(opsi)
