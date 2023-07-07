import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()

# Membuka dan mengubah gambar menjadi format yang dapat digunakan oleh Tkinter
image = Image.open("resistor.png")
image = image.resize((300, 300))  # Mengubah ukuran gambar sesuai kebutuhan
photo = ImageTk.PhotoImage(image)

# Membuat label dan menampilkannya di jendela
label = tk.Label(window, image=photo)
label.pack()

window.mainloop()
