import numpy as np

#To check whether the aray contains nan (not a number):
arr = np.array([2,4,np.nan,5,6,np.nan,7,8])
print(np.isnan(arr))

#To replace a nan with any default value:
cleaned_value =  np.nan_to_num(arr,nan=0)
print(cleaned_value)