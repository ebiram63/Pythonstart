n = int(input("Plaese enetr n: "))
if n > 80 or n < 0:
    print("Invalid number")
else:
    for i in range(1 , n + 1):
        for j in range(1 , n + 1):
            if i == n or j == n or i + j >= n + 1:
                print(end = "*")
            else:
                print(end = " ")
        print()