# create a function that takes a list of numbers and returns the numpy array sorted in ascending order.
import numpy as np
def ascending_order(list1):
      arr = np.array(list1)
      return np.sort(arr)

list1 = [90,20,40,10,60,30,10]
result = ascending_order(list1)
print("Array in ascending order :",result)