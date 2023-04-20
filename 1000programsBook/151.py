rows = int(input("Input rows: "))
for i in range(1, (rows * 2)):
    for j in range(1, rows + 1):
        if i == 1 and (j == 1 or j == rows ) or \
        (i == rows and (j == 1 or j == rows ) or \ 
         i == rows * 2 - 1 and  (j == 1 or j == rows))):
         