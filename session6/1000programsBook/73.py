n = int(input("Please enter n: "))
if n > 80 or n < 0:
    print("Invalid number")
else:
    for i in range(1 , n + 1 ):
        for j in range(1 , n + 1):
            if  i == n or i + j == n + 1 or j == n:
                print(end = "*")
            else:
                print(end = " ")
        print()