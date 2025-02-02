
geometry=float(input("enter the marks in geometry:"))
algebra=float(input("enter the marks in the algebra:"))
physics=float(input("enter the marks in the physics:"))
average=(geometry+algebra+physics)/3
print("average is:" +str(average))
if (average>=7):
    print("good job!")
elif (6 <average < 4):
    print("you need to work hard! ")
elif (average <4):
    print("failed,you really need to work harder!")

   
