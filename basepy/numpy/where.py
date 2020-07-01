# -*- coding: utf-8 -*-

import numpy as np

"""
np.where(condition, x, y) 
不传xy的情况 返回满足condition的索引，有几个维度就返回几个数组，分别代表相应的维度
满足条件的位置用x填充
不满足的用y填充
"""
a = np.random.randint(12, size=(3, 4)) # 需要返回两个数组来表示维度
np.where(a < 4) # 返回两个数组，第一个数组时0轴的index 第二个数组是1轴的index
"""
(array([0, 0, 0, 1, 1, 2, 2], dtype=int64),
 array([0, 2, 3, 1, 3, 1, 2], dtype=int64))

所以a[0][0] a[0][2] a[0][3]...小于4

a[np.where(a < 4)] 这样就可以拿出相应的值
"""

np.argwhere(a < 4)

"""
array([[0, 0],
       [0, 2],
       [0, 3],
       [1, 1],
       [1, 3],
       [2, 1],
       [2, 2]], dtype=int64)

argwhere返回的也是序号

但是他是这样认的

a[0][0]  a[0][2]... 小于4
是横向认的
"""

np.extract(a<4, a) # 这样是返回的元素