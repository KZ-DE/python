class Hero():
    __heroJumlah = 0
    __xpMax = 100
    
    def __init__(self, attpower:int, health:int, armor:int, *args:str) -> dict:
        '''set default artibrut'''
        self.__name = args
        self.__attpowerBase = attpower
        self.__healthBase = health
        self.__armorBase = armor
        self.__level = 1
        self.__xp = 0
        
        self.__attpowerMax = self.__attpowerBase*self.__level
        self.__healthMax = self.__healthBase*self.__level
        self.__armoraMax = self.__armorBase*self.__level
        
        Hero.__heroJumlah +=1
        
        pass
    

    def upXp(self, addxp=50, pembagi=1, jumlah=0):
        '''Setter upXp, attpower, healt, armor'''
        self.__xp += addxp
        if(self.__xp >= Hero.__xpMax):
            print(f"{self.__name[0]} Level Up.")
            self.__level += 1
            self.__xpMax += 50
            match jumlah:
                case 0:
                    self.__attpowerMax = self.__attpowerBase*self.__level
                    self.__healthMax = self.__healthBase*self.__level
                    self.__armoraMax = self.__armorBase*self.__level
                case 1:
                    self.__attpowerMax = self.__attpowerBase*self.__level*pembagi
                    self.__healthMax = self.__healthBase*self.__level
                    self.__armoraMax = self.__armorBase*self.__level
                case 2:
                    self.__attpowerMax = self.__attpowerBase*self.__level
                    self.__healthMax = self.__healthBase*self.__level*pembagi
                    self.__armoraMax = self.__armorBase*self.__level*pembagi
                case 3:
                    self.__attpowerMax = self.__attpowerBase*self.__level*pembagi
                    self.__healthMax = self.__healthBase*self.__level*pembagi
                    self.__armoraMax = self.__armorBase*self.__level
                case _:
                    print("Terjadi kesalahan, periksa fungsi upXp")
        pass
    
    def menyerang (self, addxp=50, pembagi=1, jumlah=0):
        '''setter xp up saat menyerang'''
        print(f"{self.__name[0]} Menyeranng")
        self.upXp(addxp, pembagi, jumlah)
        pass
    
    
    @property
    def info(self):
        '''method untuk melihat informasi hero'''
        print(f"""
              {self.__name[0]}: Level {self.__level}
              attack power : {self.__attpowerBase}/{self.__attpowerMax}
              helath : {self.__healthBase}/{self.__healthMax}
              armor : {self.__armorBase}/{self.__armoraMax}              
              """)

bejo = Hero(100,100,15,"Bejo")
ucup = Hero(125,20,7,"Ucup")
bejo.info
# ucup.info
bejo.menyerang(50,0.85, 2)
bejo.menyerang(50,0.85, 2)
bejo.info

            