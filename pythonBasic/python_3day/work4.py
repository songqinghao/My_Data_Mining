"""
成员检测与标识号检测
    使用“in”和"not in"运算符来判断某个对象是否为序列的成员
    in:判断对象是否在序列（列表/字符串/元组/字典）存在返回true
    not in:和in相反
"""
# in
print("4" in "1234") #字符串4是否存在“1234”中
print(1 in (1,2,3,4)) #元组
print(1 in [1,2,3]) #列表
print("名字" in {"名字": "sqh"}) #字典

# not in
print(3 not in (1,2,9))

"""
运行结果：
True
True
True
True
True
"""