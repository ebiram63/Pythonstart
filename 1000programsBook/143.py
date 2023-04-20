rows = int(input("Input rows: "))
for i in range(1, rows + 1):
    for j in range(1, rows + 1 - i):
        print(end = " ")
    for j in range(1, rows + 1):
        print(end = " * ")
    print()