#2D matrix

r=int(input("enter the rowsize:"))
c=int(input("enter the columsize:"))
matrix=[]
for i in range(r):
    arr=[]
    for j in range(c):
        arr.append(int(input()))
    matrix.append(arr)
print("____matrix____")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end="\t")
    print()