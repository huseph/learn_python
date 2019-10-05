def ShowMaxFactor(num):
    ans = num // 2
    while ans > 1:
        if num % ans == 0:
            print('{}的最大公约数是{}'.format(num,ans))
            break
        ans -= 1
    else:
        print('{}是素数!'.format(num))

num = int(input('请输入一个数:'))
ShowMaxFactor(num)
