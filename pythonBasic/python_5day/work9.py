"""
可变参数:
    *参数:最常见的变量名为args,自动手机所有未匹配的位置参数到一个tuple对象中，对象名args指向一个turple对象
"""
def abc(a,*args):
    print(a) # 5
    print(args) # args对应是一个空元组
abc(5)
abc(5,10)
abc(5,20)
abc(5,20,30,40) # 把未匹配的位置参数搞到tuple中
