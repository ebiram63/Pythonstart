t = 1
rows = int(input("Input number of rows: "))
spc = rows + 4 - 1
for i in range(1, rows+ 1):
    for k in range(spc, 0, -1):
        print(end = " ")
    for j in range(1, i + 1):
        if t < 10:
            print(t, end = " ")
            t = t + 1
        else:
            print(t, end = " ")
            t = t + 1
    spc = spc - 1
    print()