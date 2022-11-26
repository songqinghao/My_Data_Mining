"""
函数的定义：
    关键字def
    建议：函数默认参数尽量使用不可变对象
    因为可变对象会存储后续调用他的参数（可变对象就是容器类型的）
"""
def abc(a, b):
    print(a+b)

abc(100,200)

# 带默认参数
def bcd(a = 100,b=200):
    print(a+b)
bcd()

# 默认参数为容器，看看效果？
def cde(a=100,b = []):
    b.append(a)
    print(b)
cde()
cde(200)
cde(300)




