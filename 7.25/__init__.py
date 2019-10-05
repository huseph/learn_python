class Complex:
    def __init__(self, realpart, imagpart):    #'self' represent itself
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)         #so now we use 'x.r' but not 'self.r'
