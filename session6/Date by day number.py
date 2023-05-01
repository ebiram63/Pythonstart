# date based on day

Daynum = int(input("Enter your number: "))

Month = 0
Day = 0

if 0 < Daynum <= 186:
    Month = (Daynum // 31) + 1 # Month counter
    Day = Daynum % 30 # Day counter

elif 186 < Daynum <= 365:
    Daynum -= 186
    Month = (Daynum // 30) + 1  + 6# Day counter
    Day = Daynum % 30 # Day counter
else:
    print("The number is out of range!")


print("Today is: " , Month, "." , Day)
