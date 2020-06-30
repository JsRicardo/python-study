# 99乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('{} * {} = {} '.format(i, j, i * j), end='')
#     print()

# 冒泡排序
# ll = [1, 2, 53, 22, 211, 623]

# for i in range(0, len(ll)):
#     for j in range(i + 1, len(ll)):
#         if ll[j] < ll[i]:
#             ll[j], ll[i] = ll[i], ll[j]

# print(ll)


# 1 2 3 4能组成多少个互不相同且无重复数字的三位数

# res = []
# temp = 0

# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if i != j and i != k and j != k:
#                 temp = i * 100 + j * 10 + k
#                 res.append(temp)

# print(res, len(res))

# 直角三角形
# for i in range(6):
#     print('*' * i, end='')
#     print()
# 等腰三角形
# for i in range(1, 6):
#     for j in range(6 - i):
#         print(' ', end='')
#     print('* ' * i, end='')
#     print()
