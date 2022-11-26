"""
python的for循环语句
    1 遍历字典的键和值  d.items()
    2 range函数的步长
"""
d = {
    "名字": "sqh",
    "年龄": 18
}
for i in d.items():
    print(i)

# range()函数步长，range(0,4)->区间123
# range(0,6,2)->024
for i in range(0,6,2):
    print(i)