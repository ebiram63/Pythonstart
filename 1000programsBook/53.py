for i in range(8 , 4, -1):
    for j in range(8, 4, -1):
        for k in range(8, 4, -1):
            for m in range(8, 4, -1):
                if (i == j or i == k or i ==m or j == k or j == m or k == m):
                    continue
                else:
                    print(i * 1000 + j * 100 + k * 10 + m , end = " \t")
                    