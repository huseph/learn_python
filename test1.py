data = {}
while True:
    content = input('?????')
    if content == '!p':
        break
    data['a'] = content
    print(type(data['a']))
    del data['a']