class C:
    def __init__(self, size = 10):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self, value):
        self.size = value
    def delSize(self):
        del self.size
    x = property(getSize, setSize, delSize)  ###property(fget, fset, fdel, doc)

c1 = C()
print(c1.x)
c1.x = 18
print(c1.getSize())
