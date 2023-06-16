from time import sleep
def print_item(list):
    for item in list:
        sleep(1)
        print(item)

print_item([1, 2, 3, 4, 5, 6, 7])