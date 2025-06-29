allpoint = int(input("Type your point : "))
if(0 > allpoint or allpoint > 30) :
    print("sorry , Type again.")
    exit()
midterm = int(input("Type your midterm score : "))
if(0 > midterm or midterm > 30) :
    print("sorry , Type again.")
    exit()
Final = int(input("Type your Final exam score : "))
if(0 > Final or Final > 40) :
    print("sorry , Type again.")
    exit()

Grade = allpoint + midterm + Final

if(Grade >= 80) :
    print("A")
elif(Grade >= 75) :
    print("B+")
elif(Grade >= 74) :
    print("B")
elif(Grade >= 65) :
    print("C+")
elif(Grade >= 60) :
    print("C")
elif(Grade >= 55) :
    print("D+")
elif(Grade >= 50) :
    print("D")
elif(Grade >= 0) :
    print("F")

