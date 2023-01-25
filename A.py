class A:
    number = 0
    def pos(self,x):
        if x < 3:
            x+= -x
        self.number = x

num = A()
num.pos(-4)
num.number

class A:
    def __init__(self):
        print("Hello!")
        print("2022")

B = A()
