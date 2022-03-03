#list
angka_prima = [1,3,5,7,11,13,17,19]
print (angka_prima)
for a in angka_prima:
    print("angka prima adalah angka yang hanya bisa dibagi oleh bilangan itu sendiri.")
    print(f"berikut adalah contoh bilangan prima : {a}")

print(30*"=")

#Range
print(f"presentasi akan dimulai 3 detik lagi")

for i in range (3):
    print(i)

print(30*"=")

#string
string_data = "chocomyday"
for str in string_data:
    print(str)

print(20*"-")

str_data = "191202"
for data in str_data:
    print(data)

print(30*"=")

#while

angka = 0
print("jumlah murid saat ini adalah :", angka)
while angka < 10:
    angka += 1
    print(f"jumlah murid tahun ini adalah {angka}")
    print("test while loops")
