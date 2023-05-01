"""برنامه ای که مختصات سه نقطه را میگیرد و مشخص میکند که این سه نقطه در یک راستا هستند یا نه اگر باشند """
"""It means : ax + by + c = 0"""

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
x3 = int(input("Enter x3: "))
y3 = int(input("Enter y3: "))

m1 = (y2 - y1) / (x2 - x1)
m2 = (y3 - y1) / (x3 - x1)
if m1 != m2:
    print("No")
else:
    print("Y -", y1, " = ", m1, "(x - " , x1, ") ")