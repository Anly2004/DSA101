emp_years=int(input("enter the employement years:"))
kids_count=int(input("enter the no of kids:"))
bonus=int(input("enter the bonus value of the emp who didn't miss  1 day:"))
minimum_wage=400
experience=20*emp_years
emp_kid=30*kids_count 
total_amount=minimum_wage+experience+emp_kid+bonus
print("the annual wage is:"+str(total_amount))
