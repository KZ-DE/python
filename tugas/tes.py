import tkinter as tk
from tkinter import ttk, Canvas
app = tk.Tk()
canvas = tk.Canvas()
canvas.pack()
canvas.create_oval(50,50,200,200,outline="black", fill="red" )
canvas.delete("all")

app.mainloop()