n = int(input("Please enter n: "))
if n > 80 or n < 0:
    print("Invalid number")
else:
    for i in range(1 , n + 1):
        for j in range(1, n + 1):
            if i == 1 or j == 1 or i + j <= n + 1:
                print(end = "*")
            else:
                print(end = " ")
        print()