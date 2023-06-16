
"""
    یک تابعی به نام reverseبنویسید که یک عدد صحیح (مثبت یا منفی) را دریافت کند و معکوس آنرا برگرداند
"""

"""
def reverse(number):
    if int(number) > 0:
        print(str(number)[::-1])
    else:
        #print("number is negative")
        number = str(number)
        a = number[::-1]
        print(f"{number[0]}{a[:-1]}")
        #print(a[:-1])



reverse(-1124)

"""

"""======================================================================"""

"""
    یک تابعی به نام  avglenghبنویسید که یک رشته حاوي یک جمله انگلیسی را دریافت کند و میانگین طول کلمات آنرا

برگرداند، بدیهی است که علائم نگارشی نظیر . : ؟ ! ، کلمه محسوب نمی شوند"""


"""
def avglengh(string):
    list_ = []
    list_length = []
    sum_ = 0
    list_ = string.split(" ")

    for i in list_:
        if i[-1] in  ["," , "?" , "-", "_" , "!" , "."]:
            print(i)
            #i = i[:-1]
            index = list_.index(i)
            #print(i)
            #print(index)
            list_[index] = i[:-1]


    print(list_)
    for i in list_:
        if i in  ["," , "?" , "-", "_" , "!" , "."]:
            continue
        else:
            list_length.append(len(i))
            #print(list_length)

    for i in list_length:
        sum_  += i
        print("the length of a word is: " , i)
    answer  = sum_ / len(list_length)
    print("the average is: " , answer)

avglengh("salam man ebi hastam! khob man mitonam az shoma beporsam?")

"""
"""======================================================================"""

"""    یک تابع به نام  addStringبنویسید که دو عدد را بصورت رشته متنی دریافت کند و حاصل جمع آنها را محاسبه و

بازگرداند.  """


def addString(string1, string2):
    str1 = []
    str2 = []
    dic =  {"یک" : 1 , "دو" : 2 , "سه" : 3 , "چهار" : 4, "پنج" : 5, "شش" : 6, "هفت" : 7, "هشت" : 8, "نه" : 9 , "ده" : 10, "یازده" : 11, "دوازده" : 12, "سیزده" :13  , "چهارده" : 14, "پانزده" : 15 , "شانزده" : 16 , "هفده" : 17 , "هجده" : 18 , "نوزده" : 19 , "ده" : 10, "بیست" : 20, "سی" : 30, "چهل" : 40 , "پنجاه" : 50, "شصت" : 60, "هفتاد" : 70, "هشتاد" : 80 , "نود" : 90 , "صد" : 100, "دویست" : 200 , "سیصد" : 300 , "چهارصد": 400, "پانصد" : 500, "ششصد" : 600, "هفتصد" : 700, "هشتصد" : 800 , "نهصد" : 900}
   # adadbozorg = {3: "هزار", 6: "میلیون", 9: "میلیارد", 12: "تریلیون",
    #          15: "کوآدریلیون", 18: "کوینتیلیون", 21: "سکستیلیون", 24: "سپتیلیون",
    #          27: "اکتیلیون", 30: "نانیلیون", 33: "دسیلیون", 36: "آندسیلیون",
   #           39: "دیودسیلیون", 42: "تریدسیلیون", 45: "کواتیوردسیلیون", 48: "کویندسیلیون",
     #         51: "سکسدسیلیون", 54: "سپتدسیلیون", 57: "اکتودسیلیون", 60: "نومدسیلیون"}


    str1.append(string1.split("و"))
    #print(str1)
    for j in str1:
        if j in dic.keys():
            print(j)

addString("یک" ,"یک")
    













"""======================================================================"""

"""    تابعی به نام  firstUCharبنویسید که یک رشته متنی را بعنوان ورودي بگیرد و اولین کاراکتر غیرتکراري آنرا یافته و

اندیس آن در رشته متنی را برگرداند، درصورتیکه چنین کاراکتري را پیدا نکرد عدد منفی یک را برگرداند"""



"""
def firstUChar(string = input("Please eneter your sentence: ")):
    array_letter = {}
    for i in string:
        if i in array_letter:
            array_letter[i] += 1
        else:
            array_letter[i] = 1
   #print(array_letter)
    for x in array_letter.keys():
        if array_letter[x]== 1:
            print(x)
            break


firstUChar()

"""