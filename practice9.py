import numpy as np

# print the shape of a 2-D array

arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)

arr2=np.array([1,2,3,4,5],ndmin=5)
print(arr2)
print('shape of array :',arr2.shape)

