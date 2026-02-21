# Data types in Numpy
""""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""

# get the data type of an array object
import numpy as np
arr=np.array([1,2,3,4])
print(arr.dtype)

#get the data type of an array conatining strings 
arr2=np.array(['apple','banana','cherry'])
print(arr.dtype)

#create an array with data type string
arr3=np.array([1,2,3,4],dtype='S')
print(arr3)
print(arr3.dtype)

#create an array with data type 4 integer 
arr4=np.array([1,2,3,4,5],dtype='i4')
print(arr4)
print(arr4.dtype)

#change data type from float to integer by using 'i' as parameter value

import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

#Change data type from float to integer by using int as parameter value:
import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)
#change data type from integer to boolean 

arr5=np.array([1,0,3,4])
newarr=arr5.astype(bool)
print(newarr)
print(newarr.dtype)



