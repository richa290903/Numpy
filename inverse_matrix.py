# create a program that uses numpy to calculate the inverse of 2*2 matrix.
import numpy as np
arr = np.array([[1, 2],[3, 4]])
print("Matrix :\n", arr)
print("\nInverse of matrix:\n",np.linalg.inv(arr))
