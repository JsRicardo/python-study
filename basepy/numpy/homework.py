# -*- coding: utf-8 -*-

import numpy as np

# 对二维数组的每一行求和 （1轴）

a = np.arange(16).reshape(4, 4) + 1


result = []
for one in a:
    res = 0
    for two in one:
        res = res + two
    result.append(res)
    

res = np.sum(a, 1)

# 矩阵
c = np.mat('1,2,3,4;,5,6,7,8;,9,10,11,12;13,14,15,16')
d = np.mat('1;1;1;1')
c * d
