# operasi list
BaseException

data_angka = [1,4,6,3,7,9,4,7,0,4,7,3,0,3,4,6,3,5,2,7,9,2,3,4,5,7,3,6,3]
print(f"banyak data = {data_angka}")

# menghitung banyaknya item dalam list
data4 = data_angka.count(4)
data9 = data_angka.count(9)
print(f"banyaknya angka 4 = {data4}")
print(f"banyaknya angka 9 = {data9}")

# mengetahu posisi data(index)
data = ["sudrun","bejo","slamet","ahri"]
print(f"data nama = {data}")
index_bejo = data.index("bejo")
print(f"index bejo = {index_bejo}")

# mengurutkan data
print(f"data angka = {data_angka}")
data_angka.sort()
print(f"data angka terurut = {data_angka}") # di urutukan terhadap angka terkecil terlebih dahulu
print(data)
data.sort()
print(f"data terurut = {data}") # akan menampilkan sesuai aljabar huruf depannya

# membalik urutan data list
data_angka.reverse()
print(f"data terurut terbesar = \n{data_angka}")