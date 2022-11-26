"""
解包拆包
"""
s = "123"
l = [1, 2, 3]
c = {
    "a":"sqh",
    "b":"18",
    "c":"C++"
}
# 个数得相等
# 字典解包时，名字得和键一一对应
def abc(a,b,c):
    print(a)
    print(b)
    print(c)

abc(*s)

abc(*c) # 取出键

abc(**c) # 取出值
