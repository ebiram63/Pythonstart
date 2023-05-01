number = int(input("Enter the number: "))

if number > 1:
    for x in range(2,number):
        if number % x == 0:
            print(number," is not prime")
            break
    else:
        print(number," is prime")
else:
    print(number, "is not in range")            
