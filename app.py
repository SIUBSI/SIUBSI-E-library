from ast import Pass
import pickle, getpass, time

class User:
    TotalPCaktif = ["PC-1", "PC-2", "PC-3", "PC-4", "PC-5"]

    def __init__(self, name, password, PC):
        self.name = name
        self.password = password
        self.PC = PC
        User.TotalPCaktif.remove(PC)

        
print("- Selamat datang di Warnet SI -".center(60))
print("\t\t   Silahkan memilih Menu")
print("1. Daftar\n2. Masuk")
PilihMenu = int(input("Masukkan menu [1|2]: "))

if PilihMenu == 1:
    Uname = str(input("Masukkan nama anda: "))
    PW = getpass.getpass()

    pickle.dump(Uname, open("Data/username.dat", "wb"))
    pickle.dump(PW, open("Data/password.dat", "wb"))

    print("[Pesan] Menyimpan data...")
    time.sleep(3)
    print("[Pesan] Data berhasil tersimpan!")
elif PilihMenu == 2:
    Usernamenya = pickle.load(open("Data/username.dat", "rb"))
    Pwnya = pickle.load(open("Data/password.dat", "rb"))

    Uname = str(input("Masukkan nama anda: "))
    PW = getpass.getpass("Masukkan Password: ")

    if Uname == Usernamenya and PW == Pwnya:
        # print("- Selamat datang di Warnet SI -".center(60))
        # print("\t\t   Silahkan memilih Menu")
        print("\n[Pesan] Memeriksa data...")
        time.sleep(3)
        print("[Pesan] Data ditemukan!")
        time.sleep(1)
        print("\n" + f"Halo, {Uname}!")
    else:
        print("\n[Pesan] Memeriksa data...")
        time.sleep(3)
        print("[Pesan] Data tidak dikenal")

    # NomorPC = str(input("Masukkan nomor PC: "))
else:
    print(f"Menu {PilihMenu} tidak ditemukan")



# if NomorPC == "1":
#     PC = "PC-1"
# elif NomorPC == "2":
#     PC = "PC-2"
# elif NomorPC == "2":
#     PC = "PC-2"
# elif NomorPC == "3":
#     PC = "PC-3"
# elif NomorPC == "4":
#     PC = "PC-4"
# else:
#     NomorPC == "-"


# Daffy = User(Uname, PW, PC)

# if Daffy.name == Uname and Daffy.password == PW:
#     print("Login Berhasil")
# else:
#     print("Login gagal\n")

# for i in User.TotalPCaktif:
#     print(str(i), end=", ")

# Daffy = User("Daffy", "dapi", "2")
# print(User.TotalPCaktif)

# Uname = str(input("Masukkan username: "))
# pw = getpass.getpass()

# # Save Password
# pickle.dump(pw, open("pw.dat", "wb"))

# # Load Password
# pwnya = pickle.load(open("pw.dat", "rb"))

# if pw == pwnya:
#     print("Login berhasil")
# else:
#     print("Login tidak berhasil")