"""
isinstance()用来判断一个对象是否是一个已知的类型
    isinstance()返回值为bool类型
语法：
isinstance(对象,对象类型)
类型：int,float,bool,str,list,tuple,set,dict
"""
a = 123
b = "123"
c = (1,2,3)
d = [1, 2, 3]
print(isinstance(a, int))
print(isinstance(b, str))
print(isinstance(c, tuple))
print(isinstance(d, list))

"""
运行结果：
True
True
True
True
"""