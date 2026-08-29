import numpy as np

#Joining two arrays

arr1 = np.array([1,3,5])
arr2 = np.array([2,4,6])

new_arr = np.concatenate((arr1,arr2))
print(new_arr)
