class Hero :
    # deklarasi variable
    jumblah = 0
    
    def __init__(self,Name:str, Healt:int, Power:int, Armor:int, Mana:int) -> str | dict :
        ''' fungsi yang berguna untuk template yang akan di gunakan oleh hero '''
        
        self.name = Name
        self.healt = Healt
        self.power = Power
        self.armor = Armor
        self.mana = Mana
        
        Hero.jumblah += 1
        
        pass
    
    def list(self)-> dict:
        '''untuk melihat informasi lengakap hero'''
        
        print(self.__dict__)
        
    def serang(self,lawan:str)->str:
        '''fungsi menyeraang'''
        
        power = 2*((self.power+lawan.armor)/lawan.armor)
        atpower = int(power)
        global sisa_mana
        sisa_mana = self.mana - atpower
        
        print(f"{self.name} menyerang {lawan.name}")
        print(f"sisa mana bejo = {sisa_mana}")
        
        lawan.diserang(self)
        lawan.Healt(self)
        # self.update()
        lawan.update()

    def diserang(self,lawan:str)->str:
        ''' fungsi di serang'''
        
        power = 2*((lawan.power+self.armor)/self.armor)
        atpower = int(power)
        
        print(f"{self.name} diserang {lawan.name} dengan attack power {atpower}")
    
    def Healt(self,lawan)->str:
        '''untuk melihat sisa darah'''
        
        power = 2*((self.power+lawan.armor)/lawan.armor)
        atpower = int(power)
        global sisa_darah
        sisa_darah = lawan.healt - atpower
        
        print(f"sisa darah dari {self.name} {sisa_darah}")
        
    def update(self):
        '''update info hero'''
        self.healt = sisa_darah
        # self.mana = sisa_mana
        print(self.list())
    

bejo = Hero("bejo", 200, 140, 90, 82)
sudrun = Hero("sudrun", 140, 175, 170, 25)


bejo.list()
sudrun.list()
print("\n")
bejo.serang(sudrun)