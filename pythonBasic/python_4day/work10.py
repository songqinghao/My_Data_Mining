"""
for循环用于便利序列
    通过不适用下标的方式来对序列中的每一个元素进行访问
    列表/元组/字符串/字典/集合
    注意：1.字典输出键
         2.便利数字 range()
"""
a = [5,2,3]
for i in a:
    print(i)
print("=========")
b = "4234"
for i in b:
    print(i)
print("=========")
c = {
    "名字":"sqh",
    "年龄":22
}
for i in c:
    print(i)
print("=========")
d = [1, 8, 3, 4]
for i in range(len(d)):
    print(d[i])

