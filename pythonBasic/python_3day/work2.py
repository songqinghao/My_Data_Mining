"""
字典的操作方法之popitem函数+setdefault函数
    popitem函数：用于从字典中删除最后一项，并以元组的形式返回该项对应的键和值
    setdefault函数：用于设置键的默认值
                若在字典中改建以及存在则忽略设置
"""
a = {
    "名字": "sqh",
    "年龄": 18
}
r = a.popitem()
print(r)
print(a)

a1 = {
    "名字": "sqh",
    "年龄": 18
}
a1.setdefault("技能", "C++")
print(a1)

"""
运行结果
('年龄', 18)
{'名字': 'sqh'}
{'名字': 'sqh', '年龄': 18, '技能': 'C++'}
"""