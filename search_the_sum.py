n=int (input("enter the size of array"))
arr=[]
count=0
print("enter the elements into  array:")
for i in range(0,n):                                #2 5 3 7 4
    arr.append(int(input()))                        #target=6
target=int(input("enter the  sum:"))
for i in range(0,n):
    for j in range(i+1,n):                            
       if(arr[i]+arr[j]==target):                     
          print("\nthe values of the target are:"+str(arr[i])+ "&"+str(arr[j]))
          count=count+1
if(count==0):
    print("the values of target is not in the array")
       