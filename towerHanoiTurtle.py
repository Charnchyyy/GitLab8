from turtle import *
class Pole():
    def __init__(self):

        self.xPos = 0
        self.yPos = 0

    def showPole(self):
        pu()
        goto(self.xPos,self.yPos)
        setheading(0)
        pd()
        for i in range(2):
            fd(20)
            left(90)
            fd(100)
            left(90)
            
        

p = Pole()
p.showPole()
