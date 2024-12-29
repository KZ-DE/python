# method adalah sesuatu yang berkerja apa bila ada interkasi anatar user atau objek lainnya

class hero:
    jumblah = 0
    
    def __init__(self,input_healt:int,input_power:int, input_name:str,input_armor:int) -> str:
        self.nama = input_name
        self.power = input_power
        self.healt = input_healt
        self.armor = input_armor
        hero.jumblah +=1
        pass
    
    # 1. (void fuction jika di bahasa lainnya) (method fungcion jika di python) tanpa return
    def list(self):
        print(self.__dict__)
    
    # 2. method dengan argumen
    def healtup(self,up=100): # dalam ini contohnya menambah darah hero
        self.healt += up
    
    # 3. method dengan return
    def gethealt(self):
        return self.healt

hero1 = hero(100,40,"bejo",230)

hero1.list()
hero1.healtup()
hero1.list()
print(hero1.gethealt())
print(hero.jumblah)