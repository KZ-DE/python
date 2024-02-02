def positive_sum(arr):
    hasil = 0
    for i in arr:
        if i < 0:
            hasil += 0
        else:
            hasil += i
    return hasil


positive_sum([])

# sub adalah sebuah fungsi unttuk menjumlahkan semua nilai yang di masukan, tidak peduli itu di dalam list maupun tuple

# format sum sebagai berikut
# sum(iterable, start=0)
# iterable: Sebuah iterable seperti daftar, tupel, atau set yang elemennya akan dijumlahkan.
# start: Nilai awal yang akan ditambahkan ke total. Default-nya adalah 0.


def sederhana(arr):
    return sum(x for x in arr if x > 0)


sederhana([1, 23, 4, -190])
