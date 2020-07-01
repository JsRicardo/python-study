# -*- coding: utf-8 -*-

import numpy as np

mat = np.mat('1,2,3; 4,5,6') #传入字符串 用分号隔开，代表一个数组，生成一个矩阵

re = mat.reshape(2, 3) #将原数组的数字按照原来的顺序，重新生成一个2 * 3 的矩阵

mat.shape
n=mat.T # 转置 将原矩阵的轴进行旋转
n.shape

# 矩阵乘法

# 一个 3 * 2 的矩阵 和一个 2 * 3的矩阵相乘 
# mat的第一行和n的每一列对应位置的数相乘在相加 生成结果的第一行
# mat的第二行和n的每一列对应位置的数相乘在相加 生成结果的第二行
mat * n 

# 如果两个数据不是numpy 矩阵 可以用matmul进行矩阵相乘

a = np.random.randint(12, size=(3, 4))
c = np.random.randint(12, size=(4, 3))

np.matmul(a, c)