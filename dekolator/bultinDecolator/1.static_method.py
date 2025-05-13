'''
tatic method adalah metode yang terikat dengan kelas tetapi tidak secara otomatis menerima instance kelas (self)
atau kelas itu sendiri (cls) sebagai argumen pertama. 
Metode statis mirip dengan fungsi biasa yang didefinisikan di dalam kelas.
'''


class kendaraan():
    def __init__(self, merk, tipe):
        self.merk = merk
        self.tipe = tipe
        self.jumlah = 10
        print(
            f"membuat kendaraan dengan merk {self.merk} dan bertipe {self.tipe}")

    def hitung(self, x: int) -> int:
        return self.jumlah * x

    @staticmethod
    # tidak tergantung pada dekolator atau self
    def jumlah_kendaran(x: int) -> int:
        return x


# membuat objek untuk class
yamaha = kendaraan("yamaha", "mobil")
# static method bisa di panggil tanpa memerlukan objek
jumlah = yamaha.jumlah_kendaran(10) * yamaha.hitung(10)
print(jumlah)
