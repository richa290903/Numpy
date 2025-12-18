# Given a list of lists, create a 2D numpy array and find the sumof elements  in each row and column.
import numpy as np
list1 = [1,2,3,4,5,6,7,8]
arr = np.reshape(list1,(2,4))
print("Original array :\n",arr)
print("Sum of each row :",np.sum(arr,axis=1))
print("Sum of each Column :",np.sum(arr,axis=0))