class Hero:
    def __init__(self, name:str, health:int) -> dict[str,int]:
        self.__name = name
        self.__health = health
        pass
    
    def info(self, tipe, armor):
        print(
            f"{self. __name}\n\t Tipe: {tipe}\n\t Health: {self.__health}\n\t Armor: {armor}"
              )
        pass
    
    
class Figter(Hero):
    def __init__(self, name: str) -> dict[str, int]:
        super().__init__(name, 100)

        #overread method 
        self.__armor = 20
        pass
    
    def info(self):
        return super().info('Figter', self.__armor)



    
        
        
bejo = Figter('Bejo')
bejo.info()
print(bejo.__dict__)
