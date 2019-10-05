class myClass:
    def x(self):
        print('Hello!')

c = myClass()
c.x()
c.x = 1
print(c.x)


c.x()   ###TypeError: 'int' object is not callable
