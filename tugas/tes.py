import tkinter as tk
from tkinter import messagebox

lebarKanvas = 200
lebarKotak = 50

app = tk.Tk()
# app.config(cursor= "")
kanvas = tk.Canvas(bg="red")
 

kanvas.place(width=200, height=lebarKanvas)

if lebarKotak > lebarKanvas :
    alert = messagebox.showwarning(title="warning!!!!!", message="ukuran bangun ruang melebihi ukuran kanvas" )
else:
    kotak = kanvas.create_rectangle(10,10,lebarKotak,20, width=2)

app.mainloop()