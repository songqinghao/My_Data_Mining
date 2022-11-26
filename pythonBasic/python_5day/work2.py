"""
python的双重for循环
"""
a = [1,2,3,[10,20,30],[50,60,70]]
for i in a:
    print(i)
    # 如果是列表类型
    if isinstance(i,list):
        for j in i:
            print(j)
