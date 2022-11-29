# MENGIMPOR MODUL
import getpass
import time
import os
from datetime import datetime

# LIST BERISI DAFTAR BUKU BESERTA DETAILNYA
DaftarBuku = [
    # Page 1
    ["Pengantar teori dan algoritma graph", "220868","Suryadi", "1990", "Indonesia", "Gunadarma"],
    ["English conversations plus", "210646", "Sonny pradana","2010", "Indonesia-Ingrris", "Setia Kawan Press"],
    ["Linux untuk pratikum administrasi jaringan", "210606","Budi Susanto", "2003", "Indonesia", "Gava Media"],
    ["Administrasi jaringan komputer lintas platform", "210481","Ridwan Sanjaya, Paulus Ricky Kusuma dan Bastian Rae Lukito", "2005", "Indonesia", "PT Elex Media Komputindo"],
    ["Membangun jaringan komputer praktis sehari - hari", "210514","Iwan Binanto", "2007", "Indonesia", "Graha Ilmu"],

    # Page 2
    ["Administrasi jaringan menggunakan linux ubuntu 7", "208403","Dewi Prabantini (Ed)", "2008", "Indonesia", "ANDI"],
    ["Statistika dengan program komputer", "208445","Ahmad Kholiqul Amin", "2015", "Indonesia", "Deepublish"],
    ["Penyuntingan bahasa indonesia untuk karang-mengarang","210157", "Kunjana Rahardi", "2009", "Indonesia", "Erlangga"],
    ["Robotika : desain, kontrol, dan kecerdasan buatan","210119", "Endra Pitowarno", "2006", "Indonesia", "ANDI"],
    ["Struktur data dan pemrograman dengan pascal", "208144","Heri Sismoro dan Kusrini Ikandar", "2004", "Indonesia", "ANDI"],
]

# ====== FUNGSI UMUM ======
def welcome():
    os.system("cls")
    siubsielibrary(60, "Layanan peminjaman Buku yang dikhususkan untuk Mahasiswa/i ber-Program Studi" + "\n" + "\'Sistem Informasi\' pada \'Universitas Bina Sarana Informatika\'")
    print("\n")

def siubsielibrary(centernum, text):
    print("--------------------".center(centernum))
    print("| SIUBSI E-library |".center(centernum))
    print("--------------------".center(centernum))
    print(text.center(centernum))

def jeda(durasijeda):  # dengan parameter jumlah durasi jeda-nya
    time.sleep(durasijeda)  # eksekusi perintah jeda
    os.system("cls")  # Clear screen menggunakan modul os

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
    file = open("Data/users.txt", "r")

    siubsielibrary(60, "\"Daftar User terdaftar pada layanan SIUBSI E-library\"\n")
    if os.stat("Data/users.txt").st_size == 0:
        print("\n[Pesan] Tidak ada user yang terdaftar saat ini.\n\n[1]. Buat akun\n[2]. Exit")
        while True:
            menu = input("Pilih menu [1|2]: ")
            if menu == "1":
                jeda(1)
                siubsielibrary(60, "Pendaftaran Akun pada layanan SIUBSI E-library.")
                print("\n[Pesan] Masukkan Username dan Password untuk akun anda.")
                Name = input("Masukkan nama lengkap: ")
                Username = input("Masukkan Username: ")
                Password = getpass.getpass("Masukkan Password: ")
                print("\nMohon tunggu sebentar...")
                jeda(1)
                registerUser(Name, Username, Password)
            elif menu == "2":
                exit()
            else:
                print("Menu tidak ditemukan.\n")
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

def MenuKeempat():
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

def MenuKelima():
    print("\n")
    lihatstokbuku()

def MenuKeenam():
    Name = input("Masukkan nama lengkap anda: ")
    Kodebuku = input("Masukkan Kodebuku yang ingin dikembalikan: ")
    KembalikanBuku(Name, Kodebuku)

# ====== FUNGSI PENGOPERASIAN BUKU ======
def daftarbuku(pagenum):
    if pagenum == 1:
        pagenum = DaftarBuku[:5]  # Menampilkan daftar buku dari 1 s/d 10
        print("\n-> Halaman: 1/2")  # Status Halaman
        print("="*80)
        print(f"No.\tKode Buku\tJudul Buku")
        print("="*80)

    elif pagenum == 2:
        pagenum = DaftarBuku[5:]  # Menampilkan daftar buku dari 10 s/d 20
        print("\n-> Halaman: 2/2")  # Status Halaman
        print("="*80)
        print(f"No.\tKode Buku\tJudul Buku")
        print("="*80)

    # Menampilkan List buku sesuai halaman (menggunakan for loop)
    for i, v in enumerate(pagenum, start=1):
        print(f"{i}.\t{v[1]}\t\t{v[0]}")

    print("="*80)

# Kode ini akan menambahkan objek ke index belakang kedalam file peminjaman.txt
def tambahpinjambuku(Name, kodebuku, judulbuku, timestamp):
    # Permission 'a' disini adalah sebagai append, atau berfungsi untuk menambahkan item dari baris bawah/akhir.
    file = open("Data/peminjaman.txt", "a")
    file.write(f"{Name}#{kodebuku}#{judulbuku}#{timestamp}\n")
    file.close()

# Memunculkan daftar stok buku secara keseluruhan
def lihatstokbuku():
    file = open("Data/stokbuku.txt", "r")
    for i, v in enumerate(file, start=1):
        # '.split("#")', untuk memisahkan kata dengan menggunakan pemisah #
        a, b, c = v.split("#")
        c = int(c)
        # 'end' memaksa menggantikan newline dengan nonkarakter
        if c == 0:
            print(f"{i}. {a} ({b}) - Stok: Tidak tersedia", end="\n")
        else:
            print(f"{i}. {a} ({b}) - Stok: {c}", end="\n")

# Memunculkan stok buku by Kode Buku
def jumlahstok(Kodebuku):
    with open("Data/stokbuku.txt", 'r') as fp:
        for l_no, line in enumerate(fp):
            if Kodebuku in line:
                l_no += 1
                a, b, c = line.split("#")
                c = int(c)
                if c == 0:
                    return 'Tidak tersedia'
                else:
                    return c

# Fungsi mengurangkan stok buku ketika buku dipinjam
def kuranginstokbuku(Kodebuku):
    file = open("Data/stokbuku.txt", "r")
    for i in file:
        a, b, c = i.split("#")
        b == Kodebuku
        c = int(c)

        with open("Data/stokbuku.txt", "r") as files:
            filedata = files.read()
            if Kodebuku in filedata:
                jumlah = c-1
                filedata = filedata.replace(
                    f"{a}#{Kodebuku}#{c}", f"{a}#{Kodebuku}#{jumlah}")

                with open("Data/stokbuku.txt", "w") as files:
                    files.write(filedata)
                files.close()
            else:
                print(f"Kode buku {Kodebuku} tidak ditemukan.")

# Fungsi konfirmasi Peminjaman buku
def pinjambuku(Name, Kodebuku):
    Name = Name
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    for i in DaftarBuku[0:20]:
        if Kodebuku in i[1]:
            jeda(1)
            os.system("cls")
            siubsielibrary(60, f"Meminjam buku dengan kode buku `{Kodebuku}`")
            print(f"-------------------------------------------".center(60))
            if jumlahstok(Kodebuku) is not 0 or jumlahstok(Kodebuku) > 0:
                print("\n----- Data Peminjam -----")
                tambahpinjambuku(Name, i[1], i[0], ts)
                kuranginstokbuku(Kodebuku)
                print(
                    f"Nama: {Name}\nBuku yang dipinjam: {i[0]} ({i[1]})\nWaktu: {dt}\nSisa stok buku: {jumlahstok(Kodebuku)}")
            else:
                print(
                    f"\nProses peminjaman buku gagal, Stok buku dengan judul `{i[0]}` tidak tersedia!")
            break
        else:
            pass
    else:
        print(f"Kode buku `{Kodebuku}` tidak ditemukan.")

# Fungsi ini akan menampilkan detail buku by Kode Buku tsb
def detailbuku(kodebuku):
    for i in DaftarBuku[0:20]:  # Mengambil data buku dari 1 s/d 20
        if kodebuku in i[1]:  # [1] guna untuk mengambil kode buku tiap konten pada list
            jeda(1)
            siubsielibrary(
                60, f"Menampilkan detail Buku dengan kode buku `{kodebuku}`")
            print("------------------------------------------------------".center(60))
            return print(f"Kode Buku: {i[1]}\nJudul Buku: {i[0]}\nPenulis: {i[2]}\nTahun: {i[3]}\nBahasa: {i[4]}\nPenerbit: {i[5]}\nJumlah Stok: {jumlahstok(kodebuku)}\nLink: https://elibrary.bsi.ac.id/readbook/{i[1]}/{i[0].replace(' ', '-')}")
        else:
            pass
    else:
        print(f"Kode buku `{kodebuku}` tidak ditemukan.")

# Proses pengolahan pada peminjaman.txt untuk fungsu pengembalian buku
def KembalikanBuku(Name, Kodebuku):
    file = open("Data/peminjaman.txt", "r")
    for i in file:
        a, b, c, d = i.split("#")
        a == Name
        b == Kodebuku

        with open("Data/peminjaman.txt", "r", encoding='utf-8') as files:
            filedata = files.read()
            if f"{Name}#{Kodebuku}#{c}#{d}" in filedata:

                filedata = filedata.replace(f"{Name}#{Kodebuku}#{c}#{d}", "")

                with open("Data/peminjaman.txt", "w") as files:
                    files.write(filedata)
                
    
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
    elif opsi == "5":
        MenuKelima()
    elif opsi == "6":
        MenuKeenam()
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
    print("[5] Tampilkan Stok Buku keseluruhan")
    print("[6] Kembalikan buku")
    opsi = input("Masukkan pilihan [1|2|3|4|5|6]: ")
    if opsi != "1" and opsi != "2" and opsi != "3" and opsi != "4" and opsi != "5" and opsi != "6":
        mulai()


# ====== MEMANGGIL FUNGSI MEMULAI PROGRAM BESERTA AKSES-NYA ======
mulai()
akses(opsi)
