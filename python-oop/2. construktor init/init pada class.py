# 1. membuat tamlate yang benar
class hero:
    '''sebuah tamplate'''
    # 2. mendeklarasikan template objek dan memberi template atribut
    # mendeklarasikan init
    # init akan di eksekusi terlebih dahulu setelah progam di buat

    def __init__(self, input_name: str, input_power: int, input_healt: int, input_armor: int) -> str:
        # selft adalah pengganti dari nama class
        self.name = input_name
        self.healt = input_healt
        self.armor = input_armor
        self.power = input_power

        pass


# 2. membuat objek dan memberi artribut objel
# nilai dari tamplate tidak boleh kosong
hero1 = hero("bejo", 30, 300, 120)
hero2 = hero("king z", 120, 200, 50)


def isi(name: object) -> dict | str:
    x = name.__dict__

    return x


print(isi(hero1))
print(isi(hero2))
print(hero1.name)
print(hero2.armor)
