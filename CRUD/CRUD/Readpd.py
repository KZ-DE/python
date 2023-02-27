import pandas as pd


def Reat_pd():
    # fungsi names agar tampilan read agar rapi
    df = pd.read_csv('D:/belajar bahasa progam/belajar_python/CRUD/Database/Database.csv', names=[''] )
    # fungsi .to_string agar menampilkan angka ke tipe string
    print(df.to_string())