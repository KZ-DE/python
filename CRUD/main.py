import os
from CRUD import Creat
from CRUD import Search
from CRUD import Readpd
from CRUD import Update
 

if __name__ == "__main__":
    
    Creat.membuat_database() # mengecek database
    
    

    while(True):
        sistemOperasi = os.name
        match sistemOperasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        
        print(f"{'='*10} DATABASE PERPUSTAKAAN {'='*10}")
        print("="*43)
        print('')
        
        
        print("1. Creat Data")
        print("2. Read Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Search Data")
        print('')
        
        user = input("Masukan Sesuai Angka : ")
        print("="*23)
        print('')
        
        match user:
            case '1' | "creat data":
                Creat.creat()
            case '2' | "read data":
                Readpd.Reat_pd()
            case '3' | "update data":
                Update.update()
            case '4' | "delet data":
                print("Delete Data")
            case "5" | "search data":
                Search.search()                
            case _ :
                print("tolong masukan dengan benar")
        
        bot = input("\napakah sudah selesai? (y/n) : ")
        if bot == "y":
            break

print("Terimakasih :)")