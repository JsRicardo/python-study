
# import os  # 系统包

# dirs = os.getcwd()  # 文件路径
# os.listdir

# print(os.listdir())  # 文件目录

# print(os.path.abspath('range.py'))  # 获取文件的绝对路径

txtfile = open('files/desc.txt', encoding='utf-8')  # 打开文件,中文要加上utf-8

# read 读文件   seek 将光标移动到指定位置  tell 光标的位置

# print(txtfile)

txtfile.read()

txtfile.close()  # 打开文件之后 文件会从存储状态变为占用状态，其他程序无法使用  所以打开  -> 操作 之后需要关闭文件

