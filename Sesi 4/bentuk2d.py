def Segiempat():
    "Fungsi Menghitung Segi Empat"
    p=int(input("Masukan nilai panjang= "))
    l=int(input("Masukan nilai lebar= "))
    KelilingSegiempat = 2*int(p)+2*int(l)
    LuasSegiempat = int(p)*int(l)
    print("Panjang Segiempat =", p)
    print("Lebar Segiempat =", l)
    print("Keliling Segiempat =", KelilingSegiempat)
    print("Luas Segiempat =", LuasSegiempat)

def Segitiga():
    "Fungsi Menghitung Segi Tiga"
    a= int(input("Masukan nilai Alas= "))
    t= int(input("Masukan nilai Tinggi = "))
    s1 = int(input("Masukan nilai Sisi 1= "))
    s2 = int(input("Masukan nilai Sisi 2= "))
    s3 = int(input("Masukan nilai Sisi 3= "))
    LuasSegitiga = float(1/2)*int(a)*int(t)
    KelilingSegitiga = int(s1)+int(s2)+int(s3)
    print("Alas Segitiga =", a)
    print("Tinggi Segitiga =", t)
    print("Luas Segitiga =", LuasSegitiga)
    print("Keliling Segitiga=", KelilingSegitiga)

def Persegi():
    "Fungsi Menghitung Persegi"
    s=int(input("Masukan Nilai Sisi= "))
    KelilingPersegi = 4*(s)
    LuasPersegi = 2*(s)
    print("PanjangSisi =", s)
    print("Luas Persegi =", LuasPersegi)
    print("Keliling Persegi =", KelilingPersegi)

def Lingkaran():
    "Fungsi Menghitung Lingkaran"
    r = input("Masukan Panjang Jari - Jari Lingkaran")
    LuasLingkaran = float(22/7)*int(r)
    KelilingLingkaran = 2*float(22/7)*int(r)
    print("Jari - jari =", r)
    print("Luas Lingkaran=", LuasLingkaran)
    print("Keliling Lingkaran=", KelilingLingkaran)