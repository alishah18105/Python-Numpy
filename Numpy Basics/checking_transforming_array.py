import numpy as np

array1 = np.array([1,"Ali",3])
array2 = np.array([[1,2,3],[4,3.5,6]])
array3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

#To check the size of an array:
print("Size of the array:", array1.size)
print("Size of the array:", array2.size)
print("Size of the array:", array3.size)

#To check the dimension of any array:
print("Dimension of the array:", array1.ndim)
print("Dimension of the array:", array2.ndim)
print("Dimension of the array:", array3.ndim)

#To check the shape of an array:
print("Shape of the array:", array1.shape)
print("Shape of the array:", array2.shape)
print("Shape of the array:", array3.shape)

#To check the data type of an array:
print("Data type of the array:", array1.dtype)
print("Data type of the array:", array2.dtype)
print("Data type of the array:", array3.dtype)

#To change the data type of an array:
array5 = np.array([1.2, 3.5, 7.1, 8.3])
print("Data type of the array:", array5.dtype)

new_array = array5.astype(int)
print("Data type of the new array:", new_array.dtype)