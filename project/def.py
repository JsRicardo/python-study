# 函数

def happy_new_year(name):
    print('新年快乐，{}总'.format(name))


happy_new_year('王')
happy_new_year('周')
happy_new_year('吴')


def sumNum(x, y=10):  # 形参可以有默认值，但是有默认值的形参要放在最后面
    print(x + y)


sumNum(10)


def sss(x, *y):  # *y代表接收剩余参数 y就是一个元组(123, 456, 789)
    res = x
    for i in y:
        res += i
    print(res)


sss(1, 123, 456, 789)


def aaa(a, b, c):
    print(a + b + c)


args = (1, 2, 3)
aaa(*args)  # 传参解构 前面加*
