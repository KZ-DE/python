import tkinter as tk


main_window = tk.Tk()

### class yang ada di tkinter
# 1.
label1 = tk.Label(main_window, text = "label1")
label2 = tk.Label(main_window, text = "label2")
# yang ada di dalam tanda kurung adalah atribut dari fungsi tabel yang ada di dalam clas tkinter
'''
main window adalah posisi dari tabel
'''
# 2.
tombol1 = tk.Button(main_window, text = "tombol1")
tombol2 = tk.Button(main_window, text = "tombol2")

# 3.
judul = tk.BOTTOM
# method positioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

tk.BEVEL # contoh variabel constans
tk.BooleanVar #contoh class
tk.getdouble # variabel dari class
tk.image_types # fungsi
tk.mainloop # method

# method menampilkan GUI
main_window.mainloop()

'''
jika di awali huruf besar maka class
jika tidak maka itu method
'''