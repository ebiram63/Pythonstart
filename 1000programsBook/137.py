rows = int(input("Input number of rows: "))
spc = rows + 4 - 1
for i in range(1, rows + 1):
    for k in range(spc, 0, -1):
        print(end = " ")
    for j in range(1, i + 1):
        print(end = " * ")
    spc = spc - 1
    print()