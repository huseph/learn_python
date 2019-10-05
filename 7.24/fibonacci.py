a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b   #先计算右边，再同时赋值给左边S
