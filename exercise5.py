"""برنامه ای بنویسید که یک مقدار لیست را گرفته و تعیین کند که آیا مقادیر درون آن به ترتیب صعودی مرتب شده اند یا نه؟"""


"""Enterence = input("Please enter your numeric list: (sample: 123456): ")
list2 = list(Enterence)
for i in range(len(list2) - 1):
    if list2[i] < list2[i+1]:
        status = 1
    else:
        status = 0
if status == 1:
    print("Your number are in turn")
else:
    print("Your list is not in turn")  """  

"""========================================================"""

"""برنامه ای بنویسید که یه جمله گرفته و تعیین کند که کدامیک از حروف صدا دار در آن متن وجود دارد. خروجی بصورت لیست برگرداند و مقدار تکراری در این لیست نباشد"""

"""enterence = input("Please enter your sentence: ")
vowel = {'a' : 0 , 'e' : 0 , 'i' : 0, 'o' :  0, 'u' : 0}
for i in enterence:
    if i in vowel:
        vowel[i] += 1
print(vowel)"""

"""========================================================"""


"""لیستی از اعداد فرد بین ۰ تا ۵۰ ایجاد کنید در این لیست بگردید و اعدادی که بر ۵ یا ۳ بخشپذیر است را به انتهای همان لیست append کنید"""


"""mylist = []

for i in range(50):
    if i % 2 != 0:
        mylist.append(i)
print(mylist)

# coping list
mylist2 = mylist.copy()

for j in mylist:
    if j % 3 == 0 or j % 5 == 0:
        mylist2.append(j)
    else:
            continue
print(mylist2)"""

"""========================================================"""

""" لیستی به طول ۱۰۰ آیتم ایجاد کنید برای هر آیتم لیست بصورت رندم یکی رشته های زیر را انتخاب کنید (راهنمایی : برای این هدف می تونید از کتابخانه random و تابع choice استفاده کنید) _ آیتم های انتخابی: hello, yello, mello, hallo"""
"""در لیست تولید شده تمرین قبل آیتم های دارای غلط املایی را حذف کنید. (یعنی هر آیتمی که hello نیست)"""

"""
import random

list3 = []
for _ in range(100):
    list3.append(random.choice(('yello', 'mello' , 'hallo', 'hello')))
print(list3)


list4 = list3.copy()
counter1 = 0
for i in list4:
    if i != "hello":
        counter1 += 1
        list3.remove(i)
print("Edited list is: ", list4)
print("The number of deleted items are : ", counter1)
"""


