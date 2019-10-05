class Parent:
    def __init__(self):
        self.height = 10

        
    def myMethod(self):
        print('正在调用父类方法...')

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.weight = 11
    
    def myMethod(self):
        print('正在调用子类方法...')

c = Child()
c.myMethod()
super(Child, c).myMethod()
print(c.height, c.weight)
