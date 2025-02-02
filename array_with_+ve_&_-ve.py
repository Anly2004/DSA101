# question:ex 22

n = int (input("enter the limit:"))
arr=[]
for i in range (n):
    arr.append(int(input("enter the element" + str(i) +":")))
for i in range (n):
    if (arr[i]>0):
        print ("positive")
    elif (arr[i]<0):
        print("negative") 
  
   
    