for i in range(1000, 10000):
    num = i 
    while num > 0:
        digit = num % 10
        if digit == 9 or digit == 4 or digit == 2 or digit == 1:
            break
        num //= 10

    if num > 0:
        print(i , end = "  ")

print("================================================")
# this app witout and repeatition

for o in range(1000,10000):
    c1 = c2 = c4 = c9 = 0
    num = o
    while num > 0:
        digit = num % 10
        if(digit == 1):
            c1 = c1 + 1
        elif( digit == 2):
            c2 = c2 + 1
        elif( digit == 4):
            c4 = c4 + 1
        elif( digit == 9):
            c9 = c9 + 1
        num //= 10
    if c1 == 1 and c2 == 1 and c4 == 1 and c9 == 1:
        print(o , end = "  ")
