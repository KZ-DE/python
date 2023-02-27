import os
import csv
from . import Search



def update():
    sistemOperasi = os.name
    match sistemOperasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
    Search.search()
    user = input("pilih uratan yang akan di update : ")
    