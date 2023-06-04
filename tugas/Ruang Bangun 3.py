# import libary
import tkinter as tk 
from tkinter import messagebox


app = tk.Tk() 
selected_option = tk.StringVar()

# ============ var posisi input ==========
kiri = 0.5
tengah = 0.65
kanan = 0.8

#  ==================== maxx ukuran objek ==============
xx1 = 10
yy1 = 275
xx2 = 1355
yy2 = 710


# membuat kanvas
kanvas = tk.Canvas(height=1000, width= 1400)
kanvas.pack()



#  ======== fungsi gambar =========
def xxx ():
    # segitiga
    hasilAlas = float(x.get()) + xx1
    
    # untuk persegi
    hasilGambarx = float(x.get()) + xx1
    hasilGambarx2 = float(x.get()) + yy1 
    
    # lingkaran
    llx = hasilGambarx * 2
    lly = hasilGambarx2 + hasilGambarx
    

    
    match selected_option.get():
        case "opsi 1":
            if(hasilGambarx2 > yy2):
                alert = messagebox.showwarning("peringatan", "ukuran gambar melebihi kanvas, tidak dapat menampilkan gambar")
            else:
                kotak = kanvas.create_rectangle(xx1,yy1, hasilGambarx, hasilGambarx2, width= 2)
        case "opsi 2":
            if(float(x.get()) + xx1 > xx2 or float(x2.get())+yy1 > yy2):
                alert = messagebox.showwarning("peringatan", "ukuran gambar melebihi kanvas, tidak dapat menampilkan gambar")
            else:
                pp = kanvas.create_rectangle(xx1,yy1,float(x.get())+ xx1, float(x2.get())+ yy1, width= 2) 
        case "opsi 3":
            if(hasilAlas > xx2 or float(x2.get()) > yy2):
                alert = messagebox.showwarning("peringatan", "ukuran gambar melebihi kanvas, tidak dapat menampilkan gambar")
            else:
                # alas
                kanvas.create_line(xx1,float(x2.get()) + yy1 ,hasilAlas,float(x2.get()) + yy1 , width=2)
                # tinggi
                kanvas.create_line(xx1,yy1,xx1,float(x2.get()) + yy1 , width=2)
                # miring
                kanvas.create_line(xx1, yy1, hasilAlas, float(x2.get()) + yy1 , width=2)
        case "opsi 4":
            if(lly > yy2):
                alert = messagebox.showwarning("peringatan", "ukuran gambar melebihi kanvas, tidak dapat menampilkan gambar")
            else:
                ling = kanvas.create_oval(xx1,yy1,llx,lly, width= 2)
                print(f"x = {llx}, dan y = {lly}")




#judul aplikasi
app.title("Ruang Bangun") 

# ukuran
app.configure() #lebar aplikasi jika pertama kali si buka

# ========fungsi=========
def clear(): 
    ''' hapus input'''
    lbl.place_forget()
    lbl2.place_forget()
    x.place_forget()
    btn1.place_forget()
    x2.place_forget()
    hasil_l.config(text="")



def pilihan(): 
    ''' hasil pilihan radio button'''
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
    ''' template '''
    global lbl, lbl2, x, x2, btn1
    match ruang:
        case 1:
            lbl = tk.Label(app, text=f"Masukan {o}")
            lbl.place(relx=tengah,rely=0.15, anchor="center")
        
            x= tk.Entry(app,)
            x.place(relx=tengah, rely=0.2, anchor="center")
            
            btn1 = tk.Button(app, text="Hitung", command=getentry)
            btn1.place(relx=tengah, rely=0.25, anchor="center")
        case 2:
            lbl = tk.Label(app, text=f"Masukan {o}")
            lbl.place(relx=kiri,rely=0.15, anchor="center")
            
            lbl2 = tk.Label(app, text=f"Masukan {p}")
            lbl2.place(relx=kanan, rely=0.15, anchor="center")
            
            x= tk.Entry(app,)
            x.place(relx=kiri, rely=0.2, anchor="center")
            
            x2= tk.Entry(app,)
            x2.place(relx=kanan, rely=0.2, anchor="center")
            
            btn1 = tk.Button(app, text="Hitung", command=getentry)
            btn1.place(relx=tengah, rely=0.25, anchor="center")
        case _:
            print("tidak ada")
            
def getentry():
    ''' Rumus - Rumus'''
    match selected_option.get(): 
        case "opsi 1":
            try:
                angka1 = float(x.get())
                luas = angka1*angka1
                kel = angka1*4
                hasil_l.config(text=f"Luas = {luas} Cm^2\nKeliling = {kel}")
                kanvas.delete("all")
                xxx()
            except: 
                hasil_l.config(text="Mohon masukan Bilangan")
        case "opsi 2":
            try:
                angka1 = float(x.get())
                angka2 = float(x2.get())
                luas = angka1*angka2
                kel = 2*(angka1 + angka1)
                hasil_l.config(text=f"Luas = {luas} Cm^2\nKeliling = {kel}")
                kanvas.delete("all")
                xxx()
            except: 
                hasil_l.config(text="Mohon masukan Bilangan")
        case "opsi 3":
            try:
                angka1 = float(x.get())
                angka2 = float(x2.get())
                luas = 0.5*angka1*angka2
                sm = ((angka1**2) + (angka2**2))/2
                kel = angka1 + angka2 + sm
                hasil_l.config(text=f"Luas = {luas} Cm^2\nKeliling = {kel}")
                kanvas.delete("all")
                xxx()
            except: 
                hasil_l.config(text="Mohon masukan Bilangan")
        case "opsi 4":
            try:
                angka1 = float(x.get())
                luas = 3.14*angka1*angka1
                kel = 2*3.14*angka1
                hasil_l.config(text=f"Luas = {luas} Cm^2\nKeliling = {kel}")
                kanvas.delete("all")
                xxx()
            except: 
                hasil_l.config(text="Mohon masukan Bilangan")
def home ():
    ''' Home '''
    judul.place(relx=0.15, rely=0.05, anchor="w")
    opsi.place(relx=0.15, rely=0.15, anchor="w")
    rb1.place(relx=0.15, rely=0.2, anchor="w")
    rb2.place(relx=0.15, rely=0.25, anchor="w")
    rb3.place(relx=0.15, rely=0.3, anchor="w")
    rb4.place(relx=0.15, rely=0.35, anchor="w")

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

home()

# ================mendeklarasikan tempat============
hasil_l = tk.Label(app, text="")
hasil_l.place(relx=0.65, rely=0.35, anchor="center")

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

