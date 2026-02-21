import  numpy as np

arr=np.array([1,2,3,4,5])

print(arr[1:5])

# slice element from index 4 to the end of the array

arr2=np.array([1,2,3,4,5,6,7])
print(arr2[4:])

# slice elements from the begining to index 4

arr3=np.array([1,2,3,4,5,6])
print(arr3[:4])

#slice from the index 3 from the end to index 1 from the end

arr4=np.array([1,2,3,4,5,6,7])
print(arr4[-3:-1])

#return every other elements from index 1 to index 5

arr5=np.array([1,2,3,4,5,6,7])
print(arr5[1:5:2])

#return every other elements from the entire array
print(arr5[::2])