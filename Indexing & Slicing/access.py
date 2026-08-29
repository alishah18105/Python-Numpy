import numpy as np

#Accesing  elements frm an array using indexing:

array_1 = np.array([1,2,3,4,5])
array_2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(array_1[0])
print(array_1[-1])

print(array_2[0,2])
print(array_2[-1,0])