def move(man,step):         #未报到数的向列表后面移动
    for i in range(1,step):
        item = man.pop(0)
        man.append(item)


def play(man,step,rest):
    print('总共有%s个人，每报到%s的人自杀，最后剩余%s个人'%(man,step,rest))
    '''
        man :总人数
        step:自杀数字
        rest:剩余人数
    '''
    man = [i for i in range(1,man+1)]       #初始化列表
    while rest < len(man):
        move(man,step)
        print('Kill',man.pop(0))
    return man

print('约瑟夫问题求解')
f = input('开始求解请输入:B/b')
while f.lower() == 'b':
    man = input('请输入总人数：')
    step = input('请输入自杀间隔数：')
    rest = input('请输入最后剩余数：')
    servive = play(int(man),int(step),int(rest))
    print('最后生存的人是：',servive)
    f = input('开始求解请输入:B/b')
   
