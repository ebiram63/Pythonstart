class program:
    Name = ""
    ID = 0



Lang = program()
Lang.Name = "Python"
Lang.ID = 1372
print(Lang.Name, " -> " ,Lang.ID)



Lang2 = program()
Lang2.Name = "Java"
Lang2.ID = 3344

print(Lang2.Name, " -> " ,Lang2.ID)

class programer:
    pass

Lang3 = programer()
Lang3.Name = "C++"
Lang3.serialnumber = 236789

print(Lang3.Name, " -> " , Lang3.serialnumber)


class API:
    color = ""
    size = 0
    shape = ""



b1 = API()
b1.color = "black" 
b1.size = 200
b1.size = 1

print(b1.color)


class Time:
    pass

def timeprint(tt):
    print(str(tt.hours) + ":" + str(tt.minutes) + ":" + str(tt.seconds))

time1  = Time()
time1.hours = 13
time1.minutes = 48
time1.seconds = 60


print(timeprint(time1))


class coordinate:
    pass

def samecoordinate(p1, p2):
    return()