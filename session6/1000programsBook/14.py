#The program that get x as a variable and without * calculates y = 31 * x -17 * x + 5 

x = int(input("Enter x: "))
m = (x << 5) - x
n = -((x << 4) + x)
y = m + n + 5
print("y = ", y)