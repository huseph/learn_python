class New_int(int):
    def __add__(self, other):
        return int.__sub__(self, other)
    def __sub__(self, other):
        return int.__add__(self, other)

a = New_int(3)
b = New_int(5)

print(a + b)
print(a - b)
