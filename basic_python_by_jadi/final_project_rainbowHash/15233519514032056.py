import hashlib
import csv


with open("C:/Python/basic_python_by_jadi/final_project_rainbowHash/1.csv", "r") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row[1])



#def hash_password_hack(input_file_name, output_file_name):
    


