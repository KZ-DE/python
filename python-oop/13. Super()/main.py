# super() fungsi yang ada di python untuk mengakses init yang ada di super class

class Hero:
    '''Super class'''
    __var_private = None

    def __init__(self, name, health, armor) -> tuple[str, int, int]:
        self.__info = name
        self.__health = health
        self.__armor = armor
        pass

    # getter

    @property
    def info(self):
        '''Menampilkan informasi hero'''
        print(f"{self.__info}\n\t heatlh: {self.__health}\n\t armor: {self.__armor}")


class Figter(Hero):
    '''Sub class'''

    def __init__(self, name) -> tuple[str, int, int]:
        # ketika menggunakan hero maka harus di beri self pada init
        Hero.__init__(self, name, 100, 15)
    pass


class Mage(Hero):
    '''Sub class'''

    def __init__(self, name: str) -> tuple[str, int, int]:
        super().__init__(name, 80, 12)
    pass


bejo = Figter("Bejo")
ucup = Mage("Ucup")
sudrun = Mage("Sudrun")
print("Tidak menggubaka method super")
bejo.info
print("\nMenggunakan method super")
ucup.info
sudrun.info
