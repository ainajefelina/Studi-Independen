def kubus():
    "menghitung kubus"
    s=int(input("Masukan panjang sisi kubus = "))
    volKubus = s*s*s
    lpKubus = 6*s*s
    print("Panjang sisi kubus : ", s)
    print("Volume kubus: ", volKubus)
    print("Luas permukaan kubus : ", lpKubus)

def balok():
    "menghitung balok"
    p=int(input("Masukan panjang balok : "))
    l=int(input("Masukan lebar balok : "))
    t=int(input("Masukan tinggi balok : "))
    volBalok = p*l*t
    lpBalok = 2*((p*l)+(p*t)+(t*l))
    print("Panjang Balok : ", p)
    print("Lebar balok : ", l)
    print("Tinggi balok : ", t)
    print("Volume balok : ", volBalok)
    print("Luas permukaan balok : ", lpBalok)

def bola():
    "Menghitung bola"
    r=int(input("Masukan jari - jari bola : "))
    pi = float(22/7)
    volBola = 4/3*pi*r
    lpBola = 4*pi*r*r
    print("Jari - jari bola : ", r)
    print("Volume bola : ", volBola)
    print("Luas Permukaan bola : ", lpBola)

def tabung():
    "Menghitung tabung"
    r = int(input("Masukan jari - jari alas tabung : "))
    t = int(input("Masukan tinggi tabung : "))
    pi = float(22/7)
    lAlas = (pi*r*r)
    kAlas = (2*pi*r)
    volTabung = (lAlas*t)
    lpTabung = ((2*lAlas)+(t*kAlas))
    print("Jari - jari alas tabung : ", r)
    print("Tinggi tabung : ", t)
    print("Volume tabung : ", volTabung)
    print("Luas Permukaam tabung : ", lpTabung)
    return
