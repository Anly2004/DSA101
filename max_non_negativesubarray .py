n=int(input("enter the limit of array:"))
arr=[]
temparr=[]
maxsumarr=[]
maxsum=0
tempsum=0
print("enter the elements:")
for i in range(n):
    values=int(input())             
    arr.append(values)


for i in range(n):
    if arr[i]>=0:
        temparr.append(arr[i])
        tempsum=tempsum+arr[i]
        
    else:
        if tempsum>maxsum:
            maxsum=tempsum
            maxsumarr=temparr[:]
        elif tempsum==maxsum and len(temparr) >len(maxsumarr):
            maxsumarr=temparr[:]
            maxsum=tempsum
        temparr.clear()
        tempsum=0
if(tempsum>maxsum):
        maxsum=tempsum
        maxsumarr=temparr[:]
elif tempsum==maxsum and len(temparr) >len(maxsumarr):
        maxsumarr=temparr[:]
        maxsum=tempsum


print("The subarray with the maximum sum is:", maxsumarr)
print("The maximum sum is:", maxsum)


    

        
        