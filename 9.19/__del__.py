class Try:
    def __init__(self):
        print('__init__ running...')
    def __del__(self):
        print('__del__ running...')
    def isAlive(self):
        print('I am still alive')

t1 = Try()
t2 = t1
del t1
print('t1 has been deleted')
del t2   ### you can notice that __del__ runs when all the tag has been deleted
print('t2 has been deleted')
