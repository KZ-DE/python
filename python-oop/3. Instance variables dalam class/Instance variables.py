# cara melihat semua artribut yang di gunakan oleh objek yang ada di dalam class

# 1. membuat tamlate yang benar
class hero:
    '''sebuah tamplate ntuk membuat objek yang di dalam class'''
    # class variabel
    jumblah = 0
    
    def __init__(self,input_name:str, input_power:int, input_healt:int, input_armor:int) -> str: 
        # selft adalah pengganti dari nama class
        self.name = input_name
        self.healt = input_healt
        self.armor = input_armor
        self.power = input_power
        hero.jumblah += 1 # selalu di tulis --> nama_class.valriable
        
        pass

## 2. membuat objek dan memberi artribut objel
# nilai dari tamplate tidak boleh kosong
hero1 = hero("bejo",30,300,120) 
hero2 = hero("king z",120,200,50)

def isi(name:str)-> dict | str:
    '''untuk melihat informasi hero yang ada di dalam nya'''
    x = name.__dict__
    
    return x


print(isi(hero1))
print(isi(hero2))
print(hero1.name)
print(hero2.armor)
print()
print(hero.jumblah)

