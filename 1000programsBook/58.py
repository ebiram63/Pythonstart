for i in range(100,1000):
    num = i 
    while num > 0:
        digit = num % 10 
        if digit == 1 or digit == 4 or digit == 8:
            break
        num //= 10
    if num > 0:
        print(i , end = "  ")
