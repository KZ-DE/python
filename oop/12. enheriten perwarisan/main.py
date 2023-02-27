# perwarisan init pada class

class Hero:
    '''super class'''
    def __init__(self, *args) -> dict[str, int]:
        self.__name = args
        self.__armor = None
        pass
    
    # getter
    @property
    def info(self):
        print (f"Nama: {self.__name[0]}\n\t Health: {self.__name[1]}")

class figter(Hero): # tanda di dalam kurung merupakan tanda bahwa class ini mewarisi init yang ada di class hero
    '''sub class dari class Hero'''
    pass

class Tank(Hero):
    '''sub class dari class Hero'''
    pass



bejo = figter("bejo", 100)
bejo.info
sudrun = Tank("sudrun", 500)
sudrun.info