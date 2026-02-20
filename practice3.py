import numpy as np

# 1D array
arr = np.array([1,2,3,4,5])
print("arr:", arr)
print("Type:", type(arr))
print("Dimensions:", arr.ndim)
print()

# Using tuple to create numpy array
arr1 = np.array((1,2,3,4))
print("arr1:", arr1)
print("Type:", type(arr1))
print("Dimensions:", arr1.ndim)
print()

# 0-D array (scalar)
arr2 = np.array(42)
print("arr2:", arr2)
print("Type:", type(arr2))
print("Dimensions:", arr2.ndim)
print()

# 1-D array
arr3 = np.array([1,2,3,4,5,6])
print("arr3:", arr3)
print("Dimensions:", arr3.ndim)
print()

# 2-D array
arr4 = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])
print("arr4:\n", arr4)
print("Type:", type(arr4))
print("Dimensions:", arr4.ndim)
print("Shape:", arr4.shape)
print("Itemsize:", arr4.itemsize)
print("Size:", arr4.size)
print()

# 3-D array
arr5 = np.array([
    [[1,2,3],
     [4,5,6]],
    
    [[7,8,9],
     [10,11,12]]
])
print("arr5:\n", arr5)
print("Dimensions:", arr5.ndim)
print("Shape:", arr5.shape)
print("Size:", arr5.size)