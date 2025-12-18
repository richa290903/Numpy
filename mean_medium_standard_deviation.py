# Generate a numpy array of random numbers and calculate its mean,median and standard deviation.
import numpy as np
from numpy import random
arr = random.randint(50,size=(5))
print("Array :",arr)
print("Mean :",np.mean(arr))
print("Median :",np.median(arr))
print("Standard Deviation:", np.std(arr))