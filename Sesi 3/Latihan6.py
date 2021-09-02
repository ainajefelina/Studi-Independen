def Segiempat(p, l):
    "Fungsi Menghitung Segi Empat"
    KelilingSegiempat = 2*int(p)+2*int(l)
    LuasSegiempat = int(p)*int(l)
    print("Panjang Segiempat =", p)
    print("Lebar Segiempat =", l)
    print("Keliling Segiempat =", KelilingSegiempat)
    print("Luas Segiempat =", LuasSegiempat)

def Segitiga(a, t, s1, s2, s3):
    "Fungsi Menghitung Segi Tiga"
    LuasSegitiga = float(1/2)*int(a)*int(t)
    KelilingSegitiga = int(s1)+int(s2)+int(s3)
    print("Alas Segitiga =", a)
    print("Tinggi Segitiga =", t)
    print("Luas Segitiga =", LuasSegitiga)
    print("Keliling Segitiga=", KelilingSegitiga)

def Persegi(s):
    "Fungsi Menghitung Persegi"
    KelilingPersegi = 4*(s)
    LuasPersegi = 2*(s)
    print("PanjangSisi =", s)
    print("Luas Persegi =", LuasPersegi)
    print("Keliling Persegi =", KelilingPersegi)

def Lingkaran(r):
    "Fungsi Menghitung Lingkaran"
    LuasLingkaran = float(22/7)*int(r)
    KelilingLingkaran = 2*float(22/7)*int(r)
    print("Jari - jari =", r)
    print("Luas Lingkaran=", LuasLingkaran)
    print("Keliling Lingkaran=", KelilingLingkaran)

print("Perhitungan 2 dimensi")
print("1, Segi Empat")
print("2, Segi Tiga")
print("3, Persegi")
print("4, Lingkaran")

pilihan= int(input("Masukan Pilihan Anda = "))

if pilihan==1:
    p=int(input("Masukan nilai panjang= "))
    l=int(input("Masukan nilai lebar= "))
    Segiempat(p,l)

elif pilihan ==2:
    a= int(input("Masukan nilai Alas= "))
    t= int(input("Masukan nilai Tinggi = "))
    s1 = int(input("Masukan nilai Sisi 1= "))
    s2 = int(input("Masukan nilai Sisi 2= "))
    s3 = int(input("Masukan nilai Sisi 3= "))
    Segitiga(a, t, s1, s2, s3)

elif pilihan ==3:
    s=int(input("Masukan Nilai Sisi= "))
    Persegi(s)

elif pilihan ==4:
    r = input("Masukan Panjang Jari - Jari Lingkaran")
    Lingkaran(r)

else:
    print("Pilihan belum Tersedia")