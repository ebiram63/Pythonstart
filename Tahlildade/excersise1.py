number = int(input("insert your number: "))

if number > 365:
    reminder = number % 365
    year = number // 365

    #yeartomonth = year * 12
    month = reminder // 30 #+ #yeartomonth
    reminder = reminder % 30
    day = reminder 
    
    print ("year = ", year , "month = ", month , "day = ", day) 
else:
    print("It is year = 0")
