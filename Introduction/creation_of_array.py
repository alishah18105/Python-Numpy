import numpy as np

#creating an array from a list

numpy_array = np.array([1,2,3,4,5])
print(numpy_array)

#creating an array with default value zeros
numpy_array_zeroes = np.zeros(3)
print(numpy_array_zeroes)

#creating an array with default value ones
numpy_array_ones = np.ones((2,3))
print(numpy_array_ones)

#creating an array with default value
numpy_array_full = np.full((2,3),7)
print(numpy_array_full)

#creating an array with sequence of numbers
numpy_array_arange = np.arange(1,10,1)
print(numpy_array_arange)

#creating an identity matrix
numpy_array_identity = np.eye(3)
print(numpy_array_identity)