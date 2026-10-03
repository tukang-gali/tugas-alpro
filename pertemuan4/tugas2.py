PI = 3.14

r = float(input("Masukkan jari-jari tabung: "))
t = float(input("Masukkan tinggi tabung: "))

luas = 2 * PI * r * (r + t)

print("Luas permukaan tabung adalah {:.2f}".format(luas))