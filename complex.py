import math

class Complex:
    def __init__(self, real,imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        r = self.real + other.real
        i = self.imag + other.imag
        return Complex(r, i)

    def __sub__(self, other):
        r = self.real - other.real
        i = self.imag - other.imag
        return Complex(r, i)

    def __mul__(self, other):
        a = self.real * other.real
        b = self.real * other.imag
        c = self.imag * other.real
        d = self.imag * other.imag
        r = a - d
        i = b + c
        return Complex(r, i)

    def __truediv__(self, other):
        conjugate = Complex(other.real, other.imag * -1)
        a = other.real * conjugate.real
        b = other.imag * conjugate.imag * -1
        denominator = a + b

        a = self.real * conjugate.real
        b = self.real * conjugate.imag
        c = self.imag * conjugate.real
        d = self.imag * conjugate.imag
        r = (a - d) / denominator
        i = (b + c) / denominator
        return Complex(r, i)

    def mod(self):
        result = abs(math.sqrt(self.real**2 + self.imag**2))
        return "{0:.2f}".format(result)

    def __repr__(self):
        if(self.real == 0 and self.imag == 0):
            return "{0:.2f}".format(0)
        elif(self.real == 0 and self.imag != 0):
            return "{0:.2f}i".format(self.imag)
        elif(self.real != 0 and self.imag == 0):
            return "{0:.2f}".format(self.real)
        else:
            if self.imag < 0:
                sign = "-"
            else:
                sign = "+"
            return "{0:.2f} {1} {2:.2f}i".format(self.real, sign, abs(self.imag))
    def __str__(self):
        return self.__repr__()

c = Complex(2, 1)
d = Complex(5, 6)

print(c + d)
print(c - d)
print(c * d)
print(c / d)
print(c.mod())
print(d.mod())
