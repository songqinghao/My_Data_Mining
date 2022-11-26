"""
    函数中各个参数排列位置的注意事项
    1.可变参数必须定义在普通参数以及默认值参数的后面
    2.函数定义时，二者同时存在，一定需要将*args放在**kwargs前面
    def abc(普通参数,默认值参数name="sqh",*参数,**参数)
"""
def abc(a,name="sqh",*args,**kwargs):
    print(a)
    print(name)
    print(args)
    print(kwargs)

abc(100,"张三",1,2,3,4,x=100,y=300)