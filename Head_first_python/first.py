cast = ["Cleese" , "Palin", "Jones", "Idle"]

print(cast)

print(len(cast))

print(cast[1])

cast.append("Gilliam")
print(cast)

cast.pop()
print(cast)

cast.extend(["Ebi" , "Samira"])
print(cast)

cast.remove("Ebi")
print(cast)

cast.insert(0, "Ebi")
print(cast)