import numpy as np

arr_1 = np.array([1,3,5])
arr_2 = np.array([2,4,6])
hstack_array = np.hstack((arr_1,arr_2)) #horizontal stack
vstack_array = np.vstack((arr_1,arr_2)) #vertical stack

print(hstack_array)
print(vstack_array)