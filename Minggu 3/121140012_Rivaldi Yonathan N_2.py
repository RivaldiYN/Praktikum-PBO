class Produk:
    def __init__(self, hargaProduk):
        self.hargaProduk = hargaProduk

    def hitungHarga(self):
        pass

class Makanan(Produk):
    def __init__(self, hargaProduk, jumlah):
        super().__init__(hargaProduk)
        self.jumlah = jumlah

    def hitungHarga(self):
        return self.hargaProduk * self.jumlah

class Minuman(Produk):
    def __init__(self, hargaProduk, ukuran, jumlah):
        super().__init__(hargaProduk)
        self.ukuran = ukuran
        self.jumlah = jumlah

    def hitungHarga(self):
        return self.hargaProduk * self.ukuran * self.jumlah

class Barang(Produk):
    def __init__(self, hargaProduk, berat):
        super().__init__(hargaProduk)
        self.berat = berat

    def hitungHarga(self):
        return self.hargaProduk * self.berat

class KeranjangBelanja():
    def __init__(self):
        self.produks = []

    def tambahProduk(self, produk):
        self.produks.append(produk)

    def hitungTotalHarga(self):
        totalHarga = 0
        for produk in self.produks:
            totalHarga += produk.hitungHarga()
        return totalHarga

keranjang = KeranjangBelanja()

makanan1 = Makanan(5000, 5)
keranjang.tambahProduk(makanan1)

minuman1 = Minuman(1000, 200, 3)
keranjang.tambahProduk(minuman1)

barang1 = Barang(5000, 5)
keranjang.tambahProduk(barang1)

print(keranjang.hitungTotalHarga())