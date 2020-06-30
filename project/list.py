# list 列表
# 有序
# 可变

ll = [0, 2, 3, 4, 5, [2, 'adas', 'sda']]

ll.append('dasd')  # 增加一个元素到列表的末尾，只能一次只能增加一个
ll.insert(3, '第四个')  # 指定位置添加一个元素

ll.pop()  # 默认删除最后一个元素

ll.pop(0)  # 删除第0个元素

print(ll)
