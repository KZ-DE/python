import tkinter as tk
from tkinter import Label, Entry, Button
from PIL import ImageTk, Image

app = tk.Tk()
# membuat aplikasi tidak bisa di lebarkan
app.resizable(True, True) 

#judul aplikasi
app.title("Kalkulator resistor") 

# ukuran Lebar aplikasi jika pertama kali si buka
app.configure(width=600, height=600)

# judul
judul = Label(app, text="KALKULATOR RESISTOR DIVIDER",font=["Helvetica", 14, "bold"])
judul.place(relx=0.5, rely=0.05, anchor="center")


def calculate():
    try:
        inp1 = float(vs_entry.get())
        inp2 = float(r1_entry.get())
        inp3 = float(r2_entry.get())
        
        nilai = inp1 * inp3 / (inp2 + inp3)
        hasil.config(text=f"Output Voltage: {nilai:.2f} V")
    except ValueError:
        hasil.config(text="Input tidak valid. Harap masukkan angka.")

vs_label = Label(app, text="Supply Voltage (Vs):")
vs_label.place(relx=0.34, rely= 0.1, anchor="w")
vs_entry = Entry(app)
vs_entry.place(relx=0.34, rely= 0.15, anchor="w")

r1_label = Label(app, text="Resistor R1 (ohm):")
r1_label.place(relx=0.34, rely= 0.2, anchor="w")
r1_entry = Entry(app)
r1_entry.place(relx=0.34, rely= 0.25, anchor="w")

r2_label = Label(app, text="Resistor R2 (ohm):")
r2_label.place(relx=0.34, rely= 0.3, anchor="w")
r2_entry = Entry(app)
r2_entry.place(relx=0.34, rely= 0.35, anchor="w")

btn = Button(app, text="Hitung", command=calculate)
btn.place(relx=0.34, rely= 0.4, anchor="w")

hasil = Label(app)
hasil.place(relx=0.34, rely= 0.45, anchor="w")

app.mainloop()
