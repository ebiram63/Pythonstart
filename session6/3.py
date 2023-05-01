"""تابعی بنویسید که سه نقطه در فضای دو بعدی بگیرد و تعیین کند که آیا این سه نقطه همراستا هستند یا نه"""

def position(x1,y1,x2,y2,x3,y3):
     #slope one is equal with, the slope between a and  b 
     slope1 = (y2-y1) / (x2-x1)
     #slope one is equal with, the slope between b and  c 
     slope2 = (y2-y3) / (x2 - x3)

     if slope1 == slope2:
          print("3 points are located on one line")
     else:
            print("3 points are not located on one line") 


"""========================================================"""
"""در مسئله قبل اگر نقاط همراستا نیستند نوع مثلث تشکیل شده را تعیین کنند (متساوی الاضلاع یا متساوی الثاقین یا قائم الزاویه یا معمولی)"""

import math
def checkTriangle(x1, y1, x2, y2, x3, y3):
     a = (x1 * (y2 - y3) +x2 * (y3 - y1) +x3 * (y1 - y2))
     if a == 0:
          print('These points are not shaping a Triangle')
     else:
          print('Yes there is a Triangle')

  


"""========================================================"""
"""تابعی بنویسید که تعدادی نقاط بگیرد و فاصله آن نقاط از مرکز را محاسبه کند و براساس فاصله از مرکز نقاط را مرتب کند. (پیشنهاد می شود از تابع نوشته شده در تمرین 31 استفاده شود)
تابعی بنویسید که یک عدد بگیرد و تعیین کند که آیا این عدد توان کامل است یا نه؟ """
import math
def distance(*args, **kwargs):
     # Calculating distance
     for arg,kwarg in args,kwargs:
          a = 1
          
          math_ = math.sqrt(math.pow(arg[a] - arg[a-1], 2) + math.pow(kwarg[a] - kwarg[a - 1], 2) * 1.0)
          a += 1
          return math_

print(distance())


"""========================================================"""

