# di gumakan utuk tipe data string
# untuk memisahkan sebuah string menjadi potongan-potongan yang lebih kecil berdasarkan suatu delimiter (pemisah). Fungsi ini mengembalikan daftar (list) dari potongan-potongan tersebut.

def string_to_array(string: str):
    return string.split()


print(string_to_array("hello word"))
