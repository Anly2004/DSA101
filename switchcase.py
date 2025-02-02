cost=int(input("reads the price of the product:"))
location=input("enter the location:")
match location:
    case "us":
        amount=cost+5
    case "europe":
        amount=cost+7
    case "canada":
        amount=cost+3
    case "others" :
        amount=cost+9
print("you have to pay" +str(amount)+ "$")


    