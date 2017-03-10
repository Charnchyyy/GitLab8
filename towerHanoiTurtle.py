from turtle import *
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
class Pole(disk):
    def __init__(self,name,stack,top=0,xPos,yPos,thick,length,color):

        self.name = name
        self.stack = stack
        self.top = top
        self.xPos = xPos
        self.yPos = yPos
        self.thick = thick
        self.length = length
        self.color = color
        

    def showPole(self):
        pu()
        goto(self.xPos,self.yPos)
        setheading(0)
        pd()
        begin_fill()
        color(str(self.color))
        for i in range(2):
            fd(self.thick)
            left(90)
            fd(self.length)
            left(90)
        end_fill()

    def pushdisk(self,disk):
        
    
        
p = Pole()
p.showPole()
