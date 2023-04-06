class Operasi:
    def tambah(self, a, b):
        return a + b

    def kurang(self, a, b):
        return a - b

    def kali(self, a, b):
        return a * b

    def bagi(self, a, b):
        return a / b

class Tampil:
    def tampil(self, hasil):
        print(hasil)

class Kalkulator(Operasi, Tampil):
    def __init__(self):
        Operasi.__init__(self)
        Tampil.__init__(self)

    def hitung(self):
        angka1 = int(input("Masukkan angka pertama: "))
        operasi = input("Masukkan operasi (+,-,* atau /): ")
        angka2 = int(input("Masukkan angka kedua: "))
        if operasi == "+":
            hasil = self.tambah(angka1, angka2)
        elif operasi == "-":
            hasil = self.kurang(angka1, angka2)
        elif operasi == "*":
            hasil = self.kali(angka1, angka2)
        elif operasi == "/":
            hasil = self.bagi(angka1, angka2)
        else:
            print("Invalid input")
            return
        print("Hasil perhitungan adalah:", hasil)

kalkulator = Kalkulator()
kalkulator.hitung()
