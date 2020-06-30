# 编写一个函数，接收n个参数，求这n个参数的和

def sumNum(*n):
    res = 0
    for i in n:
        res += i
    print(res)


sumNum(1, 21, 3, 15, 1, 8, 16)

# c = lambda *n: for i in n: yield i + i

# print(c(1, 21, 3, 15, 1, 8, 16))
