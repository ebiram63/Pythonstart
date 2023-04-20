sum = 0
sign = 1
fact = 1
pow = 1
x = int(input("Enter x: "))
n = int(input("Enter n: "))
for i in range(2, n + 1 , 2):
    fact = fact * i * (i - 1)
    pow = pow * x * x
    if sign ==1:
        print(" + ", x , " ^ ", 1 , " / ", i , ' ! ', end = '')
    else:
        print(" - ", x , " ^ ", 1 , " / ", i , ' ! ', end = '')
    sum += pow * sign / fact
    sign = -sign
print(" = ", sum)
