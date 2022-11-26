"""
数据类型第二弹: bool()可以把其他类型转换成True和False
1.容器类型转bool
    容器类型:字符串/列表/元组/字典/集合
    非容器类型:数字类型/bool类型
    容器为空:返回False否则返回True
2.数据类型转bool类型
    int类型中，0为False
    float类型中，0.0为False
"""
a = "" # 字符串
b = [] # 空列表
c = () # 空元组
d = {} # 空字典
e = set() # 空集合
print(bool(a),bool(b),bool(c),bool(d),bool(e))
print("========================")
f = 0
g = 0.0
print(bool(f),bool(g))
"""
运行结果：
False False False False False
========================
False False

"""


