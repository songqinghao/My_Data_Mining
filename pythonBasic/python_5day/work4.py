"""
循环语句中的关键字：
    break 语句可以跳出for和while的循环体
    continue 语句跳过这一轮
"""
for i in "python":
    if(i=='t'):
        break
    print(i)

for i in "python":
    if(i=='t'):
        continue
    print(i)

a = 0
while a<6:
    a += 1
    if a == 3:
        continue
    print(a)