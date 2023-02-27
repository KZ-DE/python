import csv
import pandas as pd

isi = [] # membuat tempalte list

def search ():
    with open ("Database/Database.csv", 'r') as file:
        data = csv.reader(file) # membaca isi file
        for row in data:
            isi.append(row) # merubah isi file ke dalam bentuk list
            
    isi.pop(0)
    jumlah = len(isi)
    print(f"jumlah komponen == {jumlah}\n")
    no = 0
    for data in isi:
        no += 1
        print(f"{data[0]} \t {data[1]} \t {data[2]} \t {data[3]} \t {no}") # memformat string
        
    print("\nAngka di akhir merupakan urutan\n")
    print(isi)
    
    # test
    user = int(input("pilih angka : "))
    nama = input("nama baru :")
    tipe = input()
    a = input()
    
    urut = user - 1
    
    isi[urut][1] = nama
    isi[urut][2] = tipe
    isi[urut][3] = a
    
    namePk = isi[urut][0]
    komponen = isi[urut][1]
    jenis = isi[urut][2]
    tipe = isi[urut][3]
    end = '.'
    
    # r=pd.read_csv("Database/Database.csv")
    # r.drop([urut], inplace=True)
    # r.to_csv("Database/Database.csv")
    
    
    with open ("Database/Database.csv", "a", encoding='utf-8', newline='') as file:
            w = csv.writer(file)
            newdata = namePk, komponen, jenis, tipe, end
            w.writerows(newdata)
    
    print(isi)
