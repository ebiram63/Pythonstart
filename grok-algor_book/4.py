voted = {}

def check_voter(name):
    if voted.get(name):
        print("Kick them out");
    else:
        voted[name] = True
        print("let them vote!")


check_voter("ebi")
print(voted)
check_voter("omid")
print(voted)
check_voter("samira")
print(voted)
check_voter("ebi")
print(voted)