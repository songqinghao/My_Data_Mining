"""
集合添加元素
    1.add()往集合中添加元素
    2.update将集合进行合并
"""

a = {1, 2, 3} # {1, 2, 3, 4}
# a.add(4)
# a.add("sqh") # {1, 2, 3, 'sqh'}
# a.add((1,2,3)) # {1, 2, 3, (1, 2, 3)}
b = {"w","a","b"}
a.update(b) # {'a', 1, 2, 3, 'w', 'b'}
print(a)

