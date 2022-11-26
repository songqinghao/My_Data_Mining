"""
    判断某两个对象是否相用，用is和not is运算符进行运算
    is：如果两对象相同则返回true
    not is：和is相反

    数字/字符串/元组表面相等那么就是一样（不可变数据类型）
    列表/集合/字典表面一样实际却是不一样（可变的数据类型）
"""
a = "sqh"
b = "sqh"
c = "hqs"
print(a is b)
print(a is c)

a1 = {1,2,3}
b1 = {1,2,3}
print(a1 is b1)
