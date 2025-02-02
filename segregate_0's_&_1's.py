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

