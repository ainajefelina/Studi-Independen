print("Perhitungan 2 Dimensi")
print("1, Segi Empat")
print("2, Segi Tiga")
print("3, Persegi")
print("4, Lingkaran")

ulang = "Y"

while ulang=="Y" or ulang=="y":
    pilihan = int(input("Masukan Pilihan Anda, eg. 1, 2, dst "))
    
    if pilihan == 1:
        panjang = input (" Masukan Variable Panjang")
        lebar = input ("Masukan Variable Lebar")
        KelilingSegiempat = 2*int(panjang)+2*int(lebar)
        LuasSegiempat = int(panjang)*int(lebar)
        print("Panjang Segiempat =", panjang)
        print("Lebar Segiempat =", lebar)
        print("Keliling Segiempat =", KelilingSegiempat)
        print("Luas Segiempat =", LuasSegiempat)
    
    elif pilihan == 2:
        alas = input (" Masukan Variable Alas")
        tinggi = input ("Masukan Variable Tinggi")
        PanjangSisi1 = input ("Masukan Variable Panjang Sisi 1")
        PanjangSisi2 = input ("Masukan Variable Panjang Sisi 2")
        PanjangSisi3 = input ("Masukan Variable Panjang Sisi 3")
        LuasSegitiga = (1/2)*int(alas)*int(tinggi)
        KelilingSegitiga = int(PanjangSisi1)+int(PanjangSisi2)+int(PanjangSisi3)
        print("Alas Segitiga =", alas)
        print("Tinggi Segitiga =", tinggi)
        print("Luas Segitiga =", LuasSegitiga)
        print("Keliling Segitiga=", KelilingSegitiga)
   
    elif pilihan == 3:
        PanjangSisi= input (" Masukan Variable Panjang Sisi")
        KelilingPersegi = 4*int(PanjangSisi)
        LuasPersegi = 2*int(PanjangSisi)
        print("PanjangSisi =", PanjangSisi)
        print("Luas Persegi =", LuasPersegi)
        print("Keliling Persegi =", KelilingPersegi)
    
    elif pilihan == 4:
        JariJari= input ("Masukan Variable Jari - Jari")
        LuasLingkaran = float(22/7)*int(JariJari)
        KelilingLingkaran = 2*float(22/7)*int(JariJari)
        print("Jari - jari =", JariJari)
        print("Luas Lingkaran=", LuasLingkaran)
        print("Keliling Lingkaran=", KelilingLingkaran)
    
    else :
        print ("Belum Tersedia")

    ulang = input("Apakah amda ingin mengulang? (Y/N)")

else:
    print("Program Selesai")