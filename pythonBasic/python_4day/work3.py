"""
数据类型+数据强制转换
type():输出变量的类型
str():转换成string，任何类型都可以转换成str
# 数字类型之间可以相互转换，只有字符串可以转换成数字类型并且字符串必须为纯数字，否则无法转换
int():转换成int
float():
"""

a = 1
print(a, "数据类型为：", type(a)) # int
b = {1, 2, 3, 4}
print(b, "数据类型为：", type(b)) # 列表
c = (1, 2, 3, 4, 5)
print(c, "数据类型为：", type(c)) # 元组

str_a = str(a)
print(str_a, "数据类型为：",type(str_a))

print("===============================")
a = 123
float_a = float(123)
print(float_a, "数据类型为：", type(float_a))
b = 123.6 # 将小数点直接舍去
int_b = int(b)
print(int_b, "数据类型为：", type(int_b))

c = True # bool值在python中也属于数字
int_c = int(c)
print(int_c, "数据类型为：",type(int_c))

d = "1234" # 如果不是全数字则会报错
int_d = int(d)
print(int_d, "数据类型为：", type(int_d))

e = "12345.441"
# 用int来接会报错
# int_e = int(e)
# print(int_e, "数据类型为：",type(int_e))

float_e = float(e)
print(float_e, "数据类型为：", type(float_e))

