import numpy as np

a = np.array((3, 4))

a.shape

# reshape不会修改原数组

b = a.reshape(4, 3) # 将a中的所有元素扁平化 再将扁平化后的数组修改为四行三列的数组

c = a.reshape(-1, 6) # -1代表不确定这一位应该填几，他会根据6 去计算这个-1 应该是几

d = a.reshape(-1) #将a数组拉平成一维数组

e = a.flatten() # 将a数组拉平成一维数组

f = np.arange(12).reshape(1,3,-1) #从[0 -12)中 以1为步长 区数，生成一个一维数组，再修改维度为（1， 3 -1） 

f.resize(3, 4) # resize也是改变维度，会改变原数组


# 在py中数组切片返回的值，和原数组指向的不是同一个内存空间，在np中切片返回的数组和原数组则是指向的同一个内存空间