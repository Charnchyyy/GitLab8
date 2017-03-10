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

class disk:
    def __init__(self,name,x,y,height,width,color):
        self.name = name
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
    def showdisk(self):
        goto(self.x,self.y)
        begin_fill()
        color(str(self.color))
        fd(self.width/2)
        lt(90)
        fd(self.height)
        lt(90)
        fd(self.width)
        lt(90)
        fd(self.height)
        lt(90)
        fd(self.width/2)
        end_fill()
    def newpos(self,newx,newy):
        self.x = newx
        self.y = newy
        penup()
        goto(self.x,self.y)
        pendown()
    def cleardisk(self):
        goto(self.x,self.y)
        begin_fill()
        color('white')
        fd(self.width/2)
        lt(90)
        fd(self.height)
        lt(90)
        fd(self.width)
        lt(90)
        fd(self.height)
        lt(90)
        fd(self.width/2)
        end_fill()
        
        
        
