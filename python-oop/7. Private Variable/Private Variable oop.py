class Hero:

    # class variabel
    jumlah = 0
    # variable private untuk class
    __privateJumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        # untuk membuat nilai dari variable jumlah bertambah jika menggunakan method ini
        Hero.jumlah += 1

        # variabel instance private
        self.__private = "private"
        # variabel instance protected
        self._protected = "protected"


lina = Hero("lina", 100)

print(lina.__dict__)
lina.__private = "test private"  # akan membuat variable baru
# akan merubah variable yang sudah ada dan tidak membuat variable baru
lina._protected = "test protected"
print(lina.__dict__)

# untuk melihat variable yang ada di dalam class
print(Hero.__dict__)

# tidak bisa di akses untuk variable private class
# print(Hero.__privateJumlah)
