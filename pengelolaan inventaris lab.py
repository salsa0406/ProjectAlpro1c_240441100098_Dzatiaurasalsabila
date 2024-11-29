admin = (
    ("sarifah", "hasana"),
    ("salsa", "123456")
)

barang = {
    1: {"nama": "Monitor", "jumlah": 20, "kategori": "Elektronik"},
    2: {"nama": "Keyboard", "jumlah": 50, "kategori": "Elektronik"},
    3: {"nama": "Mouse", "jumlah": 80, "kategori": "Elektronik"},
    4: {"nama": "LCD", "jumlah": 10, "kategori": "Elektronik"},
}

peminjaman = []

def login():
    print("===== Program Pengelolaaan Inventaris Lab Komputer =====")
    while True:
        username = input("Masukkan Username: ")
        if username.strip() == "":
            print("Username tidak boleh kosong! Silakan masukkan username anda.")
        else:
            break

    while True:
        password = input("Masukkan Password: ")
        if password.strip() == "":
            print("Password tidak boleh kosong! Silakan masukkan password anda.")
        else:
            if len(password) != 6:
                print("Password harus berisi 6 karakter")
            else:
                break
    cek = False
    for data in admin:
        if username == data[0] and password == data[1]:
            cek = True
            break
    if cek:
        print("Login berhasil")
        menu()
    else:
        print("Login gagal")
        login()

def menubarang():
    while True:
        print("\n***** MENU DATA BARANG *****")
        print("1. Lihat Barang")
        print("2. Tambah Barang")
        print("3. Edit Barang")
        print("4. Hapus Barang")
        print("5. Lihat Barang Dipinjam")
        print("6. Pencarian Barang")
        print("7. Kembali ke Menu Utama")
        
        pilihan = input("Masukkan pilihan menu (1-7): ")
        print()
        
        if pilihan == "1":
            tampilBarang()
        elif pilihan == "2":
            tambahBarang()
        elif pilihan == "3":
            editBarang()
        elif pilihan == "4":
            hapusBarang()
        elif pilihan == "5":
            barangDipinjam()
        elif pilihan == "6":
            cariBarang()
        elif pilihan == "7":
            menu()
        else:
            print("Pilihan tidak tersedia. Silakan coba lagi!!!")

def tampilBarang():
    print("DATA BARANG INVENTARIS")
    print("=" * 60)
    print(f"| {'ID':^5} | {'Nama Barang':^20} | {'Jumlah':^10} | {'Kategori':^10} |")
    print("=" * 60)
    for id, data in barang.items():
        print(f"| {id:^5} | {data['nama']:<20} | {data['jumlah']:^10} | {data['kategori']:<10} |")
    print("=" * 60)

def tambahBarang():
    print("\nTAMBAH DATA BARANG")
    id = max(barang.keys()) + 1 if barang else 1
    nama = input("Masukkan nama barang: ")
    # Periksa apakah nama barang sudah ada
    if any(nama.lower() == b["nama"].lower() for b in barang.values()):
        print(f"Barang dengan nama '{nama}' sudah ada. Tidak dapat menambahkan.")
        return

    jumlah = input("Masukkan jumlah barang: ")
    kategori = input("Masukkan kategori barang: ")

    if jumlah.isdigit():
        barang[id] = {"nama": nama, "jumlah": int(jumlah), "kategori": kategori}
        print(f"Barang '{nama}' berhasil ditambahkan.")
    else:
        print("Jumlah barang harus berupa angka.")

def editBarang():
    tampilBarang()
    print("\nEDIT DATA BARANG")
    id = input("Masukkan ID barang yang ingin diubah: ")

    if id.isdigit() and int(id) in barang:
        nama = input("Masukkan nama barang baru: ")
        jumlah = input("Masukkan jumlah barang baru: ")
        kategori = input("Masukkan kategori barang baru: ")

        if jumlah.isdigit():
            barang[int(id)] = {"nama": nama, "jumlah": int(jumlah), "kategori": kategori}
            print(f"Barang dengan ID {id} berhasil diperbarui.")
        else:
            print("Jumlah barang harus berupa angka.")
    else:
        print("ID barang tidak ditemukan.")

def hapusBarang():
    tampilBarang()
    print("\nHAPUS DATA BARANG")
    id = input("Masukkan ID barang yang ingin dihapus: ")

    if id.isdigit() and int(id) in barang:
        barang.pop(int(id))
        print(f"Barang dengan ID {id} berhasil dihapus.")
    else:
        print("ID barang tidak ditemukan.")

def cariBarang():
    print("\n=== PENCARIAN BARANG ===")
    print("1. Cari berdasarkan ID")
    print("2. Cari berdasarkan Nama")
    print("3. Cari berdasarkan Kategori")
    print("4. Kembali ke Menu Data Barang")
    
    pilihan = input("Masukkan pilihan (1-5): ")
    
    if pilihan == "1":
        id = input("Masukkan ID barang: ")
        if id.isdigit() and int(id) in barang:
            data = barang[int(id)]
            print("\nBarang ditemukan:")
            print(f"ID: {id}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Kategori: {data['kategori']}")
        else:
            print("ID barang tidak ditemukan.")
    
    elif pilihan == "2":
        nama = input("Masukkan nama barang: ").lower()
        hasil = {id: data for id, data in barang.items() if nama in data["nama"].lower()}
        if hasil:
            print("\nBarang ditemukan:")
            for id, data in hasil.items():
                print(f"ID: {id}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Kategori: {data['kategori']}")
        else:
            print("Barang dengan nama tersebut tidak ditemukan.")
    
    elif pilihan == "3":
        kategori = input("Masukkan kategori barang: ").lower()
        hasil = {id: data for id, data in barang.items() if kategori in data["kategori"].lower()}
        if hasil:
            print("\nBarang ditemukan:")
            for id, data in hasil.items():
                print(f"ID: {id}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Kategori: {data['kategori']}")
        else:
            print("Barang dengan kategori tersebut tidak ditemukan.")
    
    elif pilihan == "4":
        menubarang()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        cariBarang()


def pinjamBarang():
    print()
    tampilBarang()
    nama = input("Masukkan nama peminjam: ")
    nim = input("Masukkan NIM peminjam: ")

    id = input("Masukkan ID barang yang ingin dipinjam: ")
    jumlah = input("Masukkan jumlah barang yang ingin dipinjam: ")

    if id.isdigit() and int(id) in barang and jumlah.isdigit():
        if jumlah.isdigit() > 0:
            id = int(id)
            jumlah = int(jumlah)

            if jumlah <= barang[id]["jumlah"]:
                barang[id]["jumlah"] -= jumlah
                peminjaman.append([nama, nim, barang[id]["nama"], jumlah, "Belum Dikembalikan"])
                print("Barang berhasil dipinjam. Berikut struk peminjaman:\n")
                struk(nama, nim, barang[id]["nama"], jumlah)
            else:
                print(f"Jumlah barang '{barang[id]['nama']}' tidak mencukupi.")
        else:
            print("Jumlah pinjam tidak boleh kurang dari 1")
    else:
        print("ID barang atau jumlah tidak valid.")

def kembalikanBarang():
    if peminjaman == 0:
        print("Belum ada barang yang dipinjam.")
        return

    print("\nDATA PEMINJAMAN")
    print(f"{'No':<5} {'Nama':<20} {'NIM':<15} {'Barang':<20} {'Jumlah':<10} {'Status':<20}")
    print("=" * 90)
    for i, item in enumerate(peminjaman, start=1):
        print(f"{i:<5} {item[0]:<20} {item[1]:<15} {item[2]:<20} {item[3]:<10} {item[4]:<20}")

    id = input("Masukkan nomor peminjaman yang ingin dikembalikan: ")

    if id.isdigit() and 1 <= int(id) <= len(peminjaman):
        id = int(id)
        item = peminjaman[id - 1]
        if item[4] == "Sudah Dikembalikan":
            print("Barang ini sudah dikembalikan sebelumnya.")
            return

        jumlah = input("Masukkan jumlah barang yang ingin dikembalikan: ")

        if jumlah.isdigit():
            jumlah = int(jumlah)

            for id, data in barang.items():
                if data["nama"] == item[2]:
                    if jumlah <= item[3]:
                        barang[id]["jumlah"] += jumlah
                        item[3] -= jumlah
                        print(f"Barang {item[2]} sebanyak {jumlah} berhasil dikembalikan.")
                        if item[3] == 0:
                            item[4] = "Sudah Dikembalikan"
                        return
                    else:
                        print("Jumlah barang yang dikembalikan melebihi jumlah yang dipinjam.")
                        return
        else:
            print("Jumlah barang harus berupa angka.")
    else:
        print("Nomor peminjaman tidak valid.")

def tampilPeminjaman():
    if not peminjaman:
        print("Belum ada data peminjaman.")
        return

    print("\nDATA PEMINJAMAN")
    print(f"{'No':<5} {'Nama':<20} {'NIM':<15} {'Barang':<20} {'Jumlah':<10} {'Status':<20}")
    print("=" * 90)
    for i, item in enumerate(peminjaman, start=1):
        print(f"{i:<5} {item[0]:<20} {item[1]:<15} {item[2]:<20} {item[3]:<10} {item[4]:<20}")


def barangDipinjam():
    barangDipinjam = {item[2] for item in peminjaman if item[4] == "Belum Dikembalikan"}
    if barangDipinjam:
        print("\nBarang yang Sedang Dipinjam:")
        for nama in barangDipinjam:
            print(f"- {nama}")
    else:
        print("Tidak ada barang yang sedang dipinjam.")

def struk(nama, nim, barang, jumlah):
    print("\n====== STRUK PEMINJAMAN ======")
    print(f"Nama Peminjam: {nama}")
    print(f"NIM Peminjam : {nim}")
    print(f"Barang       : {barang}")
    print(f"Jumlah       : {jumlah}")
    print("==============================")
        
def menu():
    while True:
        print("\n===== INVENTARIS LABORATORIUM INTELIJEN SISTEM =====")
        print("SILAHKAN PILIH MENU : \n")
        print("1. Data Barang")
        print("2. Peminjaman Barang")
        print("3. Pengembalian Barang")
        print("4. Data Peminjaman")
        print("5. Keluar")
        
        pilihan = input("Masukkan pilihan menu (1-5): ")
        
        if pilihan == "1":
            menubarang()
        elif pilihan == "2":
            pinjamBarang()
        elif pilihan == "3":
            kembalikanBarang()
        elif pilihan == "4":
            tampilPeminjaman()
        elif pilihan == "5":
            print("Terima kasih")
            login()
        else:
            print("Pilihan tidak tersedia. Silakan coba lagi!!!")

login()
