import numpy as np

array1 = np.array([10,20,40,5])
array2 = np.array([12,45,89,56])
print(np.concatenate((array1, array2)))
array3=array1+array2
print(array3)
array4=np.stack((array1,array2))
print(array4)
array5=np.vstack((array1,array2))
print(array5)


'''
np.concatenate((array1, array2))

👉 Combines arrays end-to-end

🔍 Dry Run:
[10, 20, 40, 5] + [12, 45, 89, 56]
✅ Output:
[10 20 40  5 12 45 89 56]
'''

'''
array3 = array1 + array2

👉 This is NOT concatenation ❗
👉 This is element-wise addition

🔍 Dry Run (index by index):
Index	array1	array2	Sum
0	10	12	22
1	20	45	65
2	40	89	129
3	5	56	61
✅ Result:
[22, 65, 129, 61]
'''

'''
What np.stack() does

👉 It joins arrays along a new axis
👉 Think: “put arrays on top of each other”

🔍 Dry Run

We stack them like rows:

[
 [10, 20, 40, 5],
 [12, 45, 89, 56]
]
'''


