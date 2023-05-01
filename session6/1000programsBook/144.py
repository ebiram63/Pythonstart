rows = int(input("Input rows: "))
for i in range (1, rows + 1):
    for j in range(1, rows + 1 - i):
        print( end = " " )
    for j in range(1, rows + 1):
        if i == 1 or i == rows  :
            print(end = "*")
        else:
            print(end = " ")
    print()