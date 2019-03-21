# 声明一个int_demo的方法
def int_demo():
    # 声明aint变量 并赋值 1
    aint = 1
    # 打印 aint的值
    print(aint)


# 声明一个min的方法 参数有两个
def min(aint, bint):
    # 打印 aint 的值
    print(aint)
    # 打印 bint 的值
    print(bint)
    #
    return aint - bint

def afloat_demo():
    # 声明afloat变量 ， 并赋值 1.8
    afloat = 1.8
    # 打印 afloat 的值
    print(afloat)
    # 打印 afloat 的类型， type(afloat): 获取afloat的类型
    print(type(afloat))


if __name__ == '__main__':
    afloat_demo()
    # int_demo()
    # result = min(4, 2)
    # print(result)
    pass
    pass
