line1 = [123]
print(line1.count(123))
print(line1.count(234))
line2 = [111,222]
line1.extend([456,789,line2])   ###列表中的列表不会因reverse而翻转！！
line1.reverse()
line2.reverse()                    ######反转2后1中的也被翻转！！
print(line1)

