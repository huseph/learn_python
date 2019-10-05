try:

    f = open('我为什么是一个文件.txt','w')
    print(f.write('我存在啦！'))
    sum = 1 + '1'
    f.close()
except OSError as reason:
    print('打开文件出错啦！错误原因：', reason)
except TypeError as reason:
    print('类型出错啦！错误原因：', reason)
