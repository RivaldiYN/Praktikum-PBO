temperatur = float(input("Masukkan temperatur dalam celcius: "))


if temperatur >= 100:
    print(f"Wujud air pada suhu {temperatur} derajat Celcius adalah Gas")
elif temperatur <= 0:
    print(f"Wujud air pada suhu {temperatur} derajat Celcius adalah Padat")
else:
    print(f"Wujud air pada suhu {temperatur} derajat Celcius adalah Cair")