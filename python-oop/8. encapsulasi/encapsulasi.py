# setter dan getter
# setter untuk mengubah nilai private variable
# getter untuk mengambil data private variable

class Hero():
    def __init__(self, name: str, health: int, attpower: int) -> dict:
        '''sebuah construktor dari class Hero'''
        # penggunaan ( __ ) agar variable private agar tidak bisa di ganti dan juga tida dapat di lihat nilainya
        # untuk mengatset nilainya dan juga menseting nilainya maka harus membuat method getter dan setter
        self.__name = name
        self.__health = health
        self.__atkPower = attpower
        pass

    # method getter (untuk mengakses nilai dari sebuah variable private)
    def get_name(self) -> str:
        return self.__name

    def get_healt(self) -> str:
        return self.__health

    # method setter
    def diserang(self, nilai: int):
        '''Mengurangi nilai dari darah'''
        self.__health -= nilai


# mendeklarasikan hero
bejo = Hero("Bejo", 100, 13)
print(bejo.__dict__)

# untuk melihat isi dari variable private tinggal mengunakan method yang sudah di buat
print(bejo.get_name())
print(bejo.get_healt())
# sedangkan jika langsung menggunakan variablenya maka akan eror
# print(bejo.__name)

# method setter untuk menseting nilai ari variable private
bejo.diserang(10)
print(bejo.__dict__)

# walaupun di coba untuk mengubah nilai di luar class
bejo.__health = 100
print(bejo.__health)
# walaupun hasilnya berubah namun hal tersebut tidak mengubah value dari variable asli yang mana hanya dapat di tampulkan menggunakan method getter

print(bejo.__dict__)


print(bejo.get_healt())
