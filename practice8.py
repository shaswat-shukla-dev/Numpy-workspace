# difference between copy and view

import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.copy()
arr[0]=42
print(arr)
print(x)

#make a view , change the original array and display both arrays
arr2=np.array([1,2,3,4,5])
x=arr2.view()
arr2[0]=42
print(arr2)
print(x)

#make a view , change the view and display both arrays
arr3=np.array([1,2,3,4,5,6])
x=arr3.view()
x[0]=31
print(arr3)
print(x)

#print the value of the base attribute to check if an array owns its data or not 

arr4=np.array([1,2,3,4,5])
x=arr4.copy()
y=arr4.view()
print(x.base)
print(y.base)