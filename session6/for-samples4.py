
for num in range(2,20):
    for s in range(2,num):
        if num % s == 0:
            continue
    print(num)    