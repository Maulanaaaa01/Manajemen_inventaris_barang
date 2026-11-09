data_barang = []

while(True):
    print("=" * 40)
    print("SISTEM MANAJEMEN INVENTARIS".center(40))
    print("=" * 40)

    print("1. Tambah barang")
    print("2. Lihat barang")
    print("3. Cari barang")
    print("4. Ubah barang")
    print("5. Hapus barang")
    print("6. Barang masuk")
    print("7. Barang keluar")
    print("8. Laporan inventaris")
    print("9. Simpan dan muat data")
    print("10. Keluar")
    print("=" * 40)

    option = input("Pilih menu (1-10): ")

    match option:
        case "1": print("Tambah barang")
        case "2": print("Lihat barang")
        case "3": print("Cari barang")
        case "4": print("Ubah barang")
        case "5": print("Hapus barang")
        case "6": print("Barang masuk")
        case "7": print("Barang keluar")
        case "8": print("Laporan inventaris")
        case "9": print("Simpan dan muat data")
        case "10": 
            is_done = input("Apakah anda ingin keluar (y/n): ")
            if is_done.lower() == "y":
                print("Terima kasih telah menggunakan sistem manajemen inventaris.")
                break
            else:
                print("Kembali ke menu utama.")
        case _: print("Menu tidak valid. Silakan pilih menu yang tersedia.")
        
    
        