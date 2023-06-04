from scipy.optimize import fsolve
import numpy as np

# Panjang segmen pada setiap sendi
l1 = 5
l2 = 8
l3 = 6

# Koordinat efektor akhir pada setiap kaki
x = 12
y = 6
z = 8

# Fungsi persamaan kinematik
def kinematic_equations(angles, x, y, z):
    theta1, theta2, theta3 = angles
    
    f = [
        l2 * np.cos(theta1) + l3 * np.cos(theta1 + theta2) - x,
        l2 * np.sin(theta1) + l3 * np.sin(theta1 + theta2) - y,
        l1 - z + l2 * np.sin(theta2) + l3 * np.sin(theta2 + theta3)
    ]
    
    return f

# Menghitung sudut sendi pada setiap kaki
def inverse_kinematics(x, y, z):
    initial_guess = [0, 0, 0]  # Tebakan awal untuk sudut sendi
    angles = fsolve(kinematic_equations, initial_guess, args=(x, y, z))
    
    return angles

# Menghitung sudut sendi pada setiap kaki
theta1_1, theta2_1, theta3_1 = inverse_kinematics(x, y, z)
theta1_2, theta2_2, theta3_2 = inverse_kinematics(x, y, z)
theta1_3, theta2_3, theta3_3 = inverse_kinematics(x, y, z)
theta1_4, theta2_4, theta3_4 = inverse_kinematics(x, y, z)

# Menampilkan sudut sendi pada setiap kaki
print("Kaki 1: Sudut sendi 1 =", np.degrees(theta1_1), "Sudut sendi 2 =", np.degrees(theta2_1), "Sudut sendi 3 =", np.degrees(theta3_1))
print("Kaki 2: Sudut sendi 1 =", np.degrees(theta1_2), "Sudut sendi 2 =", np.degrees(theta2_2), "Sudut sendi 3 =", np.degrees(theta3_2))
print("Kaki 3: Sudut sendi 1 =", np.degrees(theta1_3), "Sudut sendi 2 =", np.degrees(theta2_3), "Sudut sendi 3 =", np.degrees(theta3_3))
print("Kaki 4: Sudut sendi 1 =", np.degrees(theta1_4), "Sudut sendi 2 =", np.degrees(theta2_4), "Sudut sendi 3 =", np.degrees(theta3_4))