import numpy as np

a = np.array((1, 2, 3, 4))  # a = np.array([1, 2, 3, 4])

print(a.shape)  # shape numpy数组的形状

type(a)  # numpy.ndarray numpy数组


b = np.array([
    [
        [2, 3, 4], [1, 2, 3]
    ],

    [
        [1, 2, 3], [4, 5, 6]
    ],

    [
        [1, 2, 3], [4, 5, 6]
    ]
])

b.shape  # (3, 2, 3) 最外层有两个逗号  内一层，有1个逗号，最内层有2个逗号


c = np.zeros((3, 4)) # 生成一个三行4列的 0 填充的数组   ones就是用1填充

d = np.zeros_like(b) # 生成一个用0 填充的像b一样的np数组

e = np.random.random((3, 4)) # 生成一个三行四列的 随机数数组

f = np.random.normal(size=(3, 4)) # 通过正态分布生成一个随机数填充的三行四列数组

g = np.random.uniform(size=(2,2)) # 生成一个0-1均匀分布的随机数填充的两行两列的数组
 
h = np.arange(0.1, 1, 0.1) #从0.1开始 一直加到 1 每一次加0.1，取头不取尾 生成一个数组  

i = np.linspace(0.1, 10, 10) # 在0.1 - 10之间  均匀取十个数 首尾都取 组成一个数组 将endpoint设为False则不取尾