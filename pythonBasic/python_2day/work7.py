"""
字典的操作方法
3.item
    将以列表的形式返回字典中的左右键值对
4.values
    将以列表的形式返回字典中的所有值
5.clear
    用于将字典清空
6.copy
    用于创建字典的副本，修改原字典对象不会影响副本
"""

d = {
    "名字": "sqh",
    "年龄": 18
}
r = d.items() # dict_items([('名字', 'sqh'), ('年龄', 18)])
r1 = d.values() # dict_values(['sqh', 18])
print(r)
print(r1)
d.clear()
print(len(d)) # 0
d2 = {
    "名字": "sqh",
    "年龄": 18
}
d3 = d2.copy()
del d2["名字"]
print(d2) # {'年龄': 18}
print(d3) # {'名字': 'sqh', '年龄': 18}

