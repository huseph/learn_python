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

class Friend:
    def __init__(self):
        self.parent = Parent()
        self.child = Child()

f = Friend()
f.parent.myMethod()
f.child.myMethod()
