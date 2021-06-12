from tkinter import *
from random import * # x0 = randint(0, 100)
from copy import deepcopy
from time import sleep,time
from math import sin, cos, radians, degrees, atan2

AREA_X = 300
AREA_Y = 300

out_window = Tk()
out_window.title('pingpong')
canvas = Canvas(out_window,width=AREA_X,height=AREA_Y,bg="white")

flag_window = 1
def off_window():
    global flag_window
    flag_window = 0
    
def click(event):
    off_window()
    out_window.destroy()
    
canvas.bind("<Button-1>", click)
canvas.pack()


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
        self.color = "white"
        self.g = 0.7
        
    def draw(self):
        try:
            canvas.delete("all")
            canvas.create_oval( [self.x-self.radius,self.y-self.radius], [self.x+self.radius,self.y+self.radius], fill=self.color, outline="black")
            out_window.update()
        except TclError:
            off_window()
        
    def delay(self):
        sleep(1/self.fps)
        
    def move(self):
        while (self.angle<0): self.angle+=360
        while (self.angle>360): self.angle-=360
        self.x-=self.speed*sin(radians(self.angle))
        self.y+=self.speed*cos(radians(self.angle))
        
    def move_physics(self):
        # устранение критических угловых значений
        while (self.angle<0): self.angle+=360
        while (self.angle>360): self.angle-=360
        # просчет прямолинейного движения
        dx = self.speed*sin(radians(self.angle))
        dy = self.speed*cos(radians(self.angle))
        # добавления силы тяжести
        dy = dy+self.g #self.g
        self.speed = (dy**2+dx**2)**(1/2)
        self.angle = degrees(atan2(dx,dy))
        # устранение критических угловых значений
        while (self.angle<0): self.angle+=360
        while (self.angle>360): self.angle-=360
        # вычисление новых координат
        self.x-=dx
        self.y+=dy
        #self.y-=1
        
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
ball.fps = 70
ball.color = "red"
ball.g = 0.01
    



while (flag_window):
    if (ball.speed<0.01):
        ball.speed = 0
        ball.draw()
    else:
        ball.save_coo()
        ball.move_physics()
        if (ball.x-ball.radius>=0 and ball.y-ball.radius>=0 and ball.y+ball.radius<=AREA_Y and ball.x+ball.radius<=AREA_X):
            pass
        else:
            #print("!!!")
            if (ball.x-ball.radius<=0 and 0<ball.angle<180 or ball.x+ball.radius>AREA_X and 180<ball.angle<360): # врезались левой или правой частью
                ball.angle = 360-ball.angle
            if (ball.y-ball.radius<=0 and 90<ball.angle<270 or ball.y+ball.radius>=AREA_Y and (ball.angle>0 or ball.angle<90)): # врезались верхней или нижней частью 
                ball.angle = 540-ball.angle
                if (ball.y+ball.radius>=AREA_Y): ball.speed = ball.speed/1.3
            ball.becup_coo()
            ball.move_physics()
        ball.draw()
        ball.delay()
        #print(ball.x,ball.y,ball.angle,ball.speed) #event.x,event.y
    #x = out_window.winfo_pointerx()
    #y = out_window.winfo_pointery()
    


        
    

    
#canvas.create_rectangle(ras*4,ras*9.2,ras*5,ras*9.8,fill="grey")
#canvas.create_text(ras*7,ras*9.5,text="you must eat",font="Verdana 10",justify=CENTER,fill="black")
#out_window.mainloop()