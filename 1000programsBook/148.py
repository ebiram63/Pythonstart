rows = int(input("Input rows: "))
for i in range(1, rows):
    print(end = " ")
    for j in range(1, (2 * i - 2) + 1):
        print(end =" ")
    for j in range(i, rows + 1):
        print(end = "*")
    print()
for i in range(1, rows + 1):
    for j in range((2 * i - 2), (2 * rows  - 2)):
        print(end =" ")
    for j in range(1, i + 1):
        print(end = "*")
    print()                   