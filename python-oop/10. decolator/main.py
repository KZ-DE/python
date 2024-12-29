# getter dan setter

class Hero():
    def __init__(self, name: str, healt: int, armor: int) -> dict:
        self.__name = name
        self.__health = healt
        self.__armor = armor
        # tidak usah di tulis ketika memkasai method decolator
        self.info = "Name {} :\n\tHealth {}".format(self.__name, self.__health)
        # tidak usah di tulis ketika memkasai method
        self.__info = "Name {} :\n\tHealth {}".format(
            self.__name, self.__health)
        pass

    # getter method menggunakan cara yang biasa <tidak di sarankan>
    def getinfo(self):
        return self.__info

    # menggunakan decolator properti <disarankan>
    @property  # mengubah method menjadi variable
    def getinfo2(self):
        return "Name {} :\n\tHealth {}".format(self.__name, self.__health)

    # deklarasi property untuk armor
    @property
    def armor(self):
        pass

    # membuat method untuk getter
    @armor.getter
    def getArmor(self):
        return self.__armor

    # membuat method untuk setter
    @armor.setter
    def setArmor(self, input):
        self.__armor = input

    # membuat method untuk deletter
    @armor.deleter
    def delArmor(self):
        self.__armor = None
        print("armor di delete")


print("Merubah info\n")
sudrun = Hero("sudrun", 100, 10)
# tanpa private variable maka akan mudah di rubah
print(sudrun.info)
sudrun.info = "info"
print(sudrun.info)

# getter method biasa
print(f"\ncara biasa :\n{sudrun.getinfo()}")

# menggunakan decolator property <di sarankan>
print(f"\nmenggunakan decolator :\n{sudrun.getinfo2}")

# jika tida menggunakan decolator getter maka saat di cek menggunaka dict akan keliatan semua data yang adas
print(sudrun.__dict__)


# setter dan getter dengan property
print("\ngetter dan setter menggunakan method property\n")
print(sudrun.getArmor)
print(sudrun.__dict__)
sudrun.setArmor = 30
print(sudrun.__dict__)
del sudrun.delArmor
print(sudrun.__dict__)
