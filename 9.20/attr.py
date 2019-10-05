class C:
    def __getattribute__(self, name):
        print('__getattribute__ is running')
        return super().__getattribute__(name)
    
    def __getattr__(self, name):
        print('__getattr__ is running')

    def __setattr__(self, name, value):
        print('__setattr__ is running')
        return super().__setattr__(name, value)

    def __delattr__(self, name):
        print('__delattr__ is running')
        return super().__delattr__(name)

c = C()
print(c.x)

c.x = 1
print(c.x)

del c.x
    
