import numpy as np

#To check whether the array contains positive or negative infinite value
arr = np.array([2,4,5,np.inf, 100, 12, -np.inf])
print(np.isinf(arr))

#To replace infinite value:
cleaned_value = np.nan_to_num(arr,posinf=1000, neginf=-1000)

print(cleaned_value)

