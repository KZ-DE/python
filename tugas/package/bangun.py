# import libary
import tkinter as tk 


app = tk.Tk() 
selected_option = tk.StringVar()


# membuat aplikasi tidak bisa di lebarkan
app.resizable(False, False) 

#judul aplikasi
app.title("Ruang Bangun") 

# ukuran
app.configure(width=600, height=600) #lebar aplikasi jika pertama kali si buka

# ========fungsi=========
def clear(): 
    lbl.place_forget()
    lbl2.place_forget()
    x.place_forget()
    btn1.place_forget()
    x2.place_forget()
    hasil_l.config(text="")


def pilihan(): 
    if selected_option.get() == "opsi 1":
        clear()
        hitung(1, "lebar", "")
        hasil_l.place_slaves()
    elif selected_option.get() == "opsi 2":
        clear()
        hitung(2, "panjang", "lebar")
    elif selected_option.get() == "opsi 3":
        clear()
        hitung(2, "alas", "tinggi") 
    elif selected_option.get() == "opsi 4":
        clear()
        hitung(1, "jari-jari", "")         
    
def hitung(ruang, o, p):
    global lbl, lbl2, x, x2, btn1
    match ruang:
        case 1:
            lbl = tk.Label(app, text=f"Masukan {o}")
            lbl.place(relx=0.5,rely=0.46, anchor="center")
        
            x= tk.Entry(app,)
            x.place(relx=0.5, rely=0.5, anchor="center")
            
            btn1 = tk.Button(app, text="Hitung", command=getentry)
            btn1.place(relx=0.5, rely=0.55, anchor="center")
        case 2:
            lbl = tk.Label(app, text=f"Masukan {o}")
            lbl.place(relx=0.3,rely=0.46, anchor="center")
            
            lbl2 = tk.Label(app, text=f"Masukan {p}")
            lbl2.place(relx=0.7,rely=0.46, anchor="center")
            
            x= tk.Entry(app,)
            x.place(relx=0.3, rely=0.5, anchor="center")
            
            x2= tk.Entry(app,)
            x2.place(relx=0.7, rely=0.5, anchor="center")
            
            btn1 = tk.Button(app, text="Hitung", command=getentry)
            btn1.place(relx=0.5, rely=0.6, anchor="center")
        case _:
            print("tidak ada")
            
def getentry():
    
    match selected_option.get(): 
        case "opsi 1":
            try:
                angka1 = float(x.get())
                luas = angka1*angka1
                kel = angka1*4
                hasil_l.config(text=f"Luas = {luas} Cm^2\nKeliling = {kel}")
            except: 
                hasil_l.config(text="Mohon masukan Bilangan")
        case "opsi 2":
            try:
                angka1 = float(x.get())
                angka2 = float(x2.get())
                luas = angka1*angka2
                kel = 2*(angka1 + angka1)
                hasil_l.config(text=f"Luas = {luas} Cm^2\nKeliling = {kel}")
            except: 
                hasil_l.config(text="Mohon masukan Bilangan")
        case "opsi 3":
            try:
                angka1 = float(x.get())
                angka2 = float(x2.get())
                luas = 0.5*angka1*angka2
                sm = 0.5*angka1
                kel = angka1 + sm**2
                hasil_l.config(text=f"Luas = {luas} Cm^2\nKeliling = {kel}")
            except: 
                hasil_l.config(text="Mohon masukan Bilangan")
        case "opsi 4":
            try:
                angka1 = float(x.get())
                luas = 3.14*angka1*angka1
                kel = 2*3.14*angka1
                hasil_l.config(text=f"Luas = {luas} Cm^2\nKeliling = {kel}")
            except: 
                hasil_l.config(text="Mohon masukan Bilangan")

# ===============Membuat alat=================
# judul halaman
judul = tk.Label(text="Kalkulator Ruang Bangun",relief="solid")
judul.config(font=("popins", 15))

# radio buton
opsi = tk.Label(text="pilih bangun yang akan di hitung!!")
rb1 = tk.Radiobutton(app, text="Persegi", variable=selected_option, value="opsi 1", command=pilihan)
rb2 = tk.Radiobutton(app, text="Persegi Panjang", variable=selected_option, value="opsi 2", command= pilihan)
rb3 = tk.Radiobutton(app, text="Segitiga", variable=selected_option, value="opsi 3", command=pilihan)
rb4 = tk.Radiobutton(app, text="Lingkaran", variable=selected_option, value="opsi 4", command=pilihan)

# ==============Menampilkan alat=================
judul.place(relx=0.25, rely=0.05, anchor="w")

opsi.place(relx=0.25, rely=0.15, anchor="w")
rb1.place(relx=0.25, rely=0.2, anchor="w")
rb2.place(relx=0.25, rely=0.25, anchor="w")
rb3.place(relx=0.25, rely=0.3, anchor="w")
rb4.place(relx=0.25, rely=0.35, anchor="w")
# ================mendeklarasikan tempat============
hasil_l = tk.Label(app, text="")
hasil_l.place(relx=0.5, rely=0.7, anchor="center")

lbl = tk.Label()
lbl2 = tk.Label()
x = tk.Label()
x2 = tk.Label()
btn1 = tk.Label()



app.mainloop() # untuk menjalankan app



# catatan
'''
untuk command dengn fungsi jangan menggunakan tanda kurung
'''