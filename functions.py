import time
import os
from datetime import datetime

# ====== LIST BERISI DAFTAR BUKU BESERTA DETAILNYA ======
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