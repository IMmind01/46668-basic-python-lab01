name = (input("Type product name : "))
price = float(input("How much is it? : "))
price2 = str(float(price)).rstrip('0').rstrip('.')
print(f"Product:{name}, Price:{price2} THB")