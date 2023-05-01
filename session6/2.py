"""تابعی بنویسید که یک لیست به عنوان آرگومان ورودی گرفته و یک لیست بصورت برعکس لیست اول خروجی دهد."""


"""
def reversing(list1):
    print(list1)
    list2 = list1.reverse()
    print(list2)
    print(list1)
    


reversing([1, 2, 3, 4, 5])

"""


"""=============================================================================="""
"""تابعی بنویسید یک لیست بصورت ترکیبی از استزینگ و ارقام گرفته و بزرگترین مقدار لیست را خروجی دهد. (بزرگترین مقدار = استرینگی با بیشترین طول یا عددی با بیشترین مقدار)"""

"""
def get_max(lst, fallback=''):
    intlist = []
    strlist = []
    if not lst:
        return fallback
    for i in lst:    
        if type(i) == int or type(i) == float:
            intlist.append(i)
        elif(type(i) == str):    
            strlist.append(i)
    print("max in numbers is: " , max(intlist) ,"\b", "max strings is: ", max(strlist, key=len))

get_max(["sdasssadsdasdasdasdasasa",2,"asasasssaaqa",8,99])
"""

"""=============================================================================="""
"""تابعی بنویسید برای کنترل سرعت خودرو: این تابع یک آرگومان میگیرد که نمایانگر سرعت است. اگر سرعت کمتر از 70 باشد مقادر "good" بر می گرداند. در غیر اینصورت به ازای هر 5 کیلومتر سرعت بیشتر از مقدار مجاز 70 یک امتیاز منفی به راننده می دهد و در آخر مجموع میزان امتیاز منفی را خروجی می دهد. مثلا اگر سرعت 80 باشد امتیاز منفی 2 را خروجی می دهد. و اگر یک راننده بیشتر از 12 امتیاز منفی داشته باشد گواهینامه راننده باطل شده و تابع پیام "گواهینامه شما باطل شد" را پرینت می گیرد"""


"""
def userspeed(speed):
    if speed < 70:
        print("good")
    else:
        penalty = (int(speed) - 70) / 5
        if penalty > 12:
            print("Your license has been revoked")
        else:
            print(penalty)

userspeed(135)
"""

"""=============================================================================="""
"""تابعی بنویسید که فاصله اقلیدسی دو نقطه a,b را در فضای دو بعدی حساب کند. """
import math

"""
#firstspot = (x1,x2)
#secondspot = (y1,y2)
def mathspots(x1,y1,x2,y2):
    print(math.sqrt((x1-x2)^2 + (y1-y2)^2)) 

mathspots(67,83,63,97)

"""