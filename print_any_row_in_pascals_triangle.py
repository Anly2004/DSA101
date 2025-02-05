rowlimit=int(input("enter the row limit:"))

arr=[]

for i in range(rowlimit):
    row=[]
    for  j in range(i+1):
        if(j==0 or j==i) :
            row.append(1)
        else:
            row.append(arr[i-1][j-1]+arr[i-1][j])
    arr.append(row)  
for i in range(rowlimit):
    for j in range(i+1):

        print(arr[i][j],end=" ")
    print()
    print()

k=int(input("enter the printing row number:"))
for i in range(rowlimit):
    if(k==i):
        print(arr[i])
    print()




