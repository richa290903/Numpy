# implement a function that takes a numpy array and returns and transpose of the array.

import numpy as np
def get_transpose(arr):
    return np.transpose(arr)  

matrix = np.array([[1, 2, 3],[4, 5, 6]])
print("Original Matrix:\n", matrix)
print("Transpose:\n", get_transpose(matrix))
