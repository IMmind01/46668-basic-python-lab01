number = int(input("Please enter your number : "))
buaklek = 0
for num in range(1,number+1):
    if num % 2 != 0:
     buaklek += num
print(f"ผลลัพธ์คือ {buaklek}")
