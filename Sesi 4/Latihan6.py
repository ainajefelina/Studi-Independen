import bentuk2d

print("Perhitungan 2 dimensi")
print("1, Segi Empat")
print("2, Segi Tiga")
print("3, Persegi")
print("4, Lingkaran")

ulang = "Y"
while ulang == "Y" or ulang == "y":
    pilihan= int(input("Masukan Pilihan Anda = "))
    
    if pilihan==1:
        bentuk2d.segiempat()
    
    elif pilihan ==2:
        bentuk2d.Segitiga()
        
    elif pilihan ==3:
        bentuk2d.Persegi()
    
    elif pilihan ==4:
        bentuk2d.Lingkaran()
        
    else:
        print("Pilihan belum Tersedia")
    
    ulang = input("Apakah amda ingin mengulang? (Y/N)")

else:
    print("Program Selesai")
    exit