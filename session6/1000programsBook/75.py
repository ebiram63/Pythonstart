n = int(input("Please eneter n: "))
if n > 80 or  n < 0:
    print("Invalid number")
else:
    for i in range(1, n  + 1):
        for j in range(1 , n + 1):
            if i == 1 or j == n or j >= i:
                print(end = "*")
            else:
                print(end = " ")
        print()