# numpy 的运算
# numpy的运算针对的是数组中的每个元素，如果是两个维度不同的数组进行运算，会进行广播
# 广播时，需要低维度数组形状能和高维度数组后面的形状相等能相等
# 如(2, 3, 2) 和 (3, 2)才能进行运算，进行广播
# 特殊 (3, 1) 这种 和 (3, )这种可以相运算 数组维度相同 其中一个轴为1
# 广播就是自我复制，复制成高维度的维度

import numpy as np

a = np.array([1, 2, 3])
b = np.array([2, 3, 4])

# numpy数组的加减乘除是对应的每一位数的加减乘除
print(a + b) # [3,5,7]

c = a < b # 比较也是一样  对应的每一位去比较
c.astype(np.int) # 将布尔值数组转成int保存

np.all(c)

np.arange(3).reshape(3, 1) + np.arange(3) # 特殊 (3, 1) 这种 和 (3, )这种可以相运算

np.arange(24).reshape(2, 3, 4) + np.random.randint(3, size=(2,1,4))


a = np.random.normal(size=(2000,))

np.mean(a) # 求一个数组的均值

np.std(a) # 求一个数组的方差

np.sum(a) # 求一个数组的和

#axis 轴 数组从外层括号到内存依次是 0 1 2 3.。。轴

a.shape
c = np.expand_dims(a, 0) # 在a的0轴增加一个维度
c.shape

d = np.squeeze(c) # 把多余的维度都压缩掉 比如 [[1]]两个括号但是只有一个元素，外层回呗压缩掉

np.max(c,axis=0) #找出0轴上对应位置的数中最大的数，组成新的数组 不加axis找出所有数中最大的数

np.maximum(c, d) # 将两个数组相比，对应的每个数比较 留下大的数，适用广播机制
np.maximum(c, 10) # 将10广播，再与C对比

a.argmax(axis=0) #在0轴进行比较，返回最大值所在的index

np.sort(a, axis=0) # 把数组按0轴进行排序
np.argsort(a, axis=0) #在0轴上这个数排第几大 升序