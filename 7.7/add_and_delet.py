line = [1, 2, 3, [666]]
print(line)
line.append('OK')
print(line)
line.insert(0, 'huseph')
line.extend(['come', 'on'])
print(line)
line.remove('OK')
first = line.pop(0)
del line[1]
print(line, '\nfirst =', first)
del line

input()

