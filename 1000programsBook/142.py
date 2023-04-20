BITS = 32
num = int(input("Input num: "))
msb = 1 << (BITS - 1)
k = num & msb
if k != 0:
    print("Least significant bt of ", num, " is set(1). ")
else:
    print("Least significant Bit of ", num, "is unset(0). ")