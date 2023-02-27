import random
import string

def pk (panjang = 6 )->str:
    hasil_pk = "".join(random.choice(string.ascii_letters)for i in range(panjang))
    
    return hasil_pk
