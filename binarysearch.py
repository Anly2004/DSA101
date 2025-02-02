n=int(input("enter the limit:"))
arr=[]
print("enter the numbers:")
for i in range(n):
    values=int(input())
    arr.append(values)
target=int(input("enter the target:"))
low=0
high=n-1
                                                  #2 6 3 8 10
while(low<=high):                                 #0 1 2 3 4    target=8
    mid=(low+high)/2
    if(arr[mid]==target):
        print(str(target)+ " found at  " + str(mid))
    elif(target>arr[mid]):
        low=mid+1
    elif(target<arr[mid]):
        high=mid-1    
print("the value is not in the array.")




