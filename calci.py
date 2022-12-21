import math
import cmath


class Complex:
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag

    def setReal(self, real):
        self.real = real

    def setImag(self, imag):
        self.imag = imag

    def __mul__(self, other):
        C3 = Complex()
        C3.real = self.real * other.real - self.imag * other.imag
        C3.imag = self.real * other.imag + self.imag * other.real

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
        print(str(self.real) + "+ i" + str(self.imag))


class SingleCalc:
    def __init__(self, n=0):
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
        return math.pow(self.n, 1 / 3)

    def factorial(self):
        return math.factorial(self.n)


class BasicFns:
    def __init__(self, n=0):
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
    def __init__(self, i=0, j=0, k=0, mag=0):
        self.i = i
        self.j = j
        self.k = k
        self.mag = mag

    def setI(self, i):
        self.i = i

    def setJ(self, j):
        self.j = j

    def setK(self, k):
        self.k = k

    def magnitudeCalc(self):
        self.mag = math.sqrt(self.i ** 2 + self.j ** 2 + self.k ** 2)

    def directionCalc(self):
        self.magnitudeCalc()
        Dir = Vector()
        Dir.i = self.i / self.mag
        Dir.j = self.j / self.mag
        Dir.k = self.j / self.mag
        return Dir

    def printVector(self):
        print("The vector is: {i} i + {j} j + {k} k".format(i=self.i, j=self.j, k=self.k))

    # Dot Product

    def __mul__(self, other):
        dot = (self.i * other.i) + (self.j * other.j) + (self.k * other.k)
        return dot

    # Cross Product

    def __truediv__(self, other):
        Cross = Vector()

        Cross.i = self.j * other.k - self.k * other.j
        Cross.j = self.k * other.i - self.i * other.k
        Cross.k = self.i * other.j - self.j * other.i

        return Cross

    def __add__(self, other):
        Add = Vector()

        Add.i = self.i + other.i
        Add.j = self.j + other.j
        Add.k = self.k + other.k

        return Add

    def __sub__(self, other):
        Sub = Vector()

        Sub.i = self.i - other.i
        Sub.j = self.j - other.j
        Sub.k = self.k - other.k

        return Sub


class Quad:
    def __init__(self, a, b, c, Disc=0):  # ax2+bx+c
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
        s1 = (-self.b + cmath.sqrt(self.Disc)) / (2 * self.a)
        s2 = (-self.b - cmath.sqrt(self.Disc)) / (2 * self.a)
        self.sols.append(s1)
        self.sols.append(s2)

    def printQuadEq(self):
        print("The equation is {a}X^2 + {b}X + {c} = 0".format(a=self.a, b=self.b, c=self.c))

    def printQuadRoots(self):
        print("The roots of the quadratic equation are {s1} and {s2}".format(s1=self.sols[0], s2=self.sols[1]))


def BC():
    ch = 'y'
    while ch == 'y':
        print("\t-----Basic Arithmetic-----")
        a = int(input("\tEnter 1st number: "))
        b = int(input("\tEnter 2nd number: "))
        Num1 = BasicFns(a)
        Num2 = BasicFns(b)
        print("\t1. Add")
        print("\t2. Subtract")
        print("\t3. Multiply")
        print("\t4. Divide")
        print("\t5. Exit :(")
        print()
        opt = int(input("\tYour option, please: "))
        if opt == 1:
            Num3 = Num1 + Num2
            print("\t", end="")
            Num3.printBasic()
        elif opt == 2:
            Num3 = Num1 - Num2
            print("\t", end="")
            Num3.printBasic()
        elif opt == 3:
            Num3 = Num1 * Num2
            print("\t", end="")
            Num3.printBasic()
        elif opt == 4:
            Num3 = Num1 / Num2
            print("\t", end="")
            Num3.printBasic()
        else:
            print("Exited...")
            break

        ch = input("\tDo you wish to perform another ARITHMETIC operation? [y/n]: ")


def PR():
    ch = 'y'
    while ch == 'y':
        print("\t-----Powers, Roots and Factorial-----")
        a = int(input("\tEnter the number: "))
        Num1 = SingleCalc(a)
        print("\t1. Square")
        print("\t2. Cube")
        print("\t3. Sq root")
        print("\t4. Cu root")
        print("\t5. Factorial")
        print("\t6. Exit :(")
        print()
        opt = int(input("\tYour option, please: "))
        if opt == 1:
            print("\tResult: ", Num1.square())
        elif opt == 2:
            print("\tResult: ", Num1.cube())
        elif opt == 3:
            print("\tResult: ", Num1.squareRoot())
        elif opt == 4:
            print("\tResult: ", Num1.cubeRoot())
        elif opt == 5:
            print("\tResult: ", Num1.factorial())
        else:
            print("Exited...")
            break

        ch = input("\tDo you wish to perform another POWERS operation? [y/n]: ")


def CA():
    ch = 'y'
    while ch == 'y':
        print("\t-----Complex Numbers' Arithmetic-----")
        r1 = float(input("\tEnter the REAL value of 1st complex no: "))
        i1 = float(input("\tEnter the IMAGINARY value of 1st complex no: "))
        C1 = Complex(r1, i1)
        print()
        r2 = float(input("\tEnter the REAL value of 2nd complex no: "))
        i2 = float(input("\tEnter the IMAGINARY value of 2nd complex no: "))
        C2 = Complex(r2, i2)
        print("\t1. Add")
        print("\t2. Subtract")
        print("\t3. Multiply")
        print("\t4. Divide")
        print("\t5. Exit :(")
        print()
        opt = int(input("\tYour option, please: "))
        if opt == 1:
            C3 = C1 + C2
            print("\t", end="")
            C3.printCromp()
        elif opt == 2:
            C3 = C1 - C2
            print("\t", end="")
            C3.printCromp()
        elif opt == 3:
            C3 = C1 * C2
            print("\t", end="")
            C3.printCromp()
        elif opt == 4:
            C3 = C1 / C2
            print("\t", end="")
            C3.printCromp()
        else:
            print("Exited...")
            break

        ch = input("\tDo you wish to perform another COMPLEX operation? [y/n]: ")


def QE():
    ch = 'y'
    while ch == 'y':
        print("\t-----Quadratic Equation Solving-----")
        print("\tQuadratic equations are of the standard form: aX^2 + bX + c = 0")
        print()
        a = int(input("\t\ta?: "))
        b = int(input("\t\tb?: "))
        c = int(input("\t\tc?: "))

        Equat = Quad(a, b, c)
        Equat.discCalc()
        Equat.solve()
        print("\n\t", end="")
        Equat.printQuadEq()
        print("\t", end="")
        Equat.printQuadRoots()

        ch = input("\tDo you wish to SOLVE another equation? [y/n]: ")


def VX():
    pass


def main():

    #
    # C3 = Complex()
    # C3 = C1 - C2
    # C3.printCromp()

    ch = 'y'
    while ch == 'y':
        print()
        print()
        print("Hey, I'm Calci, your personal scientific calculator!")
        print()
        print("1. Calci performs basic arithmetic")
        print("2. Calci performs powers, roots and factorial")
        print("3. Calci performs complex numbers' arithmetic")
        print("4. Calci solves quadratic equations")
        print("5. Calci performs vector operations")
        print("6. Calci performs matrix operations")
        print("7. Calci exits :(")
        print()
        print()
        opt = int(input("Your option, please: "))
        if opt == 1:
            BC()
        elif opt == 2:
            PR()
        elif opt == 3:
            CA()
        elif opt == 4:
            QE()
        elif opt == 5:
            VX()
        else:
            print("Exited...")
            print("Thanks for using Calci! <3")
            break
        print()
        ch = input("Do you wish to perform ANY other operation? [y/n]: ")


main()


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

# V1 = Vector(3, 1, -4)
# V2 = Vector(8, -8, 4)
# V1.printVector()
# V2.printVector()
#
# V1.magnitudeCalc()
# print("Magnitude is: ", V1.mag)
# V2.magnitudeCalc()
# print("Magnitude is: ", V2.mag)
#
# VV2 = V1-V2
# VV2.printVector()
# # V2 = Vector()
# V3 = V1.directionCalc()
# V3.printVector()
# V4 = V2.directionCalc()
# V4.printVector()
#
# V5 = V1*V2
# print(V5)
#
# V6 = V1/V2
# V6.printVector()



