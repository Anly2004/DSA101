#inverted traingle
n=int(input("enter the size of pyramid: "))
a=n
for i in range(0,n):
    for j in range(0,a):
        print("*",end=" ")
    print("\n")
    a-=1


