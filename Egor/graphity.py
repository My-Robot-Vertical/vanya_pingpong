from graphics import *
from vector import *
#from tkinter import *

Vector.version("1.0")



graphics_object_array = []

class graphics_object(Vector):

    def __init__(self,angle=0,speed=0,x=0,y=0,save_mas=[0,0,0,0],save_coo_mas=[0,0], outline="black",fill="red",type="oval",size=5):
        # Vector
        Vector.__init__(self,angle=0,speed=0,x=0,y=0,save_mas=[0,0,0,0],save_coo_mas=[0,0])
        # graphics
        self.outline = outline
        self.fill = fill
        self.type = type
        self.size = size

    def update(self):
        # занести инфу в общий массив
        pass

    def copy(self):
        return graphics_object(angle=self.angle,speed=self.speed,x=self.x,y=self.y,save_mas=self.save_mas,save_coo_mas=self.save_coo_mas, outline=self.outline,fill=self.fill,type=self.type,size=self.size)

class graphics_area(Graphics):

    def __init__(self,AREA_X,AREA_Y):
        Graphics.__init__(self,AREA_X,AREA_Y)
        self.object = []

    def update(self):
        try:
            if (self.flag==0): return
            #self.canvas.delete("all")
            for obj in self.object:
                if (obj.type=="oval"): self.canvas.create_oval( [obj.x-obj.size,obj.y-obj.size], [obj.x+obj.size,obj.y+obj.size], fill=obj.fill, outline=obj.outline)
                #elif (self.type=="rectangle"): self.canvas.create_rectangle
            self.window.update()
        except TclError:
            self.destroy()




if __name__=="__main__":
    ball = graphics_object()
    print(ball.x)
    simulation = graphics_area(300,300)
    t = time()
    while (t+2>time()):
        simulation.update()
    simulation.destroy()
