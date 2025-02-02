arr=[]
limit=int(input("enter the limit of array:"))
for i in range (limit):
    num=int(input("enter the numbers:"))
    arr.append(num)
print(arr)
print("max of array " +str(max(arr)))
print("min of array "+ str(min(arr)))


