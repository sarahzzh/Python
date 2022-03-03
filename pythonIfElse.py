print("Hello World")
print("----------------")

print("Selamat Datang di My ATM")
print("Silahkan Pilih Option:")
print("1. Cek Saldo Saya")
print("2. Tarik Tunai")
print("3. Setor Tunai")
option=int(input("Silahkan Pilih Option:"))
if option ==1: #kondisi 1
    print("Sisa saldo 500.000")
elif option ==2: 
    print("Masukkan Nominal yang akan ditarik")
    print("1. Rp. 100.000")
    print("2. Rp. 50.000")
    saldo=500000
    option2=int(input("option:"))
    if option2==1:
        hasil= saldo-100000
        print("Sisa saldo anda sekarang tinggal :", hasil)
    elif option2==2:
        hasil2= saldo-50000
        print("Sisa saldo anda sekarang tinggal :", hasil2)
    else:
        print("Kode yang anda masukkan salah")
elif option ==3:
    saldo=500000
    print("Silahkan masukkan nominal yang akan di setor")
    option3=int(input("Masukkan nominal yang akan di setor :"))
    hasil3=saldo+option3
    print("jumlah uang kamu sekarang adalah :", hasil3)
else:
    print("Keyword yang anda masukkan salah")  
    



