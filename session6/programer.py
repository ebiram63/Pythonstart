class Language:
    def Langname(self,name):
        self.name = name

    def displayname(self):
        return self.name

    def messagename(self):
        print("welcome to ", self.name)

L1 = Language()
L1.Langname("Python")
L1.displayname()
L1.messagename()

L2 = Language()
L2.Langname("matlab")
L2.displayname()
L2.messagename()




