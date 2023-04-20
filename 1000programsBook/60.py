s = input("Enter a sentence: ")
couter = 0;
for ch in s:
    if '0' <= ch <= '9':
        couter += 1
print(couter)