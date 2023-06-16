"""برنامه ای بنویسید که محتوای یک فایل متنی را در فایل دیگری کپی کند"""

"""
with open('first.txt','r') as firstfile, open('second.txt','a') as secondfile:
    for line in firstfile:
        secondfile.write(line)
firstfile.close()
secondfile.close()


OR

import shutil
shutil.copyfile('first.txt','second.txt')
firstfile.close()
secondfile.close()

"""

"""==========================================================="""

"""تابعی بنویسید که یک فایل را گرفته و مشخصات آن فایل شامل تعداد کاراکترها، نام، تاریخ ایجاد به شمسی و میلادی، تعداد کلمات  را در یک فایل دیگری ذخیره کند"""

"""
import os
import time

file_path = "C:/Python/first.txt"

file_creation_date = os.path.getctime(file_path, )
file_size = os.path.getsize(file_path)
#print(file_creation_date)
c_time = os.path.getctime(file_path)
local_time = time.ctime(c_time)


print(file_size, "bytes ")
print("file_creation_date:", local_time) 

"""


"""==========================================================="""

"""تابعی بنویسید که یک کلمه خاص در یک فایل متنی را با کلمه دلخواه جایگزین کند"""


"""
def replace_word_textfile(search_text):
    replaced_word = "USA" 
    with open(r'text.txt', 'r') as file:
        data = file.read()
        data = data.replace(search_text, replaced_word)
    with open(r'text.txt', 'w') as file:
        file.write(data)
    

    print("Text replaced")


#replace_word_textfile("Turkmenistan")

"""


"""==========================================================="""

"""تابعی بنویسید که n  خط اول یک فایل را بخواند. (n آرگومان ورودی تابع است)"""

"""
n = 2
filename = 'C:/Python/text.txt'
with open(filename) as my_file:
    head = my_file.readlines()[:n]
    
print(head)

"""


"""==========================================================="""


"""تابعی بنویسید که n خط آخر یک فایل را بخواند"""

"""
def count_lines_text_file(n):
    with open(r"C:/Python/text.txt", 'r') as file:
        lines = len(file.readlines())
        last_line = file.readlines()[-1]
        print(last_line)



count_lines_text_file(1)

"""

"""OR"""

"""
import os
with open("text.txt", "rb") as file:
    try:
        file.seek(-2, os.SEEK_END)
        while file.read(1) != b'\n':
            file.seek(-2, os.SEEK_CUR)
    except OSError:
        file.seek(0)
    last_line = file.readline().decode()
print(last_line)

"""