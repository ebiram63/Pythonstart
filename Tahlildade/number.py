#the number is odd or even 

name = str(input("What's your name? "))
print("Welcome  ", name , "to the game")

number = int(input("insert your number :"))




if number % 2 != 0:
    print("the numebr is odd")
else: 
    print("the numebr is even")
