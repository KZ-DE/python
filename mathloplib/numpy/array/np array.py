import numpy as np

# bisa menggunakan tanda kurung 
a1 = np.array((2,1,3))
print(a1)
print(type(a1))

# bisa juga menggunakan kurung persegi
print("\n########################\n")
a1 = np.array([2,1,3])
print(a1)
print(type(a1))

# array 1D
print("\narray 1D")
a1 = np.array([2,1,3])
print(a1)

# array 2D
print("\narray 2D")
a2 = np.array([[2,1,3],[1,3,1]])
print(a2)

# array 3D
print("\narray 3D")
a3 = np.array([[2,3,4],[2,4,6],[3,4,7]])
print(a3)

# memeriksa dimensi dari aray
print("\nmemeriksa dimensi dari aray")
print(a1.ndim)
print(a2.ndim)
print(a3.ndim)


# catatan
''''
1. jumlah kurung kotak bisa di gunakan untuk patokan membuat aray yang lebih dari 1 dimensi
'''