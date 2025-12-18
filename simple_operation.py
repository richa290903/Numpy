# create a numpy array from a python list and perform basic operations like addition,multiplication etc.

import numpy as np
list1 = [1, 2, 3, 4, 5]
array1 = np.array(list1)
print(array1)
list2 = [6, 7, 8, 9, 10]
array2 = np.array(list2)
print(array2)
print("Addition :",array1 + array2)
print("subtraction :",array1 - array2)
print("Multiplication:",array1 * array2)