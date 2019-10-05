f = open(r'C:\Users\huseph\Desktop\python\8.1\record.txt','r')

roles = {}


for each_line in f:
    if each_line[:5] != '=====':
        [role, line_spoken] = each_line.split(':',1)
        if role not in roles:
            roles[role] = []
        roles[role].append(line_spoken)

f.close()
print(roles)
print('共有', len(roles),'个人物登场',sep = '')
