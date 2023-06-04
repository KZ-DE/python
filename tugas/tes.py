import tkinter as tk
from tkinter import messagebox
import time
import csv


waktu = time.asctime()

try: 
    with open ('File.csv', mode='r') as file:
        print("file di temukan")
except:
    with open ("File.csv", mode="w", encoding='utf-8', newline="") as file:
        print("File tidak di temukan, membuat file baru")
        messagebox.showinfo(title="pemberitahuan", message="Membeuta file baru")
        isi = "WAKTU",'X1', 'Y1', 'X2', 'Y2'
        w = csv.writer(file)
        w.writerow(isi)

lebarKanvas = 200
lebarKotak = 50

app = tk.Tk()
# app.config(cursor= "")
kanvas = tk.Canvas()
 

kanvas.place(width=1000, height=1000)

alas = 100
tinggi = 50

xawal = 10
yawal = 5



# alas
kanvas.create_line(xawal,tinggi,alas,tinggi, width=2)
# tinggi
kanvas.create_line(xawal,yawal,xawal,tinggi, width=2)
# miring
kanvas.create_line(xawal, yawal, alas, tinggi, width=2)
with open ("File.csv", mode='a', encoding='utf-8', newline='') as file:
    isi = waktu, xawal, yawal, alas, tinggi
    a = csv.writer(file)
    a.writerow(isi)
app.mainloop()