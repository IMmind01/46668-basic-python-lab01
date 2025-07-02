price = float(input("Type the price : "))
if(price >= 2000):
    finalprice = price - (price * 15/100)
elif(price >= 1000):
    finalprice = price - (price * 10/100)
elif(price >= 500):
    finalprice = price - (price * 5/100)
elif(price <= 500):
    finalprice = price 

print(finalprice)