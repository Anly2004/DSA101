n=int(input("enter the limit of the sequence:"))
a1=0
a2=1
sum=0
print(a1)
print(a2)
for i in range(0,n):
    sum=a1+a2
    print(sum)
    a1=a2
    a2=sum
   
