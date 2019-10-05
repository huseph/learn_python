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
    return summ

summ = 0
