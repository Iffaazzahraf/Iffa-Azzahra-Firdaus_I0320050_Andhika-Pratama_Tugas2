print ("tugas programa komputer weeks 2")

print("oleh:Iffa Azzahra Firdaus(I0320050)")
print("=============")
print("penghitung cepat")
print("=============")

print("mau hitung apanih?")
print("1. luas persegi panjang")
print("2. luas lingkaran")
print("3. luas permukaan kubus")
print("4. konversi suhu celsius ke fahrenheit")
print("5. konversi suhu reamur ke kelvin")

print("==================")

choice=input("pilih nomor yang mau dihitung (1/2/3/4/5):")

if choice == "1":
    p=float(input("berapa panjangnya (dalam cm)?"))
    l=float(input("berapa lebarnya (dalam cm)? "))
    luas= float(p)*float(l)
    print("luas persegi panjang tersebut adalah",int(luas),"cm")
    cetak =1



elif choice == "2":
    r = float(input("berapa panjang jari-jarinya?  "))
    Luas = 3.14*r*r
    print("lingkaran tersebut memiliki luas sebesar",int(Luas),)
    cetak = 1

elif choice == "3":
    rusuk = float(input("berapa panjang rusuknya? "))
    Luas = 6*float(rusuk)**2
    print ("luas permukaan kubus tersebut adalah",int(Luas),)
    cetak = 1

elif choice == "4":
    celcius = float(input("berapa suhunya? "))
    ckef = (9/5 * float(celcius)) + 32
    print ("suhu",int(celcius), "celcius =",int(ckef),"fahrenheit")
    cetak = 1

elif choice == "5":
    reamur = float(input("berapa suhunya?  "))
    rkec = 5/4 *float(reamur)
    print ("suhu",int(reamur),"reamur =",int(rkec)," celcius")
    cetak = 1

else :
    print("input salah")











