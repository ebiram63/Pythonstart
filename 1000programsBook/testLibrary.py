rows = int(input("Input rows: "))
for i in range(1, (rows * 2)):
    if i == rows:
        for j in range(1, (rows * 2)):
            print(end = "+")
    else:
        for j in range(1, rows):
            print(end = " ")
        print(end = "+")
    print()