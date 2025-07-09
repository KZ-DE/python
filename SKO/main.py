import numpy as np
from scipy.linalg import solve_continuous_are

# Matriks sistem
A = np.array([[0, 1],
              [0, -1]])
B = np.array([[0],
              [1]])
Q = np.array([[1, 0],
              [0, 1]])
R = np.array([[1]])

# Menyelesaikan persamaan Riccati
P = solve_continuous_are(A, B, Q, R)

# Menghitung gain feedback optimal K
K = np.linalg.inv(R) @ B.T @ P

print("Solusi Riccati matrix P:\n", P)
print("State feedback gain K:\n", K)
