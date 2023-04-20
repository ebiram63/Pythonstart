n = int(input("Enter your odd number: "))
y = n // 3
k = n + 3
for i in range(1, y + 2):
    print(end =  " ")
for  i in range(1, y + 1):
    print(end = "*")
print()
for i in range(1, y +1):
    for j in range(1, y - i + 1):
        print(end = " ")
    print(end = "*")
    for c in range(n + 2, y + k + 1):
        print(end = " ")
    if( i == n):
        print(end = " ")
    else:
        print(end = "*")
    print()
    k = k + 2
for po in range(1, n // 2 + 1):
    print(end = "*")
    for pow in range(1, n + 1):
        print(end = " ")
    print("*")
m = 1
for i in range(1, y + 1):
    for c in range(y + 2, y + m + 1):
        print(end = " ")
    print(" ")
    if i == y:
        print(end = " ")
        for h in range(1,y + 1):
            print(end = "*")
    else:
        print(end = "*")
    for j in range(1, 2 * y - 2 * i + y + 1):
        print( end = " ")
    if i == y:
        print(end = "")
    else:
        print(end = "*")
    print()
    m = m + 1
        