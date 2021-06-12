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
        #self.size = 0
        self.radius = 0
        self.angle = 0
        self.speed = 0
        self.fps = 100
        self.x_save = 0
        self.y_save = 0
        
    def draw(self):
        canvas.delete("all")
        canvas.create_oval( [self.x-self.radius,self.y-self.radius], [self.x+self.radius,self.y+self.radius], fill="white", outline="black")
        out_window.update()
        
    def delay(self):
        sleep(1/self.fps)
        
    def move(self):
        self.x-=self.speed*sin(radians(self.angle))
        self.y+=self.speed*cos(radians(self.angle))
        
    def save_coo(self):
        self.x_save = self.x
        self.y_save = self.y
        
    def becup_coo(self):
        self.x = self.x_save
        self.y = self.y_save
        
ball = Vector()
    
ball.x = 250
ball.y = 100
ball.radius = 5
ball.angle = 300
ball.speed = 1
ball.fps = 200
    


canvas.pack()

while (1):
    ball.save_coo()
    ball.move()
    if (ball.x-ball.radius>=0 and ball.y-ball.radius>=0 and ball.y+ball.radius<=AREA_Y and ball.x+ball.radius<=AREA_X):
        pass
    else:
        print("!!!")
        if (ball.x-ball.radius<=0 or ball.x+ball.radius>=AREA_X): # врезались левой или правой частью
            ball.angle = 360-ball.angle
        if (ball.y-ball.radius<=0 or ball.y+ball.radius>=AREA_Y): # врезались верхней или нижней частью 
            ball.angle = 540-ball.angle
        ball.becup_coo()
        ball.move()
    #ball.x+=1
    #ball.y+=1
    ball.draw()
    ball.delay()
    #print(ball.x,ball.y)
    
    


        
    
        
    '''
    def click(event):
        pass
    
    #canvas.create_rectangle(ras*4,ras*9.2,ras*5,ras*9.8,fill="grey")
    #canvas.create_text(ras*7,ras*9.5,text="you must eat",font="Verdana 10",justify=CENTER,fill="black")
    
    canvas.bind("<Button-1>", click)

    canvas.pack()
    out_window.mainloop()
    #in_window.mainloop()
    '''
out_window.mainloop()