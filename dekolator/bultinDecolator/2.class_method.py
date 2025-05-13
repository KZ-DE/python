class Karyawan:
    jumlah_karyawan = 0

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        Karyawan.jumlah_karyawan += 1

    @classmethod
    def dari_string(cls, string_karyawan):
        nama, gaji = string_karyawan.split('-')
        return cls(nama, int(gaji))

    @classmethod
    def tampilkan_jumlah_karyawan(cls):
        print(f"Jumlah karyawan: {cls.jumlah_karyawan}")


# Membuat instance karyawan menggunakan constructor biasa
karyawan1 = Karyawan("Budi", 5000)

# Membuat instance karyawan menggunakan factory method dari_string
karyawan2 = Karyawan.dari_string("Ani-6000")

# Memanggil classmethod untuk menampilkan jumlah karyawan
Karyawan.tampilkan_jumlah_karyawan()  # Output: Jumlah karyawan: 2
