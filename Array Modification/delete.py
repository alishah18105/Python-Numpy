import numpy as np

#Deleting or removing elements from an array:

arr = np.array([2,4,6,8,10,12])
new_arr = np.delete(arr,0,axis=None)
print(new_arr)

#Deleting from a 2D array:
arr_2d = np.array([[2,4,6],[1,3,5]])
new_arr_2d = np.delete(arr_2d,0,axis = 0)
print(new_arr_2d)