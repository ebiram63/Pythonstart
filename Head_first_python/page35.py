"""This is the "nester.py" modul,and it provides
one function called print_lol() which prints lists
 that may or may not include nested lists"""
def print_lol(the_list):
    """This function takes a positional argument called "thelist", which 
    is any Python list (of,possibly,nested lists).Each data item in the provided
      list is (recursively) printed to the screen on its own line"""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)



movies = ["The Holy Grail", 1975, "Terry ones", 91, "Graham Chapman", ["Michael Palin", "ohan Cleese", "Terry Gilliem"]]

print_lol(movies)