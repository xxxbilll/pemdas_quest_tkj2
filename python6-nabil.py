print("1. segitiga")

alas =int(input("nilai alas : "))
tinggi = int(input("nilai tinggi : "))
luas_s = alas * tinggi /2

print("luas segitiga adalah", luas_s)

print("\n2. persegi panjang")

panjang = int(input("nilai panjang: "))
lebar = int(input("nilai lebar: "))
luas_pp = panjang * lebar 

print("luas persegi panjang adalah", luas_pp)

print("\n3. jajargenjang")

alas = float(input("nilai alas: "))
tinggi = float(input("nilai tinggi: "))
luas_jg = alas * tinggi

print("luas jajargenjang adalah", luas_jg)

print("\n4. lingkaran")

r = float(input("masukan jari jari"))
luas_l = 3.14 * r * r 
print("luas lingkaran adalah", luas_l)    
except Exception, e:
    raise e
except Exception, e:
    raise e