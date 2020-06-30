# loop = 0
# while 10 > loop:
#     print(loop)
#     loop += 1

# count = 0
# while True:
#     print('number is {}'.format(count))
#     count += 1

#     if count < 3:
#         continue
#     else:
#         break
import random

role_dict = {'1': '刘备', '2': '关羽', '3': '张飞'}
fist_dict = {1: '石头', 2: '剪刀', 3: '布'}

role_win = 0
pc_win = 0
ping = 0

role_num = input('请选择角色：1.刘备，2.关羽，3.张飞')
role = role_dict[role_num]
print('您选择的角色是：{}'.format(role))

while True:
    fist_num = int(input('请出拳：1.剪刀，2.石头，3.布'))
    fist = fist_dict[fist_num]
    print('{}出拳{}'.format(role, fist))

    pc_fist_num = random.randint(1, 3)
    pc_fist = fist_dict[pc_fist_num]
    print('pc出拳{}'.format(pc_fist))

    res = fist_num - pc_fist_num

    if res in (-2, 1):
        role_win += 1
        print('{}赢了'.format(role))
    elif res in (-1, 2):
        pc_win += 1
        print('pc赢了')
    else:
        ping += 1
        print('平局')
    choice = input('需要继续猜拳么？ y/n')
    if choice == 'y':
        continue
    else:
        break

print('{}赢了{}次，PC赢了{}次，平局{}次'.format(role, role_win, pc_win, ping))
