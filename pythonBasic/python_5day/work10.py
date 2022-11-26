"""
可变参数:
    **参数:最常见的变量名为kwargs，看到该变量名，一眼就知道变量指向一个dict对象
    自动洲际所有未匹配的关键字参数到一个dict对象中，变量名kwargs指向了此dict对象
"""
def abc(a,**kwargs):
    print(a) # 5
    print(kwargs) # kwargs对应是一个dict字典

abc(5, x = 200, y = 300)

"""
运行结果：
5
{'x': 200, 'y': 300}
"""