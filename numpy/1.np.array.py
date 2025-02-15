import numpy as np

arr_1_dimensi: list = np.array([1, 2, 3, 4, 5])
arr_2_dimensi: list = np.array(object=[[1, 2, 3, 4],
                                       [1, 2, 3, 4]])

# menambahkan tipe data
arr_ndimensi = np.array([1, 2, 3], dtype=np.int16)

# memberi ukuran string (pada tulisan word tanda ! akan tidak di ekesusi)
contoh_arr = np.array(["hello", "world!!"], dtype="<U5")


def cekArray(arr: list) -> None:
    print(arr)
    # cek type
    print(f"memiliki type : {type(arr)}")
    # cek dimensi
    print(f"dengan type {arr.ndim}")
    # cek ukuran array
    print(f"dengan ukuran : {arr.shape}")
    # cek tipe data
    print(f"tipe datanya adalah : {arr.dtype}")


if __name__ == "__main__":
    cekArray(arr_1_dimensi)
    cekArray(arr_2_dimensi)
    cekArray(arr_ndimensi)
    cekArray(contoh_arr)
