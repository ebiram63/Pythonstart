sum = 0
sign = 1
fact = 1
n = int(input("Enter n: "))
for i in range(1, n + 1):
    fact = fact * i
    if sign == 1 :
        print(" + ", i , " / ", fact , end = '')
    else:
        print(" - ", i , " / ", fact , end = '')
    sum += i * sign / fact
    sign = -sign;
print(" = ", sum)