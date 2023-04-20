for i in range(1000, 10000):
    num = i 
    p = 1 
    while num > 0:
        r = num % 10
        p *= r
        num //=10
    sum = 0
    for j in range(1,  p):
        if p % j == 0:
            sum += j
    if p == sum and p != 0:
        print(i  , end = '\t')