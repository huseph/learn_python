line1 = [123, 456]
line2 = line1
line1.insert(0, 111)           ########真就两个都改呗！！！！！
print(line1, line2)

line1 = [123, 456]
line2 = [789]
line3 = line1[:]          #####要这样建立被备份！
line3.extend(line2)
print(line1)
line2.insert(0, ['huseph', 'moana'])
print(line2[0][1])

