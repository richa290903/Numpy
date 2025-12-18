# Implement a program that generates a random numpy array and finds the maximum and minimum values.

import numpy as np
from numpy import random
arr = random.randint(100,size=(3,3))
print("Array :\n",arr)
print("Minimum :",np.min(arr))
print("Maximum :",np.max(arr))