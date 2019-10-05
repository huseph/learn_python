import os
f = open(r'C:\Users\huseph\Desktop\python\8.1\record.txt','r')

roles = {}
cal = 0

for each_line in f:
    if each_line[:5] != '=====':
        [role, line_spoken] = each_line.split(':',1)
        if role not in roles:
            roles[role] = ''
        roles[role] += line_spoken

    else:
        cal += 1
        names = list(roles)
        path = r'C:\Users\huseph\Desktop\python\8.8\contact\con'+str(cal)
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
        for each in range(len(roles)):
            file_name = r'C:\Users\huseph\Desktop\python\8.8\contact\con'+str(cal)+'\\'+names[each] +'.txt'
            fi = open(file_name, 'w+')
            fi.write(roles[names[each]])
            fi.close()
        roles.clear()


        
f.close()
