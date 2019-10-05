class C:
    def __init__(self, x = 0):
        self.x = x

c1 = C()
print(hasattr(c1, 'y'))
print(getattr(c1, 'y', '您所访问的属性不存在...'))

setattr(c1, 'y', 'hello')
print(getattr(c1, 'y', '您所访问的属性不存在...'))

delattr(c1, 'y')
print(getattr(c1, 'y', '您所访问的属性不存在...'))
