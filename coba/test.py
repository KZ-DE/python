n = int(input("Maukan niali N: "))

jumlah = 1
space = (n-1)
jumlah2 = n-1

for i in range(n):
    print("*"*jumlah, " "*space + " "*jumlah2 + "*"*jumlah)   
    jumlah+=1 
    space-=1
    jumlah2-=1


jumlah-=1
jumlah2+=1
print("*"*n+"*"*n+"*")
space +=1

for i in range(n):
    print("*"*jumlah, " "*space + " "*jumlah2 + "*"*jumlah)   
    jumlah-=1 
    space+=1
    jumlah2+=1