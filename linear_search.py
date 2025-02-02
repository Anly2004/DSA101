n=int (input("enter the size of array"))
arr=[]
print("enter the elements into  array:")
for i in range(0,n):
    arr.append(int(input())) 
key=int(input("enter the key element to be searched:"))
for i in range(0,n):
    if(key==arr[i]):
        print("\ntarget element is found")
        break
    else:
        print("not found")