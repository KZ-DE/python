class Hero():
    __jumlah = 0
    
    def __init__(self, name:str, health:int) -> dict:
        '''sebuah constructor'''
        self.name = name
        self.health = health
        Hero.__jumlah += 1
        pass
    
    # method getter untuk objek saja karena menggunakan self
    def get_jumlah(self):
        return Hero.__jumlah

    # method getter untuk class(tidak menggunakan self) <tida di saranakan> 
    def getJumlah():
        return Hero.__jumlah
    
    # method untuk objek dan class (method static [decolator]) <tida di saranakan> 
    @staticmethod # sebuah decolator
    def get_jumlah2 ():
        return Hero.__jumlah
    
    # method getter yang  jalan di class dan objek (menggunakan decolator) <di sarankan>
    @classmethod
    def get_jumlah3(clas): # untuk yang di dalam kurung bebas mau di isi apa karena untuk menggati nama class saat membuat method
        return clas.__jumlah
    
    
sudrun = Hero("Sudrun", 100)



### mengakses jumlah hero yang sudah di deklasi
# tidak bisa menggunakan seperti ini karena vaiable private
# print(Hero.__jumlah) 

# tidak bisa juga menggunakn method getter karena berlaku untk objek(yang berada di __init__ saja)
# print(Hero.get_jumlah())

# namun jika menggunakan objek maka akan jalan
print(f"method getter objek : {sudrun.get_jumlah()}")

# namun jika ingin jalan di class hero tinggal membuat method getter untuk class
print(f"method getter class : {Hero.getJumlah()}") # <tidak di sarankan>

bejo = Hero("Bejo", 200)

# mnggunakan static method yang jalan di objec dan class
print(f"Static method untuk Hero : {Hero.get_jumlah2()}")
print(f"Static method untuk Objec : {sudrun.get_jumlah2()}")

kz = Hero("Kz", 1000)

# menggunakan class method <di sarankan>
print(f"class method untuk class <di sarankan > : {Hero.get_jumlah3()}")
print(f"class method untuk objek <di sarankan > : {bejo.get_jumlah3()}")