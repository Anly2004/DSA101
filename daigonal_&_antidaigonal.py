#daigonal
n=int(input("enter the size: "))

for i in range(n):
    for j in range(n):
        if(i==j):
            print("*",end=" ")
        else:
            print(" ",end="")
    print()

#antidaigonal
n=int(input("enter the size: "))

for i in range(n):
    for j in range(n):
        if(i+j==n-1):
            print("*",end=" ")
        else:
            print(" ",end="")
    print()