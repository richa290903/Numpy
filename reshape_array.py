# Implement a program that generates a numpy array with numbers from 0 to 9 and reshapes it into a 3*3 matrix.
import numpy as np
arr = np.arange(10)
print("Reshape array :\n",arr[:9].reshape(3,3))