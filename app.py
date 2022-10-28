# MENGIMPORT MODUL
import getpass, time, os
from datetime import datetime

# LIST BERISI DAFTAR BUKU BESERTA DETAILNYA
DaftarBuku = [
    # Page 1
    ["Pengantar teori dan algoritma graph", "220868",
        "Suryadi", "1990", "Indonesia", "Gunadarma"],
    ["English conversations plus", "210646", "Sonny pradana",
        "2010", "Indonesia-Ingrris", "Setia Kawan Press"],
    ["Linux untuk pratikum administrasi jaringan", "210606",
        "Budi Susanto", "2003", "Indonesia", "Gava Media"],
    ["Administrasi jaringan komputer lintas platform", "210481",
        "Ridwan Sanjaya, Paulus Ricky Kusuma dan Bastian Rae Lukito", "2005", "Indonesia", "PT Elex Media Komputindo"],
    ["Membangun jaringan komputer praktis sehari - hari", "210514",
        "Iwan Binanto", "2007", "Indonesia", "Graha Ilmu"],
    ["Administrasi jaringan menggunakan linux ubuntu 7", "208403",
        "Dewi Prabantini (Ed)", "2008", "Indonesia", "ANDI"],
    ["Statistika dengan program komputer", "208445",
        "Ahmad Kholiqul Amin", "2015", "Indonesia", "Deepublish"],
    ["Penyuntingan bahasa indonesia untuk karang-mengarang",
        "210157", "Kunjana Rahardi", "2009", "Indonesia", "Erlangga"],
    ["Robotika : desain, kontrol, dan kecerdasan buatan",
        "210119", "Endra Pitowarno", "2006", "Indonesia", "ANDI"],
    ["Struktur data dan pemrograman dengan pascal", "208144",
        "Heri Sismoro dan Kusrini Ikandar", "2004", "Indonesia", "ANDI"],

    # Page 2
    ["Logika dan algoritma dasar menggunakan bahasa C++", "210646",
        "Indarwoko Kurniadi", "2013", "Indonesia", "Mitra Wacana Media"],
    ["Konsep kecerdasan buatan", "210646",
        "Anita Desiani dan Muhammad Arhami", "2006", "Indonesia", "ANDI"],
    ["Dasar - dasar pemrograman pascal", "210646",
        "Abdul Kadir", "2007", "Indonesia", "ANDI"],
    ["Menguasai presentasi dengan microsoft powerpoint xp", "210646",
        "Triton Prawiro Budi", "2005", "Indonesia", "Tugu Publisher"],
    ["36 jam belajar komputer microsoft office powerpoint 2003", "210646",
        "Budi Permana", "2005", "Indonesia", "PT Elex Media Komputindo"],
    ["Troubleshooting windows xp : konsultasi dengan ahlinya", "210646",
        "Jubilee Enterprise", "2008", "Indonesia", "PT Elex Media Komputindo"],
    ["Microsoft windows me : sistem operasi masa depan", "210646",
        "Wali Eko Djatmiko", "2001", "Indonesia", "ANDI"],
    ["CISCO CCNA jaringan komputer", "210646",
        "Iwan Sofana", "2010", "Indonesia", "INFORMATIKA"],
    ["Kamus andal microsoft excel 2000", "210646",
        "Rijanto Tosin", "2000", "bahasa", "Dinastindo"],
    ["Teknik komputer jaringan (sistem operasi dan jaringan)", "210646",
     "Muhammad Badrul dkk", "2010", "Indonesia", "Inti Prima"],
]

# ====== FUNGSI WELCOME MESSAGE ======
def welcome():
    os.system("cls")
    print("\n"+'"SIUBSI E-library"'.center(60))
    print('"Menyediakan Book maupun E-book dikhususkan untuk Prodi\nSistem Informasi pada Universitas Bina Sarana Informatika"\n\n')

# ====== FUNGSI JEDA ======
def jeda(durasijeda): # dengan parameter jumlah durasi jeda-nya
    time.sleep(durasijeda) # eksekusi perintah jeda
    os.system("cls") # Clear screen menggunakan modul os

# ====== FUNGSI BUKU ======
def daftarbuku(pagenum):
    if pagenum == 1:
        pagenum = DaftarBuku[0:10] # Menampilkan daftar buku dari 1 s/d 10
        print("\n[Halaman: 1/2]\n") # Status Halaman
        print("No.\tKode Buku\tJudul Buku")
        print("---\t---------\t----------------------------------------------------------")
    elif pagenum == 2:
        pagenum = DaftarBuku[10:20]  # Menampilkan daftar buku dari 10 s/d 20
        print("\n[Halaman: 2/2]\n") # Status Halaman
        print("No.\tKode Buku\tJudul Buku")
        print("---\t---------\t----------------------------------------------------------")

    # Menampilkan List buku sesuai halaman (menggunakan for loop)
    num = 0 # Sebagai nomor
    for i in pagenum:
        num += 1
        print(f"{num}.\t{i[1]}\t\t{i[0]}")

def tambahpinjambuku(Name, judulbuku, timestamp):
    file = open("Data/peminjaman.txt", "r")
    if os.stat("Data/peminjaman.txt").st_size == 0:
        file = open("Data/peminjaman.txt", "a")
        file.write(f"{Name}#{judulbuku}#{timestamp}")
        file.close()
    else:
        file = open("Data/peminjaman.txt", "a")
        file.write(f"\n{Name}#{judulbuku}#{timestamp}")
        file.close()

def pinjambuku(Name, Kodebuku):
    Name = Name
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    for i in DaftarBuku[0:20]:
        if Kodebuku in i[1]:
            os.system("cls")
            print('"SIUBSI E-library"'.center(60))
            print(f"Meminjam buku dengan kode buku `{Kodebuku}`".center(60))
            print("Data Peminjam:".center(60))
            print(f"Nama: {Name}\nBuku yang dipinjam: {i[0]} ({i[1]})\nWaktu: {dt}")
            tambahpinjambuku(Name, i[0], ts)
            break
        else:
            print(f"Kode buku `{Kodebuku}` tidak ditemukan.")
            break
    else:
        pass

# Fungsi ini akan menampilkan detail buku sesuai dengan kode buku yang dipilih
def detailbuku(kodebuku):
    for i in DaftarBuku[0:20]: # Mengambil data buku dari 1 s/d 20
        if kodebuku in i[1]: # [1] guna untuk mengambil kode buku tiap list
            jeda(1)
            print('"SIUBSI E-library"'.center(60))
            print(f"Menampilkan detail Buku dengan kode buku `{kodebuku}`".center(60))
            return print(f"""
            Kode Buku: {i[1]}
            Judul Buku: {i[0]}
            Penulis: {i[2]}
            Tahun: {i[3]}
            Bahasa: {i[4]}
            Penerbit: {i[5]}
            Link: https://elibrary.bsi.ac.id/readbook/{i[1]}/{i[0].replace(" ", "-")}
            """, end="")
        else:
            pass
    else:
        print(f"Kode buku `{kodebuku}` tidak ditemukan.")

# ====== FUNGSI USER LOGIN ======
def masuk(Username, Password):
    Sukses = False
    file = open("Data/users.txt", "r")
    for i in file:
        a, b, c = i.split(", ")
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
                daftarbuku(1)
            elif Halaman == "2":
                daftarbuku(2)
            elif Halaman == "menu":
                print("-"*30)
                print("\n[1]. Pinjam buku\n[2]. Lihat detail buku")
                RedirectMenuBuku = input("Masukkan pilihan [1|2]: ")

                if RedirectMenuBuku == "1":
                    Kodebuku = input("Masukkan kode buku: ")
                    pinjambuku(a, Kodebuku)
                elif RedirectMenuBuku == "2":
                    kodenya = input("\nMasukkan Kode Buku ('exit' untuk keluar program): ")
                    if kodenya == "exit":
                        print("keluar program...")
                        jeda(2)
                        exit()
                    else:
                        detailbuku(kodenya)
                else:
                    print(f"Pilihan {RedirectMenuBuku} tidak ditemukan")
            elif Halaman == "exit":
                jeda(1)
                exit()
            else:
                print("Nomor Halaman tidak tersedia.")

    else:
        print(f"\nAkun dengan username '{Username}' tidak terdaftar, silahkan daftar terlebih dahulu!")
        jeda(3)
        mulai()
        akses(opsi)

# ====== FUNGSI USER REGISTER ======
def daftar(Name, Username, Password):
    file = open("Data/users.txt", "r")
    if os.stat("Data/users.txt").st_size == 0:
        file = open("Data/users.txt", "a")
        file.write(f"{Name}, {Username}, {Password}")
    else:
        file = open("Data/users.txt", "a")
        file.write(f"\n{Name}, {Username}, {Password}")

# ====== FUNGSI USER AKSES ======
def akses(opsi):
    global Username
    global Name
    if opsi == "1":
        jeda(1)
        print("Pendaftaran akun pada program".center(60))
        print('"SIUBSI E-library"'.center(60))
        print("\n[Pesan] Masukkan Username dan Password untuk akun anda.")
        Name = input("Masukkan nama lengkap: ")
        Username = input("Masukkan Username: ")
        Password = getpass.getpass("Masukkan Password: ")
        print("\nMohon tunggu sebentar...")
        jeda(1)
        if Name == "" and Username == "" and Password == "":
            print("Pendaftaran akun gagal, data yang dimasukkan tidak boleh kosong.")
            jeda(2)
            mulai()
            akses(opsi)
        elif "," in Name or "," in Username or "," in Password:
            print("Pendaftaran akun gagal, tidak boleh mengandung ',' dalam pengisian data.")
            jeda(2)
            mulai()
            akses(opsi)
        else:
            daftar(Name, Username, Password)
            print(f"[Pesan] Berhasil membuat akun.")
            jeda(1)
            print("Pendaftaran akun pada program".center(60))
            print('"SIUBSI E-library"'.center(60))
            print(f"\n[Pesan] Selamat datang {Name}.\n")

            Username = input("Masukkan Username anda: ")
            Password = getpass.getpass("Masukkan Password anda: ")
            masuk(Username, Password)
    elif opsi == "2":
        jeda(1)
        print("Prosesi masuk pada program".center(60))
        print('"SIUBSI E-library"'.center(60))
        print("\n[Pesan] Masukkan Username dan Password akun anda dengan benar.")
        Username = input("Masukkan Username anda: ")
        Password = getpass.getpass("Masukkan Password anda: ")
        masuk(Username, Password)
    elif opsi == "3":
        jeda(1)
        os.system("cls")
        file = open("Data/users.txt", "r")

        print("Daftar User terdaftar pada program".center(60))
        print('"SIUBSI E-library"'.center(60)+"\n")
        Name = ""
        Username = ""
        Password = ""
        num = 0
        for i in file:
            num += 1
            a, b, c = i.split(", ")
            a == Name
            b == Username
            c == Password
            print(f"{num}. {a} ({b})")
    elif opsi == "4":
        jeda(1)
        os.system("cls")
        file = open("Data/peminjaman.txt", "r")

        print("Daftar Buku yang sedang dipinjam pada program".center(60))
        print('"SIUBSI E-library"'.center(60)+"\n")
        Name = ""
        Kodebuku = ""
        num = 0
        for i in file:
            num += 1
            a, b, c = i.split("#")
            a == Name
            b == Kodebuku
            dt = datetime.fromtimestamp(float(c))
            print(f"{num}. {a} ({b}) | Waktu pinjam: {dt}")

    else:
        print(f"Menu {opsi} tidak diketahui.")

# ====== FUNGSI MEMULAI PROGRAM ======
def mulai():
    global opsi
    welcome()
    print("[1] Daftar (Silahkan pilih menu ini jika anda belum mempunyai akun)")
    print("[2] Masuk (Silahkan pilih menu ini jika anda sudah mempunyai akun)")
    print("[3] Tampilkan User terdaftar")
    print("[4] Tampilkan Buku yang sedang dipinjam")
    opsi = input("Masukkan pilihan [1|2]: ")
    if opsi != "1" and opsi != "2" and opsi != "3" and opsi != "4":
        mulai()


# ====== MEMANGGIL FUNGSI MEMULAI PROGRAM BESERTA AKSES-NYA ======
mulai()
akses(opsi)
