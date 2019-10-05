def hanoi(n, fro, ass, tar):
    global summ
    if n == 1:
        print('%c --> %c' %(fro, tar))
        summ += 1
    else:
        hanoi(n-1, fro, tar, ass)
        print('%c --> %c' %(fro, tar))
        summ += 1
        hanoi(n-1, ass, fro, tar)

num = int(input('请输入汉诺塔上的盘子数：'))
summ = 0
print('移动的方法是：')
hanoi(num, 'X', 'Y', 'Z')
print('总移动次数：', summ)
  
