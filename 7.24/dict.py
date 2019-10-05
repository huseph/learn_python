dict1 = {'Name': 'Joseph', 'Age': 18, 'School': 'UESTC'}

print(dict1['Name'], dict1['Age'])

dict1['Age'] += 1

print(dict1['Age'])
#print(dict1['age'])    you can't use this 
print(dict1.get('Age'))
print(dict1.get('age'))

print(len(dict1))

print(dict1)
print(str(dict1))     #same

if 'Name' in dict1:
    print('yes')
else:
    print('no')

dict1.clear()

print(dict1)
str(dict1)

