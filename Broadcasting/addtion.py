import numpy as np

#addtion of 1D to 2D array

arr_1D = np.array([2,4,6])
arr_2D = np.array([[2,4,6],[3,4,7]])

new_arr = arr_2D + arr_1D
print(new_arr)