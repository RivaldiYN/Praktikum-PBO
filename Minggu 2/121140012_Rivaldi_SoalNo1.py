class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

    def tampilkan_info(self):
        print(f"Judul: {self.judul}")
        print(f"Pengarang: {self.pengarang}")
        print(f"Tahun terbit: {self.tahun_terbit}")

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def tampilkan_daftar_buku(self):
        if not self.daftar_buku:
            print("Tidak ada buku dalam perpustakaan.")
        else:
            for index, buku in enumerate(self.daftar_buku):
                print(f"Index buku: {index}")
                buku.tampilkan_info()

    def hapus_buku(self, index):
        if index >= len(self.daftar_buku):
            print("Index tidak valid.")
        else:
            self.daftar_buku.pop(index)

    def modifikasi_buku(self, index, judul_baru=None, pengarang_baru=None, tahun_terbit_baru=None):
        if index >= len(self.daftar_buku):
            print("Index tidak valid.")
        else:
            buku = self.daftar_buku[index]
            if judul_baru:
                buku.judul = judul_baru
            if pengarang_baru:
                buku.pengarang = pengarang_baru
            if tahun_terbit_baru:
                buku.tahun_terbit = tahun_terbit_baru

if __name__ == "__main__":
    perpustakaan = Perpustakaan()

    # Meminta jumlah buku yang ingin dimasukkan
    jumlah_buku = int(input("Masukkan jumlah buku yang ingin dimasukkan: "))

    # Memasukkan buku secara manual
    for i in range(jumlah_buku):
        print(f"\nMasukkan informasi buku ke-{i+1}:")
        judul = input("Judul: ")
        pengarang = input("Pengarang: ")
        tahun_terbit = int(input("Tahun terbit: "))
        buku = Buku(judul, pengarang, tahun_terbit)
        perpustakaan.tambah_buku(buku)

    # Menampilkan daftar buku dalam perpustakaan
    perpustakaan.tampilkan_daftar_buku()

    # Menghapus buku dari perpustakaan
    index_hapus = int(input("Masukkan index buku yang ingin dihapus: "))
    perpustakaan.hapus_buku(index_hapus)

    # Menampilkan daftar buku dalam perpustakaan setelah buku dihapus
    perpustakaan.tampilkan_daftar_buku()

    # Modifikasi buku dalam perpustakaan
    index_modifikasi = int(input("Masukkan index buku yang ingin dimodifikasi: "))
    judul_baru = input("Masukkan judul baru (kosongkan jika tidak ingin mengubah): ")
    pengarang_baru = input("Masukkan pengarang baru (kosongkan jika tidak ingin mengubah): ")
    tahun_terbit_baru = input("Masukkan tahun terbit baru (kosongkan jika tidak ingin mengubah): ")
    perpustakaan.modifikasi_buku(index_modifikasi, judul_baru, pengarang_baru, tahun_terbit_baru)

    # Menampilkan daftar buku dalam perpustakaan setelah buku dimodifikasi
    perpustakaan.tampilkan_daftar_buku()


