n = int(input("Please enter n: "))
for i in range(0 , n):
    for j in range(0, n - i):
        print(end = " ")
    for j in range(0 , i + 2):
        if j == 0 or j == i:
            print(end = "* ")
        else:
            print(end = "o ")
    print()