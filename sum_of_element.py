# Given a list of numbers, create a numpy array and find the sum and product of its elements.
import numpy as np
list1 = [10, 50, 63, 82, 26]
arr = np.array(list1)

print("Sum of elements :",np.sum(arr))
print("Product of elements:",np.prod(arr))