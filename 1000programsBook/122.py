"""برنامه ای که مختصات دو مستطیل را گرفته و مساحت ناحیه ی مشترک بین دو مستطیل را حساب میکند. به ازاء هر مستطیل دونقطه چهار عدد اعشاری باید وارد شود"""


x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
x3 = int(input("Enter x3: "))
y3 = int(input("Enter y3: "))
x4 = int(input("Enter x4: "))
y4 = int(input("Enter y4: "))

if x1 > x2:
    temp = x1
    x1 = x2
    x2 = temp
    temp = y1 
    y1 = y2
    y2 = temp
if y1 > y2:
    temp = y1
    y1 = y2
    y2 = temp
if x3 > x4:
    temp = x3
    y3 = y4
    y4 = temp
if x1 < x4 and x4 < x2:
    if x1 < x3 and x3 < x2:
        xLength = x4 - x3
    else:
        xLength = x4 - x1
else:
    if x1 < x3 and x3 < x2:
        xLength = x2 - x3
    else:
        xLength = 0
if y1 < y4 and y4 < y2:
    if y1 < y3 and y3 < y2:
        yLength = y4 - y3
    else:
        yLength = y4 - y1
else:
    if y1 < y3 and y3 < y2:
        yLength = y2 - y3
    else:
        yLength = 0
print(xLength * yLength)
