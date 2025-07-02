Day = int(input("Type day number : "))
if(0 > Day or Day > 7) :
    print("sorry , Type again.")
    exit()

if(Day <= 5 ):
    print("Weekday")
else :
    print("Weekend")