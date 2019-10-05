basket = {'apple', 'banana', 'pear', 'orange', 'banana'}
print(basket)

a = {'ababaabab'}
print(a)

a = set('abababab')
print(a)

b = set()
c = {}
print(type(b), type(c))    #you can only define an empty set with 'set()'

thisset = set(('apple', 'banana', 'pear'))
print(thisset)

thisset.update([1,2],[3,4])
print(thisset)

print(thisset.discard('a'))   #return 'None' if there is no such value
#thisset.remove('a')   #you can't use 'remove' to delet a not defined value
