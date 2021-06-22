from graphics import *
from vector import *
Vector.version("1.0")

#graphics_object_array = []

class graphics_object(Vector):

    def __init__(self,angle=0,speed=0,x=0,y=0,save_mas=[0,0,0,0],save_coo_mas=[0,0], outline="black",fill="red",type="oval",size=5):
        # Vector
        Vector.__init__(self,angle=0,speed=0,x=0,y=0,save_mas=[0,0,0,0],save_coo_mas=[0,0])
        # graphics
        self.outline = outline
        self.fill = fill
        self.type = type
        self.size = size
        # id
        self.name = time()

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
            self.canvas.delete("all")
            for obj in self.object:
                if (obj.type=="oval"): self.canvas.create_oval( [obj.x-obj.size,obj.y-obj.size], [obj.x+obj.size,obj.y+obj.size], fill=obj.fill, outline=obj.outline)
                #elif (self.type=="rectangle"): self.canvas.create_rectangle
            self.window.update()
        except TclError:
            self.destroy()

    def obj(self, obj):
        '''
        f = 0
        n = 0
        for t in self.object:
            if (t.name==obj.name):
                f = 1
                break
            n+=1
        if (f): self.object[n] = obj
        else: self.object.append(obj)
        '''
        self.object.append(obj)




if __name__=="__main__":
    simulation = graphics_area(300,300)
    ball = graphics_object(x=250,y=100,type="oval",size=5,angle=300,speed=1)
    simulation.obj(ball)
    while (simulation.flag):
        ball.x, ball.y = simulation.mouse_coo()
        simulation.update()
