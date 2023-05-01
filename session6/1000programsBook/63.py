x = int(input("Enter X: "))
n = int(input("Enter n: "))

sum = 0
for i in range(1, n + 1):
    pow = 1
    for j in range(1, i + 1):
        pow *= x
    sum += pow
print(sum)