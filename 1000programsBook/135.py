k = 1 
rows = int(input("Input number of rows: "))
for i in range(1, rows+1):
    for j in range(1, i + 1):
        print(k, end = "\t")
        k = k + 1
    print()