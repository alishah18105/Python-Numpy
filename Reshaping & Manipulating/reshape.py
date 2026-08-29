import numpy as np

#reshape is used to convert an 1D array to 2D array or a 2D array to 3D array. Original array is not affected.
array_1 = np.array([1,2,3,4,5,6])
print(array_1.reshape(3,2))