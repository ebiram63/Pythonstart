list_7 = ['ali', '2', '4','5','hi','ali','python','program','c++','ruby']
list_77 = ['5','hi','ali','python','program']
list_777 = []

for i in list_7:
    if i not in list_77:
        list_777.append(i)
print(list_777)