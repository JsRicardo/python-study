# try except

# try:
#     strs = 'ABCDEFGHIJQLMNOPQRSTUVWXYZ'
#     num = eval(input('请输入一个数字'))
#     print(strs[num])
# except NameError as na:
#     print('类型错误，请输入一个数字', na)
# except:
#     print('你搞错了！')

# try except 必须同时出现  保留字 else finally可选

# try:
# 试着执行的语句
# except:
# 出错了执行
# else:
# 没报错执行
# finally:
# 出没出错都会执行

# raise可以用于抛出异常

try:
    strs = 'ABCDEFGHIJQLMNOPQRSTUVWXYZ'
    num = eval(input('请输入一个数字'))
    if num > 27:
        raise NameError
    print(strs[num])
except NameError as na:
    print('类型错误，请输入一个数字', na)
except:
    print('你搞错了！')
