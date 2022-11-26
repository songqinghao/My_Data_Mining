"""
创建Ndarray数组对象（1）
"""
import numpy as np

# 一维数组
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

# 元素类型相同str>flot>int
arr1 = np.array([1,2,3,4,5.6])
print(arr1)
print(type(arr1))

# 多维数组
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)
print(type(arr2))

# 最小维度为2
arr3 = np.array([1,2,3,4,5],ndmin=2)
print(arr3)

# dtype参数
arr4 = np.array([1,2,3,4],dtype='f')
print(arr4)

# 结构化数据类型
student = np.dtype([("name","S20"),("age","i4"),("marks","f4")])
arr5 = np.array([("sqh",18,99.9),("xxx",18,98.9)],dtype=student)
print(arr5)

