fo = open("runoob.txt", "wb")
print ("文件名为: ", fo.name)
print('1')
# 刷新缓冲区
fo.flush()
print('2')
# 关闭文件
fo.close()
