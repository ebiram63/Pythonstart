"""تابعی بنویسید که سه نقطه در فضای دو بعدی بگیرد و تعیین کند که آیا این سه نقطه همراستا هستند یا نه؟"""

"""def on_slope(x1,y1, x2,y2, x3,y3):
    if(y2-y1) - (x2-x1) == 0:
        if(y3-y2) - (x3 - x2) == 0:
            print("Three points are on a line") 
    else:
        print("Two points are not on a line")"""




"""============================================================================"""
"""در مسئله قبل اگر نقاط همراستا نیستند نوع مثلث تشکیل شده را تعیین کنند (متساوی الاضلاع یا متساوی الثاقین یا قائم الزاویه یا معمولی)"""



"""============================================================================"""
"""تابعی بنویسید که تعدادی نقاط بگیرد و فاصله آن نقاط از مرکز را محاسبه کند و براساس فاصله از مرکز نقاط را مرتب کند. (پیشنهاد می شود از تابع نوشته شده در تمرین 31 استفاده شود)"""

"""
import math
  
# Function to calculate distance
def distance(*args, **kwargs):
    z2 = 0
    y2 = 0
    # Calculating distance
    for arg,kwarg in args,kwargs:
        return math.sqrt(math.pow(z2 - arg, 2) +
                    math.pow(y2 - kwarg, 2) * 1.0)
  
# Drivers Code
print("%.6f"%distance(3, 4))

"""

"""============================================================================"""
"""تابعی بنویسید که یک عدد بگیرد و تعیین کند که آیا این عدد توان کامل است یا نه؟"""

"""
import math
 
# Function to check
def Log2(x):
    return (math.log10(x) /
            math.log10(2));
 
def isPowerOfTwo(n):
    result = math.ceil(Log2(n)) == math.floor(Log2(n))
    if result == True:
        print("Yes");
    else:
        print("No");

 
isPowerOfTwo(64)

"""

 


"""============================================================================"""
"""برنامه ای بنویسید که لیستی با 10 عدد صحیح رندم ایجاد کند سپس این لیست را به دو لیست تقسیم کند یکی لیست اعداد زوج و دیگری لیست با اعداد فرد"""

"""
import random

list_ = []
even_list = []
odd_list = []
for _ in range(10):
    list_.append(random.randint(1, 1000))
#print(list_)
for i in list_:
    if i % 2 == 0:
        even_list.append(i)
    elif i % 2 == 1:
        odd_list.append(i)

print("even list is: ", even_list , "\n", "odd list is: ", odd_list)

"""


"""============================================================================"""
"""برنامه یک خطی بنویسید که لیستی از اعداد بین 0 تا 100 را که به 5 یا 6 بخش پذیر هستند ایجاد کند"""

"""
[i for i in  range(0, 100) if i % 6 == 0 && i % 5 == 0 print(i)]
"""


"""============================================================================"""
"""تابعی بنویسید که تاریخ تولد شما را بصورت تاریخ شمسی گرفته و تعیین کند تا امروز چند روز در این دنیا زندگی کرده اید."""

"""
import jdatetime

def your_birthdate():
    today = str(jdatetime.date.today())
    today_splited = today.split("-")
    your_birthdate = str(input("Please enter your birth date: "))
    your_birthdate_splited = your_birthdate.split(" ")
    print(today)
    print("today date: ", today_splited)
    print("your birthdate: ", your_birthdate_splited)

    current_year = int(today_splited[0]) - int(your_birthdate_splited[0])
    current_month = int(today_splited[1]) - int(your_birthdate_splited[1])
    current_day = int(today_splited[2]) - int(your_birthdate_splited[2])
    if current_year > 0:
        year_changed_day = current_year * 365 
    else:
         year_changed_day = 0
    day = year_changed_day + (current_month*30) + current_day
    return day
print(your_birthdate())
"""