def prima(n):
    if n < 2:
        return False
    for i in range(2, int(n*0.5) + 1):
        if n % i == 0:
            return False
    return True #fungsi untuk menentukan angka prima

angka_prima = 0
angka_bukan_prima = 0 #inisiasi untuk angka prima dan bukan dibuat 0

for i in range(10):
    num = int(input(f"Masukkan bilangan ke-{i+1}: "))
    if prima(num):
        print(f"{num} adalah bilangan prima")
        angka_prima += 1
        print(" ")
    else:
        print(f"{num} bukan bilangan prima")
        angka_bukan_prima += 1
        print(" ")

print(f"Jumlah angka bilangan prima: {angka_prima}")
print(f"Jumlah angka bukan bilangan prima: {angka_bukan_prima}")

if angka_prima + angka_bukan_prima > 0:
    persentase_prima = (angka_prima / (angka_prima + angka_bukan_prima)) * 100
    print(f"Persentase bilangan prima: {persentase_prima}%")
else:
    print("Tidak ada bilangan yang dimasukkan")
