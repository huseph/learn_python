import os
import time

timea = time.localtime(os.path.getatime(r'C:\Users\huseph\Desktop\python\and_or.py'))
timec = time.localtime(os.path.getctime(r'C:\Users\huseph\Desktop\python\and_or.py'))
timem = time.localtime(os.path.getmtime(r'C:\Users\huseph\Desktop\python\and_or.py'))
##依次为 最后访问时间，创建时间，最后修改时间
print('timea:',timea, 'timec:', timec, 'timem:', timem, sep='\n')
