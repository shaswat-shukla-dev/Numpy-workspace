import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(arr[0,2])

#accesing element in 3d

arr2=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr2[0,1,2])
print(arr2[1,1,0])
 # negative indexing

arr3=np.array([[1,2,3],[4,5,6]])
print(arr3[1,-3])
print(arr3[-1,-2])