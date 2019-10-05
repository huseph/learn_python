dict1 = {}
dict1 = dict1.fromkeys(range(32), 'like')
for eachValue in dict1.values():
    print(eachValue)
for eachItem in dict1.items():
    print(eachItem)



print(dict1.get(32))
