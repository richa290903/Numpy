# write a function that takes a numpy array and returns a new array with all elemets squared.
import numpy as np
def square(arr):
      return np.square(arr)

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Original array :\n",arr)
result = square(arr)

print("Squared array :\n",result)
