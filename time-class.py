

class coodinate:
    pass

def samecoordinate(p1,p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

class Time:
    def timeprint(tt):
        print(str(tt.hours) + " : " + str(tt.minutes) + " : " + str(tt.seconds))


time1 = Time()
time1.hours = 12
time1.minutes = 0
time1.seconds = 20
time1.timeprint()

class Language:
    def Langname(self,name):
        self.name = name
    def displayname(self):
        return self.name
    def messagename(self):
        print("welcome to " + self.name)        

L1 = Language()
L1.Langname("Python")
L1.displayname()      
L1.messagename()

L2 = Language()
L2.Langname("matlab")
L2.displayname()