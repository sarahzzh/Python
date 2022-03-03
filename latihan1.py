#menentukan bilangan ganjil genap

from turtle import distance


A= int(input("masukkan jumlah data = "))
for i in range (1,A,2) :
    print(i,"adalah bilangan ganjil")
    print(i+1,"adalah bilangan genap")

if A%2 !=0:
    print(A,"adalah bilangan ganjil")

print(30*"=")

P = int(input("banyaknya data = "))
if P>0:
    i=1
    x=int(input("Data ke -"+str(i)+"="))
    max=x;min=x;total=x
    for i in range (2,P+1) :
        x=int(input("data ke -"+str(i)+"="))
        total+=x
        if max<x:
            max=x
        elif min>x:
                min=x
dis=max-min
ratarata=total/x

print("bilangan terbesarnya =", max)
print("bilangan terkecilnya =", min)
print("range =", dis)
print("total =", total)
print("rata-rata =", ratarata)