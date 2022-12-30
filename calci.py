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
        self.Disc = Disc
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


class Matrix:
    def __init__(self, r = None, c = None, mat = None):
        self.r = r
        self.c = c
        self.mat = mat

    def matIn(self):
        self.r = int(input("No. of rows: "))
        self.c = int(input("No. of columns: "))
        self.mat = []
        for i in range(self.r):
            col = []
            for j in range(self.c):
                elem = int(input("Enter the element at index {r} {c}: ".format(r=i + 1, c=j + 1)))
                col.append(elem)
            self.mat.append(col)

    def matOut(self):
        print()
        print("The Matrix is: ")
        for i in range(self.r):
            for j in range(self.c):
                print(self.mat[i][j], end='\t')
            print()
        print()

    def __add__(self, other):
        if (self.r != other.r) or (self.c != other.c):
            print("These matrices cannot be added!")

        else:
            r = self.r
            c = self.c
            AddMatrix = Matrix(r, c)
            AddMatrix.mat = []
            for i in range(r):
                AddMatrix.mat.append([])
                for j in range(c):
                    AddMatrix.mat[i].append(self.mat[i][j] + other.mat[i][j])

            AddMatrix.matOut()

    def __sub__(self, other):
        if (self.r != other.r) or (self.c != other.c):
            print("These matrices cannot be subtracted!")

        else:
            r = self.r
            c = self.c
            SubMatrix = Matrix(r, c)
            SubMatrix.mat = []
            for i in range(r):
                SubMatrix.mat.append([])
                for j in range(c):
                    SubMatrix.mat[i].append(self.mat[i][j] - other.mat[i][j])

            SubMatrix.matOut()

    def __mul__(self, other):
        if self.c != other.r:
            print("These matrices cannot be multiplied!")
        else:
            x = self.r
            y = other.c
            MulMatrix = Matrix(x, y)
            MulMatrix.mat = []
            for i in range(x):
                col = []
                for j in range(y):
                    elem = 0
                    col.append(elem)
                MulMatrix.mat.append(col)

            print(len(self.mat), " ", len(other.mat), " ", len(other.mat[0]))

            for i in range(len(self.mat)):
                for j in range(len(other.mat[0])):
                    for k in range(len(other.mat)):
                        MulMatrix.mat[i][j] += self.mat[i][k] * other.mat[k][j]

            MulMatrix.matOut()


# Mat1 = Matrix()
# print("Matrix 1: ")
# Mat1.matIn()
#
# Mat1.matOut()
# Mat2 = Matrix()
# print("Matrix 2: ")
# Mat2.matIn()
# Mat2.matOut()
#
# Mat1 * Mat2


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
    ch = 'y'
    while ch == 'y':
        print("\t-----Vector Operations-----")
        print("\t1. Magnitude Calculation")
        print("\t2. Direction of the vector")
        print("\t3. Add")
        print("\t4. Subtract")
        print("\t5. Scalar (dot) Product")
        print("\t6. Vector (cross) Product")
        print("\t7. Exit :(")
        print()
        opt = int(input("\tYour option, please: "))
        print()
        if opt == 1 or opt == 2:
            print("\t\tEnter vector components (i, j, k) separated by a space: ", end="")
            lt = list(map(int, input().split()))
            Vec1 = Vector(lt[0], lt[1], lt[2])

            if opt == 1:
                Vec1.magnitudeCalc()
                print("\tMagnitude of given vector is: ", Vec1.mag)

            elif opt == 2:
                Vec2 = Vec1.directionCalc()
                print("\t", end="")
                Vec2.printVector()

        elif opt == 3 or opt == 4 or opt == 5 or opt == 6:
            print("\t\tEnter vector 1 components (i, j, k) separated by a space: ", end="")
            lt1 = list(map(int, input().split()))
            Vec1 = Vector(lt1[0], lt1[1], lt1[2])

            print("\t\tEnter vector 2 components (i, j, k) separated by a space: ", end="")
            lt2 = list(map(int, input().split()))
            Vec2 = Vector(lt2[0], lt2[1], lt2[2])

            if opt == 3:
                Vec3 = Vec1 + Vec2
                print("\t", end="")
                Vec3.printVector()

            elif opt == 4:
                Vec3 = Vec1 - Vec2
                print("\t", end="")
                Vec3.printVector()

            elif opt == 5:
                print("\tDot Product of the vectors is: ", Vec1 * Vec2)

            elif opt == 6:
                Vec3 = Vec1 / Vec2
                print("\t", end="")
                Vec3.printVector()

        else:
            print("Exited...")
            break

        ch = input("\tDo you wish to perform another VECTOR operation? [y/n]: ")


def MX():
    ch = 'y'
    while ch == 'y':
        print("\t-----Matrix Operations-----")
        print("\t1. Add")
        print("\t2. Subtract")
        print("\t3. Multiply")
        print("\t4. Exit :(")

        print()
        opt = int(input("\tYour option, please: "))
        print()
        if opt == 1 or opt == 2 or opt == 3:

            Mat1 = Matrix()
            print("Matrix 1: ")
            Mat1.matIn()
            Mat1.matOut()

            Mat2 = Matrix()
            print("Matrix 2: ")
            Mat2.matIn()
            Mat2.matOut()

            if opt == 1:
                Mat1 + Mat2
            elif opt == 2:
                Mat1 - Mat2
            elif opt == 3:
                Mat1 * Mat2

        else:
            print("Exited...")
            break

        ch = input("\tDo you wish to perform another MATRIX operation? [y/n]: ")
def main():

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
        elif opt == 6:
            MX()
        else:
            print("Exited...")
            break
        print()
        ch = input("Do you wish to perform ANY other operation? [y/n]: ")
    print()
    print("Thanks for using Calci! <3")


main()
