print("1. Balok")

panjang = int(input("masukan nilai panjang"))
lebar = int(input("masukan nilai lebar"))
tinggi = int(input("masukan nilai tinggi"))

volume_bal = panjang * lebar * tinggi
print("Nilai volume balok adalah", volume_bal)

print("2. \nTabung")

Luas_alas_lingkaran = int(input("masukan nilai luas alas lingkaran"))
tinggi = int(input("masukan nilai tinggi"))

volume_ling = Luas_alas_lingkaran * tinggi
print("nilai volume tabung adalah", volume_ling)

print("3. \nlimas")

Luas_alas_persegi = int(input("masukan nilai alas luas persegi"))
tinggi = int(input("masukan nilai tinggi"))
volume_lim = (1/3 * Luas_alas_persegi) * tinggi

print("Nilai volume limas adalah", volume_lim)

x = int(input("masukan nilai mata uang: "))
y = x * 14000
print(x,"dollar =",y,"rupiah")

 