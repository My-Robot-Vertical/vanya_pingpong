from tkinter import *
from random import * # x0 = randint(0, 100)
from copy import deepcopy
#import time
from time import sleep
from time import time

from math import sin, cos, radians

AREA_X = 300
AREA_Y = 300

out_window = Tk()
out_window.title('pingpong')
canvas = Canvas(out_window,width=AREA_X,height=AREA_Y,bg="white")

class Vector:
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 0
        self.angle = 0
        self.speed = 0
        
    def draw(self):
        canvas.delete("all")
        canvas.create_oval( [self.x,self.y], [self.x+self.size,self.y+self.size], fill="red", outline="black")
        out_window.update()
        
    def delay(self):
        sleep(1/self.speed)
        
ball = Vector()
    
ball.x = 250
ball.y = 10
ball.size = 10
ball.angle = 273
ball.speed = 20
    


canvas.pack()

while (1):
    old_coo = [ball.x, ball.y]
    ball.x-=ball.speed*sin(radians(ball.angle))
    ball.y+=ball.speed*cos(radians(ball.angle))
    if (ball.x>=0 and ball.y>=0 and ball.y+ball.size<=AREA_Y and ball.x+ball.size<=AREA_X):
        pass
    else:
        print("!!!")
        if (ball.x<=0): # врезались левой частью
            ball.angle = 360-ball.angle
        if (ball.y<=0): # врезались верхней частью
            pass
        if (ball.x+ball.size>=AREA_X): # врезались правой чстью
            ball.angle = 360-ball.angle
        if (ball.y+ball.size>=AREA_Y): # врезались нижней чстью
            pass
        ball.x = old_coo[0]
        ball.y = old_coo[1]
        ball.x-=ball.speed*sin(radians(ball.angle))
        ball.y+=ball.speed*cos(radians(ball.angle))
    #ball.x+=1
    #ball.y+=1
    ball.draw()
    ball.delay()
    print(ball.x,ball.y)
    #canvas.create_rectangle(ras*4,ras*9.2,ras*5,ras*9.8,fill="grey")
    #canvas.create_text(ras*7,ras*9.5,text="you must eat",font="Verdana 10",justify=CENTER,fill="black")


        
    
        
    '''
    def click(event):
        pass
    
    canvas.bind("<Button-1>", click)

    canvas.pack()
    out_window.mainloop()
    #in_window.mainloop()
    '''
out_window.mainloop()