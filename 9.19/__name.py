class Person:
    __name = 'hjh'
    def getname(self):
        return self.__name


p = Person()

##print(p.__name)    IndentationError: unexpected indent
print(p.getname())

