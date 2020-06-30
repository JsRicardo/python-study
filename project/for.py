# 字符串 元组 列表 字典都可以遍历

# ll = ['12', 112, 22222, 'asdadad']

# for it in ll:
#     print(it)

# # enumerate 把ll变成 [(0, '12'), (1, 112), (2, 22222), (5, 'asdadad')]
# for index, name in enumerate(ll):
#     print("%d, %s" % (index, name))

# s = 'qwertyuio'

# # reversed 倒序
# for it in reversed(s):
#     print(it)


# t = (1, 23, 45, 'sda', True)

# for it in t:
#     print(it)

# # 遍历字典时，it为字典的key
# dic = {'sdad': 'dssss', True: 123, 132: False}

# for it in dic:
#     print(it, '--', dic[it])

# 求 π 的值
# 梦特卡洛计算 π 值
# 正方形的长为 2 面积为 2 * 2
# 原型半径为 1， 面积为 πr²

# 所以 正方形和原型面积的比例为 4 / π
from random import random

loop = 100000  # 丢小球次数
hits = 0.0  # 落在扇形里的次数

for i in range(0, loop + 1):
    x, y = random(), random()  # 记录小球的落点
    dist = pow(x ** 2 + y ** 2, 0.5)  # 小球落点距离圆心的距离
    if dist < 1.0:  # 如果距离小于1，则落在扇形内
        hits = hits + 1
pi = 4 * (hits/loop)

print(pi)
