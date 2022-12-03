import getpass
import os
from datetime import datetime
from functions import welcome, siubsielibrary, jeda, lihatstokbuku, detailbuku


# ============= FUNGSI MENU =============
def MenuPertama():
    jeda(1)
    os.system("cls")
    file = open("Data/users.txt", "r")

    siubsielibrary(60, "\"Daftar User terdaftar pada layanan SIUBSI E-library\"\n")
    if os.stat("Data/users.txt").st_size == 0:
        print("\n[Pesan] Tidak ada user yang terdaftar saat ini.")

    Name = ""
    Username = ""
    Password = ""
    print("="*40)
    print(f"No.\t{'Nama':20}\t{'Username':15}")
    print("-"*40)
    for i, v in enumerate(file, start=1):
        a, b, c = v.split(",")
        a == Name
        b == Username
        c == Password
        print(f"{i}.\t{a:<20}\t{b:<15}")
    print("="*40)

def MenuKedua():
    jeda(1)
    os.system("cls")
    file = open("Data/peminjaman.txt", "r")

    siubsielibrary(60, "Daftar Buku yang sedang dipinjam\n")
    if os.stat("Data/peminjaman.txt").st_size == 0:
        return print("Tidak ada buku yang sedang dipinjam saat ini.")

    Name = ""
    Kodebuku = ""
    Judulbuku = ""
    print("="*125)
    print(f"No.\t{'Nama peminjam':<20}\tKode Buku\t{'Waktu pinjam':<18}\tJudul Buku")
    print("-"*125)
    for i, v in enumerate(file, start=1):
        a, b, c, d = v.split("#")
        a == Name
        b == Kodebuku
        c == Judulbuku
        dt = datetime.fromtimestamp(float(d)).strftime("%d-%m-%y %H:%M:%S")
        print(f"{i}.\t{a:<20}\t{b:<10}\t{dt:<18}\t{c}")
    print("="*125)

    print("\n[1]. Lihat detail buku\n[2]. Exit")
    Pilihan = input("Pilih menu [1|2]: ")
    if Pilihan == "1":
        Kodebukunya = input("Masukkan kode buku untuk ditampilkan detailnya: ")
        detailbuku(Kodebukunya)
    elif Pilihan == "2":
        exit()
    else:
        print(f"Pilihan {Pilihan} tidak ditemukan.")

def MenuKetiga():
    print("\n")
    lihatstokbuku()

def login():
    os.system("cls")
    siubsielibrary(60, "\"Masuk sebagai Admin pada layanan SIUBSI E-library\"\n")
    Username = input("Massukan Username: ")
    Password = getpass.getpass("Massukan Password: ")

    if Username == "admin" and Password == "admin":
        welcome()
        print("[1] Tampilkan User terdaftar")
        print("[2] Tampilkan Buku yang sedang dipinjam")
        print("[3] Tampilkan Stok Buku keseluruhan")
        menu = input("Masukkan pilihan [1|2|3|4]: ")
        if menu == "1":
            MenuPertama()
        elif menu == "2":
            MenuKedua()
        elif menu == "3":
            MenuKetiga()
        else:
            print(f"Menu {menu} tidak ditemukan.")

    else:
        print("Identitas tidak diketahui.")

login()