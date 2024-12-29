# oop di gunakan untuk mengubah apapun di anggap objek agar lebih mudah untuk melakukan pengcodingan
# dengan cara mengkelompokan ke dalam class
# kenapa memakai objek? agar satu objek ke objek yang lain bisa interaksi dengan adanya template

# clas mempunya dua ciri yaitu atribut (identitas objek) dan method (hal yang bisa di lakukan oleh objek)

'''
cara membuat class
1. harus mendeklarasikan class terlebi dahulu (template)
2. membuat objek yang di kaitkan ke template
'''

# 1. mendeklarasikan class
class hero:
    pass

# 2. membuat objek
hero1 = hero()
hero2 = hero()
hero3 = hero()

# 3. mendeklarasikan atribut di dalam objek
hero1.nama = "bejo"
hero1.healt = 100

hero2.name = "king z"
hero2.healt = 200

hero3.name = "ucup"
hero3.healt = 90

# untuk mengecek atribut hero
print(hero1.__dict__)
print()

# untuk melihat adress dari suatu objek
# nilai adress dari setiap objek pasti berbeda
print(hero1)
print(hero2)

# untuk mengakses atribut objek
print(hero1.nama)