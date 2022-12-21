import math
import cmath


class Complex:
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag

    def setReal(self, real):
        self.real = real

    def setImag(self, imag):
        self.imag = imag

    def __mul__(self, other):
        C3 = Complex()
        C3.real = self.real*other.real - self.imag*other.imag
        C3.imag = self.real*other.imag + self.imag*other.real

        return C3

    def __add__(self, other):
        C3 = Complex()
        C3.real = self.real + other.real
        C3.imag = self.imag + other.imag

        return C3

    def __sub__(self, other):
        C3 = Complex()
        C3.real = self.real - other.real
        C3.imag = self.imag - other.imag

        return C3

    def __truediv__(self, other):
        C3 = Complex()
        i = (other.real * other.real) + (other.imag * other.imag)
        C3.real = (self.real * other.real + self.imag * other.imag) / i
        C3.imag = (self.imag * other.real - self.real * other.imag) / i

        return C3

    def printCromp(self):
        print(str(self.real) + " i" + str(self.imag))


class SingleCalc:
    def __init__(self, n = 0):
        self.n = n

    def setN(self, n):
        self.n = n

    def square(self):
        return self.n ** 2

    def cube(self):
        return self.n ** 3

    def squareRoot(self):
        return math.sqrt(self.n)

    def cubeRoot(self):
        return math.pow(self.n, 1/3)

    def factorial(self):
        return math.factorial(self.n)


class BasicFns:
    def __init__(self, n = 0):
        self.n = n

    def setN(self, n):
        self.n = n

    def __add__(self, other):
        B3 = BasicFns()
        B3.n = self.n + other.n
        return B3

    def __sub__(self, other):
        B3 = BasicFns()
        B3.n = self.n - other.n
        return B3

    def __mul__(self, other):
        B3 = BasicFns()
        B3.n = self.n * other.n
        return B3

    def __truediv__(self, other):
        B3 = BasicFns()
        B3.n = self.n / other.n
        return B3

    def printBasic(self):
        print("Result: " + str(self.n))


class Vector:
    def __init__(self, i = 0, j = 0, k = 0, mag = 0, dir = 0):
        self.i = i
        self.j = j
        self.k = k
        self.mag = mag
        self.dir = dir

    def setI(self, i):
        self.i = i

    def setJ(self, j):
        self.j = j

    def setK(self, k):
        self.k = k

    # def


class Quad:
    def __init__(self, a, b, c, Disc = 0):  # ax2+bx+c
        self.a = a
        self.b = b
        self.c = c
        self.sols = []

    def setA(self, a):
        self.a = a

    def setB(self, b):
        self.a = b

    def setC(self, c):
        self.a = c

    def discCalc(self):
        self.Disc = self.b ** 2 - 4 * self.a * self.c

    def solve(self):
        s1 = (-self.b + cmath.sqrt(self.Disc))/(2 * self.a)
        s2 = (-self.b - cmath.sqrt(self.Disc))/(2 * self.a)
        self.sols.append(s1)
        self.sols.append(s2)

    def printQuadEq(self):
        print("The equation is {a}X^2 + {b}X + {c} = 0".format(a = self.a, b = self.b, c =  self.c))

    def printQuadRoots(self):
        print("The roots of the quadratic equation are {s1} and {s2}".format(s1 = self.sols[0], s2 = self.sols[1]))


# Q1 = Quad(1, 5, 6)
# Q1.discCalc()
# Q1.solve()
# Q1.printQuadEq()
# Q1.printQuadRoots()

# B1 = BasicFns(5)
# B2 = BasicFns(4)
# B3 = BasicFns()
# B3 = B1-B2
# B3.printBasic()


# S1 = SingleCalc(5)
# print(S1.squareRoot())


def main():
    C1 = Complex()
    C2 = Complex()
    r1 = float(input("Enter the real value of 1st complex no: "))
    i1 = float(input("Enter the imaginary value of 1st complex no: "))
    C1.setReal(r1)
    C1.setImag(i1)
    r2 = float(input("Enter the real value of 2nd complex no: "))
    i2 = float(input("Enter the imaginary value of 2nd complex no: "))
    C2.setReal(r2)
    C2.setImag(i2)

    C3 = Complex()
    C3 = C1 - C2
    C3.printCromp()


# main()
