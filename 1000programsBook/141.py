num = int(input("Please enetr your number: "))
k = num & 1
if k != 0:
    print("Least significant bt of ", num, " is set. ")
else:
    print("Least significant Bit of ", num, "is unset. ")