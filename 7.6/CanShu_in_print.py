favourite = 'huseph'
for i in favourite:
    print(i, end = ' ')
    print(i)
for i in favourite:
    print(i, sep = '', end = '')
print('\n')
for i in favourite:
    print(i, end = '')
print('\n')
for i in favourite:
    print(i, sep = '')
print('\n')
for i in favourite:
    print(i, sep = '\n')
with open('abc.txt','w') as f:
    print("file\n","abc","fff",sep='#########\n',end='',file=f)
#from these cases, we can learn that 'sep' means the things you want to print
# between things in one 'print', end means the thing you want to print at the
# end of the print.
