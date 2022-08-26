print("============")
print("bangun ruang")
print("============")

print("\n1,Balok")

panjang = int(input("masukan nilai panjang: "))
lebar = int(input("masukan nilai lebar: "))
tinggi = int(input("masukan nilai tinggi: "))
volume = panjang * lebar
print("volume balok adalah:", volume)

print("\n2,limas")

alas = int(input("masukan nilai alas: "))
tinggi = int(input("masukan nilai tinggi: "))
volume_l = alas * tinggi
print("volume limas adalah: ", volume_l )

print("\n3,tabung")

r =int(input("masukan jari jari: "))
t = int(input("masukan nilai tinggi: "))
keliling = 2 * 3,14 * r
luas = 3,14 * r * r
print("keliling =" ,keliling)
print("luas =" ,luas)

print("\n4,tabung")

alas = float(input("masukan nilai alas: "))
tinggi = float(input("masukan nilai tinggi: "))
luas_tb = alas * tinggi
print("luas =", luas_tb)

print("/n5,dolar")

kursdolar = 14000
rupiah = float(input("masukan uang rupiah anda: "))
ruptodol = rupiah / kursdolar
doldecimal = round(ruptodol, 2)
print("rp.",rupiah, "==> US$", doldecimal)
