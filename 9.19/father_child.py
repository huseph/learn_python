class Parent:
    def hello(self):
        print('正在调用父类方法……')

class Child(Parent):
    pass


p = Parent()
p.hello()

c = Child()
c.hello()

class Child(Parent):
    def hello(self):
        print('正在调用子类方法...')

cc = Child()
cc.hello()
