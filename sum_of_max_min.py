a=[-1,2,-4,5,3]
sum=0
for i in range(len(a)):
    maximum=max(a)
    minimum=min(a)
sum=maximum+minimum
print("the maximum value in the array:",str(maximum))
print("the minimum value in the array:",str(minimum))

print("the sum of max & min is:", str(sum))

