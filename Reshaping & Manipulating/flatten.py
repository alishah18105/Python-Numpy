import numpy as np

#These methods are used to convert an 2D or 3D array to 1D array

#.flatten(): It make changes in the copy of original array
# .ravel(): It make changes in the original array

array_1 = np.array([[1,2,3],[4,5,6]])
array_2 = np.array([[1,2],[3,4],[5,6]])

print(array_1.flatten())
print(array_2.ravel())