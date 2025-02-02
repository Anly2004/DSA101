num=int(input("enter the number to be read:"))
n=(num//10)   #to divide an integer we use this  symbol // (double slash),
               #by doing this we can remove the last digit.
last_digit=n%10
print ("the second last digit of the integer is:",str(last_digit))


