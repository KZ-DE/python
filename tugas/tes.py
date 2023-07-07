import tkinter as tk
from tkinter import Label, Radiobutton, IntVar, Entry, Button

app = tk.Tk()
# membuat aplikasi tidak bisa di lebarkan
app.resizable(True, True) 

#judul aplikasi
app.title("Kalkulator resistor") 

# ukuran Lebar aplikasi jika pertama kali si buka
app.configure(width=1300, height=700)

# judul
judul = Label(app, text="KALKULATOR NILAI RESISTOR",font=["Helvetica", 14, "bold"])
judul.place(relx=0.5, rely=0.05, anchor="center")

def clear():
     in1.place_forget()
     in2.place_forget()
     in3.place_forget()
def hitung(z):
    try:
        inp1 = float(q1.get())
        inp2 = float(q2.get()) #r1
        inp3 = float(q3.get()) #r2
        
        match z:
            case 1:
                hasil = inp1 * inp3 / (inp2 + inp3)
                nilai.config(text=f"Hasilnya: {hasil:.2f} V")
                print("test")
            case 2:
                hasil = inp1 * ((inp2 + inp3) / inp2)
                nilai.config(text=f"Hasilnya: {hasil:.2f} V")
                print("test")
    except ValueError:
        nilai.config(text="Input tidak valid. Harap masukkan angka.")

def masukan():
    global q1, in1, q2, in2, q3, in3, calculate_button, nilai
    y = x.get()
    match y:
        case 1:
            clear()
            in1 = Label(app, text="Supply Voltage (Vs):")
            in2 = Label(app, text="Resistor R1 (ohm):")
            in3 = Label(app, text="Resistor R2 (ohm):")
            
        case 2:
            in1 = Label(app, text="Ouput Voltage (Vout):")
            in2 = Label(app, text="Resistor R1 (ohm):")
            in3 = Label(app, text="Resistor R2 (ohm):")
        
    in1.place(relx=0.1, rely= 0.1, anchor="w")
    q1 = Entry(app)
    q1.place(relx=0.1, rely= 0.15, anchor="w")
    
    in2.place(relx=0.1, rely= 0.2, anchor="w")
    q2 = Entry(app)
    q2.place(relx=0.1, rely= 0.25, anchor="w")   
         
    in3.place(relx=0.1, rely= 0.3, anchor="w")
    q3 = Entry(app)
    q3.place(relx=0.1, rely= 0.35, anchor="w")

    calculate_button = Button(app, text="Hitung", command=hitung)
    calculate_button.place(relx=0.1, rely= 0.4, anchor="w")

    nilai = Label(app)
    nilai.place(relx=0.1, rely= 0.45, anchor="w")
    import tkinter as tk 
from tkinter import Label, Radiobutton, IntVar, Entry, Button


app = tk.Tk() 

# variabel pada radio btn
btnR = IntVar()
jmlh = IntVar()

# membuat aplikasi tidak bisa di lebarkan
app.resizable(True, True) 

#judul aplikasi
app.title("Kalkulator resistor") 

# ukuran Lebar aplikasi jika pertama kali si buka
app.configure(width=1300, height=700)


# fungsi
def clearR():
    rangkaian.place_forget()

def clearD():
    dicari.place_forget()
    name1.place_forget()
    name2.place_forget()
    name3.place_forget()
    inp1.place_forget()
    inp2.place_forget()
    inp3.place_forget()
    hasil1.place_forget()


def hasilR():
    global rangkaian
    x = btnR.get()
    match x:
        case 1:
            clearR() 
            isi = "PEMBAGI TEGANGAN"
        case 2:
            clearR()
            isi = "PEMBAGI ARUS"
            
    selectionR = "TIPE RANGKAIAN : " + isi
    rangkaian = Label(app, text=selectionR)
    rangkaian.place(relx=0.035, rely=0.35, anchor="w")
    
def hasil():
    global dicari, name1, name2, name3, inp1, inp2, inp3, ket1, ket2, ket3, btn
    y = jmlh.get()
    match y :
        case 1:
            clearD()
            out = "TEGANGAN KELUARAN (V)"
            ket1 = "TENGANAN MASUKAN"
            ket2 = "HAMBATAN R1"
            ket3 = "HAMBATAN R2"
            inp1.place(relx=0.05, rely=0.5, anchor='w')
            inp2.place(relx=0.2, rely=0.5, anchor='w')
            inp3.place(relx=0.35, rely=0.5, anchor='w')
        case 2:
            clearD()
            out = "TENGNGAN SUPLAI (V)"
            ket1 = "TENGANAN KELUARAN"
            ket2 = "HAMBATAN R1"
            ket3 = "HAMBATAN R2"
            inp1.place(relx=0.05, rely=0.5, anchor='w')
            inp2.place(relx=0.2, rely=0.5, anchor='w')
            inp3.place(relx=0.35, rely=0.5, anchor='w')
        case 3:
            clearD()
            out = "ARUS (I)"
            ket1 = "TEGANGAN MASUKAN"
            ket2 = "HAMBATAN R1"
            ket3 = "HAMBATAN R2"
            inp1.place(relx=0.05, rely=0.5, anchor='w')
            inp2.place(relx=0.2, rely=0.5, anchor='w')
            inp3.place(relx=0.35, rely=0.5, anchor='w')
        case 4:
            clearD()
            out = "HAMBATAN R1 (ohm)"
            ket1 = "TENGANAN MASUKAN"
            ket2 = "TEGANGAN KELUARAN"
            ket3 = "HAMBATAN R2"
            inp1.place(relx=0.05, rely=0.5, anchor='w')
            inp2.place(relx=0.2, rely=0.5, anchor='w')
            inp3.place(relx=0.35, rely=0.5, anchor='w')
        case 5:
            clearD()
            out =  "HAMBATAN R2 (ohm)" 
            ket1 = "TENGANAN MASUKAN"
            ket2 = "TEGANGAN KELUARAN"
            ket3 = "HAMBATAN R1"
            inp1.place(relx=0.05, rely=0.5, anchor='w')
            inp2.place(relx=0.2, rely=0.5, anchor='w')
            inp3.place(relx=0.35, rely=0.5, anchor='w')
            
    output = "YANG DI CARI : " + out
    dicari = Label(app, text= output)
    dicari.place(relx=0.035, rely=0.38, anchor="w")
    name1 = Label(app, text=ket1)
    name1.place(relx=0.05, rely=0.47, anchor='w')
    name2 = Label(app, text=ket2)
    name2.place(relx=0.2, rely=0.47, anchor='w')
    name3 = Label(app, text=ket3)
    name3.place(relx=0.35, rely=0.47, anchor='w')
    btn = Button(app, text="HITUNG")
    btn.place(relx=0.23, rely=0.55, anchor="w")
   
   
def hitung(kondisi):
    global hasil1
    match kondisi:
        case 1:
            nialihasil = inp1.get() + inp2.get()
            print(nialihasil)
    hasil1 = Label(app, text="TEGANGAN KELUARAN (V)")
    hasil1.place(relx=0.1, rely=0.65, anchor="w")

judul = Label(app, text="KALKULATOR NILAI RESISTOR",font=["Helvetica", 14, "bold"])
judul.place(relx=0.5, rely=0.05, anchor="center")

# buton tipe rangkaian
R1 = Radiobutton(app,text="PEMBAGI TEGANGAN", variable=btnR, value=1, command=hasilR)
R1.place(relx=0.02, rely=0.18, anchor="w")

R2 = Radiobutton(app,text="PEMBAGI ARUS", variable=btnR, value=2, command=hasilR)
R2.place(relx=0.02, rely=0.23, anchor="w")

# indikator tipe rangkaian
rangkaian = Label(app)
dicari = Label(app)

# button jenis yang di hitung
J1 = Radiobutton(app,text="TEGANGAN KELUAR (V)", variable=jmlh, value=1, command=hasil)
J1.place(relx=0.2, rely=0.13, anchor="w")

J2 = Radiobutton(app,text="TEGANGAN SUPLAI (V)", variable=jmlh, value=2, command=hasil)
J2.place(relx=0.2, rely=0.17, anchor="w")

J3 = Radiobutton(app,text="ARUS (I)", variable=jmlh, value=3, command=hasil)
J3.place(relx=0.2, rely=0.21, anchor="w")

J4 = Radiobutton(app,text="HAMBATAN R1 (ohm)", variable=jmlh, value=4, command=hasil)
J4.place(relx=0.2, rely=0.25, anchor="w")

J4 = Radiobutton(app,text="HAMBATAN R2 (ohm)", variable=jmlh, value=5, command=hasil)
J4.place(relx=0.2, rely=0.29, anchor="w")

# input
name1 = Label()
name2 = Label()
name3 = Label()
btn = Button()
hasil1 = Label()
inp1 = Entry(app, justify="center")
inp2= Entry(app, justify="center")
inp3 = Entry(app, justify="center")





app.mainloop()

x = IntVar()

J1 = Radiobutton(app,text="TEGANGAN KELUAR (V)", variable=x, value=1, command=masukan)
J1.place(relx=0.25, rely=0.13, anchor="w")

J2 = Radiobutton(app,text="TEGANGAN SUPLAI (V)", variable=x, value=2, command=masukan)
J2.place(relx=0.25, rely=0.17, anchor="w")

J3 = Radiobutton(app,text="ARUS (I)", variable=x, value=3, command=masukan)
J3.place(relx=0.25, rely=0.21, anchor="w")

J4 = Radiobutton(app,text="HAMBATAN R1 (ohm)", variable=x, value=4, command=masukan)
J4.place(relx=0.25, rely=0.25, anchor="w")

J5 = Radiobutton(app,text="HAMBATAN R2 (ohm)", variable=x, value=5, command=masukan)
J5.place(relx=0.25, rely=0.29, anchor="w")

in1 = Label(app)
in2 = Label(app)
in3 = Label(app)

app.mainloop()
