import support
num = int(input('请输入汉诺塔上的盘子数：'))
print('移动的方法是：')
sum1 = support.hanoi(num, 'X', 'Y', 'Z')
print('总移动次数：', sum1)
  
