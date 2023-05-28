import tkinter as tk
from tkinter import messagebox

lebarKanvas = 200
lebarKotak = 50

app = tk.Tk()
# app.config(cursor= "")
kanvas = tk.Canvas()
 

kanvas.place(width=1000, height=1000)

alas = 550
tinggi = 200

xawal = 10
yawal = 100



# alas
kanvas.create_line(xawal,tinggi,alas,tinggi, width=2)
# tinggi
kanvas.create_line(xawal,yawal,xawal,tinggi, width=2)
# miring
kanvas.create_line(xawal, yawal, alas, tinggi, width=2)

app.mainloop()