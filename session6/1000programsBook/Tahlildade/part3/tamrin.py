print("==============tamrin 1 =================")

num = int(input("Please enter your number: "))

for i in range(3):
    print("*" * num)
    if i == 2:
        break
    else:
        for j in range(num-1):
            print("*")

print("==============tamrin 2 =================")

string = []

while(True): 
    word = input("Please enter your str: ")
    if word.lower() == 'break':
        break
    else:
        string.append(word)
print(string)

print("==============tamrin 3 =================")

num_list = []
for i in range(10):
    num_list.append(input("Please enter a number: "))

num_list.sort()

print(num_list)

print("==============tamrin 4 =================")

num_list2 = ['1', '2', '3', '4', '5', '6']

sum_num = 1
count_num = len(num_list2)
for i in range(count_num):
    sum_num *= int(num_list2[i]) 
print(sum_num)

print("==============tamrin 5 =================")

 
list_5 = ['ali', '2', 'hi', '4', '5','5','hi','ali']
list_55 = []
for i in list_5:
    if i in list_55:
        continue
    else:
        list_55.append(i)
print(list_55)

print("==============tamrin 6 =================")

list_6 = ['ali', '2', '4','5','hi','ali','python','program','c++','ruby']
list_66 = ['5','hi','ali','python','program']
list_666 = []

for i in list_6:
    if i in list_66:
        list_666.append(i)
print(list_666)

print("==============tamrin 7 =================")

list_7 = ['ali', '2', '4','5','hi','ali','python','program','c++','ruby']
list_77 = ['5','hi','ali','python','program']
list_777 = []

for i in list_7:
    if i not in list_77:
        list_777.append(i)
print(list_777)
