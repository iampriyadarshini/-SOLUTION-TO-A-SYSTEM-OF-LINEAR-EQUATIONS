#Program to find the solution for the given linear equations.
#Developed by: Mohamed Riyaz Ahamed
#RegisterNumber: 24900085
import numpy as np

A = np.array([[1, -3], [3, 1]])  # Coefficient matrix
B = np.array([0, 10])  # Constants on the right-hand side

solution = np.linalg.solve(A, B)

print(solution)
