import csv
import time
from . import pk
from CRUD import template

### bentuk biasah
def membuat_database():
    try:
        with open ('Database/Database.csv','r') as file:
            print("Database Ditemukan")
            time.sleep(0.5)
    except:
        print("Database Tidak Di Temukan, Membuat Database Baru")
        print("Loading....")
        time.sleep(2)
        with open ("Database/Database.csv", "w", encoding='utf-8', newline='') as file:
            header ="PK", "Nama Komponen", "Jenis Komponen", "Tipe Komponen", "."
            # tepi ='--', "-------------", "--------------", "-------------", "."
            w = csv.writer(file)
            w.writerow(header) 
            # w.writerow(tepi) 

            
def creat():
    namePk = pk.pk()
    komponen = input("Nama komponen : ")
    jenis = input("Jenis komponen : ")
    tipe = input("Tipe komponen : ")
    end = '.'
    # dt = template.TEMPLATE.copy()
    # dt['pk'] = namePk
    # dt['nama'] = komponen + template.TEMPLATE['nama'][len(komponen):]
    # dt['jenis'] = jenis + template.TEMPLATE['jenis'][len(jenis):]
    # dt['tipe'] + tipe + template.TEMPLATE['tipe'][len (tipe):]

    with open ("Database/Database.csv", "a", encoding='utf-8', newline='') as file:
            w = csv.writer(file)
            data = namePk, komponen, jenis, tipe, end
            w.writerow(data)
         
### tipe dict

# def membuat_database():
#     try:
#         with open ('Database/Database.csv','r') as file:
#             print("Database Ditemukan")
#             time.sleep(0.5)
#     except:
#         print("Database Tidak Di Temukan, Membuat Database Baru")
#         print("Loading....")
#         time.sleep(2)
        
#         with open ("Database/Database.csv", "w", encoding='utf-8', newline='') as file:
#             w = csv.DictWriter(file,fieldames=["PK", "Nama Komponen", "Jenis Komponen", "Tipe Komponen", "."])
#             w.writeheader()
            
# def creat():
#     namePk = pk.pk()
#     komponen = input("Nama komponen : ")
#     jenis = input("Jenis komponen : ")
#     tipe = input("Tipe komponen : ")
#     end = '.'

#     with open ("Database/Database.csv", "a", encoding='utf-8', newline='') as file:
#         w = csv.DictWriter(file)
#         data = namePk, komponen, jenis, tipe, end
#         w.writerow(data)