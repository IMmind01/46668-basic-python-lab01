score = int(input("Type your final exam score : "))
if(0 > score or score > 100) :
    print("sorry , Type again.")
    exit()

if (score >= 50 ) :
    print("Pass")
else :
    print("Fail")