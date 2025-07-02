num1 = int(input("Type number here : "))
num2 = int(input("Type another one here : "))
num3 = int(input("Type last one here : "))

if (num1 > num2 and num1 > num3):
    print(num1)
elif (num2 > num1 and num2 > num3):
    print(num2)
elif (num3 > num1 and num3 > num2):
    print(num3)
else :
    print("error")