Bills = float(input("Type bills : "))
tips_percent = float(input("Type Tip's percent : "))
people = int(input("Type number of people : "))
tip = Bills * (tips_percent/100)
total_price = Bills + tip
per_person = total_price // people
print(per_person)