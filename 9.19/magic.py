class myClass:
    count = 0

a = myClass()
b = myClass()
c = myClass()

c.count += 10
myClass.count += 100
print(a.count, b.count, c.count)
