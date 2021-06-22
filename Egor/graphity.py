#from graphics import *
from physics_core import *

from tkinter import *

Vector.version("1.0")

class graphics_object(Vector):

    def __init__(self,angle=0,speed=0,x=0,y=0,save_mas=[0,0,0,0],save_coo_mas=[0,0], outline="black",fill="red",type="oval",size=5):
        # Vector
        self.angle = angle
        self.speed = speed
        self.x = x
        self.y = y
        self.save_mas = save_mas
        self.save_coo_mas = save_coo_mas
        # graphics
        self.outline = outline
        self.fill = fill
        self.type = type
        self.size = size

    def copy(self):
        return graphics_object(angle=self.angle,speed=self.speed,x=self.x,y=self.y,save_mas=self.save_mas,save_coo_mas=self.save_coo_mas, outline=self.outline,fill=self.fill,type=self.type,size=self.size)

class graphics_area:

    def __init__(self,AREA_X,AREA_Y):
        self.object = []
        self.window = Tk()
        self.window.title('graphics_area')
        self.canvas = Canvas(self.window,width=AREA_X,height=AREA_Y,bg="white")
        self.canvas.pack()
        self.AREA_X = AREA_X
        self.AREA_Y = AREA_Y

        self.flag = 1

    def update(self):
        if (self.flag==0): return
        #self.canvas.delete("all")
        for obj in self.object:
            if (obj.type=="oval"): self.canvas.create_oval( [obj.x-obj.size,obj.y-obj.size], [obj.x+obj.size,obj.y+obj.size], fill=obj.fill, outline=obj.outline)
            #elif (self.type=="rectangle"): self.canvas.create_rectangle
        self.window.update()

    def destroy(self):
        self.flag = 0
        self.window.destroy()

    def mouse_coo(self):
        return self.window.winfo_pointerx()-1,self.window.winfo_pointery()-82

    #def click(event):
    #        pass
    #    out_window.destroy()
        #print(event.x, event.y, mouse_coo())




if __name__=="__main__":
    ball = graphics_object()
    print(ball.x)
    simulation = graphics_area(300,300)
    t = time()
    while (t+2>time()):
        simulation.update()
    simulation.destroy()
