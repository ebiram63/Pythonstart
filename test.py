#Odd or Even
num = int(input("Please Insert your number: "))

if num < 100:
    if num % 2 == 0:
        if num % 3 == 0:
            print(num)
        else:
            print(num * 3)

    else:
        print("The Number is Out Of Range") 
           