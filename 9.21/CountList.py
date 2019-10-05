class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys((x for x in args), 0)
        self.count[len(self.values)] = 0
    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.count[self.values[key]] += 1
        return self.values[key]

    def __setitem__(self, value):
        self.count[len(self.values)] = 0
        self.values.append(value)

    def __delitem__(self, item):
        del self.count[self.values[item]]
        del self.values[item]

        


    
c1 = CountList(1, 2, 3, 4, 5)
c2 = CountList(6, 7, 8, 9 )

print(c1[1] + c2[1])
del c2[1]
print(c2.count, '\n', c2.values)
