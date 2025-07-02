age = int(input("Type your age : "))
day = int(input("Type day number : "))
ticket = 100

if(age < 13):
    price = ticket
elif(13 <= age < 60):
    price = ticket + 80
elif(age >= 60) :
    price = ticket + 20
else:
    print("Error please type again.")

if(day >= 6 ):
    Finalprice = price + 50
else:
    Finalprice = price

print(Finalprice)
    