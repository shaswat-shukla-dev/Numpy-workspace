import numpy as np
array1=np.array([[10,20,40],[50,4,9],[6,8,9]])
print(array1.min())
print(array1.min(axis=0))
print(array1.min(axis=1))