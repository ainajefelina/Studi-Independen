import bentuk3d

print("Perhitungan 3 dimensi")
print("1, Kubus")
print("2, Balok")
print("3, Bola")
print("4, Tabung")

ulang = "Y"
while ulang == "Y" or ulang == "y":

    pilihan = int(input("Masukan Pilihan Anda = "))
    if pilihan == 1:
        bentuk3d.kubus()
    
    elif pilihan == 2:
        bentuk3d.balok()
    
    elif pilihan == 3:
        bentuk3d.bola()

    elif pilihan == 4:
        bentuk3d.tabung()

    else:
        print("Pilihan anda salah")

    ulang = input("Apakah anda ingin  mengulang ? (Y/n) ")

else:
    print("Program selesai")
    exit