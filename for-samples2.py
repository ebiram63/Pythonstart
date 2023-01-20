for number in range(2,110):
    for x in range(2,number):
        if number % x == 0:
            print(number, " is ", x, "*", number / x)
            break
    else:
        print(number, " is prime")        