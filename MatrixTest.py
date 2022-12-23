r = int(input("Enter no of rows: "))
c = int(input("Enter no of columns: "))
mat = []
for i in range(r):
    col = []
    for j in range(c):
        elem = int(input("Enter the element at index {r} {c}: ".format(r=i+1, c=j+1)))
        col.append(elem)
    mat.append(col)

print(mat)