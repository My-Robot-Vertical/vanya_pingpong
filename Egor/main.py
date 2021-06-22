from graphics import *
from physics_core import *


class Ball(Vector):

    def __init__(self):
        Vector.__init__(self)
        #self.x = 0
        #self.y = 0
        #self.size = 0
        self.radius = 0
        #self.angle = 0
        #self.speed = 0
        self.fps = 100
        #self.x_save = 0
        #self.y_save = 0
        self.color = "white"
        self.g = 0
        self.real_fps = 0
        self.real_fps_timer = time()

    def draw(self):
        try:
            canvas.delete("all")
            canvas.create_oval( [self.x-self.radius,self.y-self.radius], [self.x+self.radius,self.y+self.radius], fill=self.color, outline="black")
            out_window.update()
            self.real_fps = int(1/(time()-self.real_fps_timer+0.000000000000001))
            self.real_fps_timer = time()
        except TclError:
            off_window()

    def delay(self):
        sleep(1/self.fps)


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


ball = Ball()

ball.x = 250
ball.y = 100
ball.radius = 5
ball.angle = 300
ball.speed = 1
ball.fps = 70
ball.color = "red"
#ball.g = 0.01

g = Vector(angle=0,speed=0.7)


while (test_window() and 1):
    ball.x, ball.y = mouse_coo()
    ball.draw()
    ball.delay()
    print(ball.real_fps)

MAX_FPS = 0

while (test_window()):
    if (ball.speed<0.1):
        ball.speed = 0
        ball.draw()
    else:
        ball.save_coo()
        ball.plus(g)
        ball.move()
        #ball.move_physics()
        if (ball.x-ball.radius>=0 and ball.y-ball.radius>=0 and ball.y+ball.radius<=AREA_Y and ball.x+ball.radius<=AREA_X):
            pass
        else:
            if (ball.x-ball.radius<=0 and 0<ball.angle<180 or ball.x+ball.radius>AREA_X and 180<ball.angle<360): # врезались левой или правой частью
                ball.angle = 360-ball.angle
            if (ball.y-ball.radius<=0 and 90<ball.angle<270 or ball.y+ball.radius>=AREA_Y and (ball.angle>0 or ball.angle<90)): # врезались верхней или нижней частью
                ball.angle = 540-ball.angle
                #if (ball.y+ball.radius>=AREA_Y): ball.fps = ball.fps*1.1
                if (ball.y+ball.radius>=AREA_Y): ball.speed = ball.speed/1.3
            ball.becup_coo()
            #ball.move_physics()
            ball.plus(g)
            ball.move()
        #print(ball.speed)
        ball.draw()
        ball.delay()
    MAX_FPS = max(MAX_FPS,ball.real_fps)
print("MAX_FPS",MAX_FPS) # 2200 бех numba

        #print(ball.x,ball.y,ball.angle,ball.speed) #event.x,event.y
    #x = out_window.winfo_pointerx()
    #y = out_window.winfo_pointery()






#canvas.create_rectangle(ras*4,ras*9.2,ras*5,ras*9.8,fill="grey")
#canvas.create_text(ras*7,ras*9.5,text="you must eat",font="Verdana 10",justify=CENTER,fill="black")
#out_window.mainloop()
print("END MAIN")
