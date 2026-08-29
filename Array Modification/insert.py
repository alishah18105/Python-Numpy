import numpy as np

#Python arrays are of fixed sized. You have to create a new array to add elements.

arr = np.array([10,25,45,50,65])
new_arr = np.insert(arr,2,30,axis=0) #axis = 0 to add in row & 1 to add in column
print(new_arr)

arr_2D = np.array([[1,2],[5,6]])
new_arr_2D = np.insert(arr_2D,1,[3,4],axis=0)
print(new_arr_2D)