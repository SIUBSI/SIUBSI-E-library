import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name

    while (True):
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
        
        print("Selamat datang di SIUBSI E-library")
        print("Database Perpustakaan")
        print("==================================")

        print(f"[1]. Tampilkan data")
        print(f"[2]. Buat data")
        print(f"[3]. Ubah data")
        print(f"[4]. Hapus data\n")

        OpsiUser = input("Masukan Opsi: ")

        print("\n==================================\n")

        match OpsiUser:
            case "1": print("Tampilkan data")
            case "2": print("Buat data")
            case "3": print("Ubah data")
            case "4": print("Hapus data")

        print("\n==================================\n")

        isDone = input("Apakah selesai? [y|n]: ")
        if isDone == "y" or isDone == "Y":
            break

    print("\nAnda telah keluar dari layanan SIUBSI E-library, Terimakasih atas waktu-nya :D")
