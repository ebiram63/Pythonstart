
sign = -1
n = int(input("Enter n : "))
p = 4
k = 3
print(" i : " , '         \t',   "PI")
print("===", ' \t', "=================")
for i in range(1, n+ 1):
    p += sign * 4 / k
    k += 2
    sign = -sign
    print(i, ' \t', p)
    