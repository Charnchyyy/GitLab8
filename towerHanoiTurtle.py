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

class Hanoi(object):
    def __init__(self,n = 3,start = 'A',workspace = 'B',destination = 'C'):
        self.startp = Pole(start,0,0)
        self.workspacep = Pole(workspace,150,0)
        self.destinationp = Pole(destination,300,0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        for i in range(n):
            self.startp.pushdisk(Disk,("d"+str(i),0,i*150,20,(n-1)*30))
    def move_disk(self,start,destination):
        disk = start.popdisk()
        destination.pushdisk(disk)
    def move_tower(self,n,s,d,w):
        if n == 1:
            self.mvoe_disk(s,d)
        else:
            self.move_tower(n-1,s,w,d)
            self.move_disk(s,d)
            self.move_tower(n-1,w,d,s)
    def solve(self):
        self.move_tower(3,self.starto,self.destinationp,self.workspacep)
h = Hanoi()
h.solve()
        
        
        
