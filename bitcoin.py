value=int(input("enter the bitcoin value: "))
perinc=int(input("enter the percentage increase: "))
final_value=(perinc/100*value)+value
print("the total increase value is:" +str(final_value))
inc_or_dec=final_value - value
print("the increased or decreased value is:" +str(inc_or_dec))