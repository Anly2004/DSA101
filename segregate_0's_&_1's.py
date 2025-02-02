#You are given an array of 0s and 1s in random order.
#Segregate 0s on left side and 1s on right side of the array [Basically you have to sort the array]. 
#Traverse array only once. 


arr=[0,0,1,0,1,1]
zeroarr=[]
onearr=[]
mainarr=[]
for  i in range(len(arr)):
    if arr[i]==0:
        zeroarr.append(arr[i])
    else:
        onearr.append(arr[i])
mainarr=zeroarr+onearr
print(mainarr)

