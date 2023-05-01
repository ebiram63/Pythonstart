n = int(input("Please Enter your number: "))
if n > 80 or n < 0:
    print("Invalid number")
else:
    for i in range(1 , n + 1):
        for j in range(1 , n + 1):
            print(end = "*")
        print()