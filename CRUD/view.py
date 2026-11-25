data_barang = []

def tambah_barang():
    ID = input("Masukkan ID barang: ")
    nama_barang = input("Masukkan nama barang: ")
    stok_barang = int(input("Masukkan stok barang: "))
    harga_barang = int(input("Masukkan harga barang: "))

    barang = {
        "id": ID,
        "nama": nama_barang,
        "stok": stok_barang,
        "harga": harga_barang
    }
    data_barang.append(barang)
    return barang


