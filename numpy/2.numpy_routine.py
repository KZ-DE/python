import numpy as np

# zeros
arr_nol: list = np.zeros((2, 3))

# ones
arr_ones: list = np.ones((2, 3))

# arra nilai acak
arr_kosong: list = np.empty([2, 3])

# array range
arr_range = np.arange(0, 10, 1)

# array linspace (array yang membuat list untuk nilai rentang awal hingga akhir dengan jumlah tertentu)
arr_lin = np.linspace(0, 1, 5)

# array eye (membuat matrix identitas)
matrix_identitas = np.eye(5)  # ukuran 5x5

# array full (membuat matrix dengan nilai yang sama semua)
arr_full = np.full((2, 3), 12)

# array random rand (membuat array acak antara nilai 0 hingga 1)
arr_acak = np.random.rand(2, 3)

# array random randit (nilai acak di atara nilai yang sudah di tentukan)
arr_randit = np.random.randint(0, 3, (2, 3))

if __name__ == "__main__":
    print(f"array nol :\n{arr_nol}\n")
    print(f"array one :\n{arr_ones}\n")
    print(f"array kosong :\n{arr_kosong}\n")
    print(f"array range :\n{arr_range}\n")
    print(f"array linspace :\n{arr_lin}\n")
    print(f"matrix identitas :\n{matrix_identitas}\n")
    print(f"matrix full :\n{arr_full}\n")
    print(f"array acak rand :\n{arr_acak}\n")
    print(f"array acak randit :\n{arr_randit}\n")
