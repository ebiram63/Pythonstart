n = int(input("Please enetr your number: "))
result = 0 
pow = 1
while n > 0:
    r = n % 10
    r = r + 1
    if r == 10:
        r = 0
    result += r * pow
    pow *= 10
    n //= 10
print(result)