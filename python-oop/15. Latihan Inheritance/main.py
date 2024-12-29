class Hero:
    def __init__(self, name:str) -> dict:
        self.__name = name
        self.__healtpoll = [0,100,200,300,400,500]
        self.__armorpoll = [0,5,9,13,17,20]
        self.__attpowerpoll = [0,100,130,165,210,250]
        self.__xp = 1
        self.__level = 1
        self.__maxxppoll = [0, 100, 150, 230, 370, 410]
        self.__xpUp = 10
        pass
    
    @property
    def info(self):
        print(f"""
            {self.__name}
            level : {self.__level}
            health : {self.__health}
            armor : {self.__armor}
            attpower : {self.__attpower}
            xp : {self.__xp}/{self.__maxxp}
              """)
        pass
    
    @property
    def level_up (self):
        '''>>> set_level = int'''
        pass
    
    
    @property
    def gainxp(self):
        '''>>> gainxp = int'''
    
    @property
    def get_level(self):
        '''menampilkan level hero'''
        pass

    @property
    def get_xp(self):
        '''menampilkan xp hero'''
        pass
    
    @property
    def get_maxxp(self):
        '''menampilkan max xp per level'''
        pass
    
    @property
    def xpUp(self):
        pass



    '''Getter'''
    @get_level.getter
    def get_level(self):
        return self.__level
    
    @get_xp.getter
    def get_xp(self):
        return self.__xp

    @get_maxxp.getter
    def get_maxxp(self):
        pass
    
    @xpUp.getter
    def xpUp(self):
        return self.__xpUp
    


    '''Setter'''
    @level_up.setter
    def level_up (self, nilai:int):
        '''static method'''
        self.__level = nilai
        self.__health = self.__healtpoll[self.get_level]
        self.__armor = self.__armorpoll[self.get_level]
        self.__attpower = self.__attpowerpoll[self.get_level]
        self.__xp = self.gainxp
        self.__maxxp = self.__maxxppoll[self.get_level]
        pass
    
    
    @gainxp.setter
    def gainxp(self, nilai):
        self.__xp = nilai
        if (self.__xp >= self.__maxxp):
            xp = self.__xp%self.__maxxp
            levelUp = self.__xp//self.__maxxp + 1
            self.level_up = levelUp
            print(f"{self.__name} naik level {levelUp}")
            
        

    
    def serang(self, musuh):
        print(f"{self.__name} menyerang {musuh.__dict__['_Hero__name']}")
        upXp = self.xpUp
        self.gainxp = upXp + 10
        
    def diserang(self):
        print(self.__dict__)
    
    

class Figter(Hero):
    def __init__(self, name: str) -> dict:
        super().__init__(name)
        self.level_up = 1

bejo = Figter("Bejo")
ucup = Figter("Ucup")
bejo.serang(ucup)
ucup.serang(bejo)
ucup.serang(bejo)
ucup.serang(bejo)
ucup.serang(bejo)
ucup.info









       