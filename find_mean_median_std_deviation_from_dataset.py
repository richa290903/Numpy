# write a python program that uses numpy to find the mean,median and standard deviation of a dataset.
import numpy as np
arr = np.loadtxt("dataset.csv",skiprows=1)
mean_val = np.mean(arr)
print("Mean :",mean_val)
print("Median :",np.median(arr))
print("standard deviation :",np.std(arr))