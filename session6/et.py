
dict1 = {"name": "Dhushi", "age": 6}
dict2 = {"name": "Dhushi", "age": 3}
result = all([dict2.get(key) == value for key, value in dict1.items()])
print(result)