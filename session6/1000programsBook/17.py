# The program calculates inflation rate

amt = int(input("Enter amount: "))
rate = float(input("Enter rate: "))
years = int(input("Enter year: "))
future_value = amt*((1 + (0.01*rate)) ** years)
print("Future_value is %12.0f" %(future_value))
