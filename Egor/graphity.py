from graphics import *
from vector import *
from copy import deepcopy
Vector.version("1.0")

g = Vector(speed=0.1,angle=0)

#graphics_object_array = []

class graphics_object(Vector):

    def __init__(self,angle=0,speed=0,x=0,y=0,save_mas=[0,0,0,0],save_coo_mas=[0,0], outline="black",fill="black",type="ball",size=5, mg=0,static=0,R=0):
        # Vector
        Vector.__init__(self,angle=angle,speed=speed,x=x,y=y,save_mas=save_mas,save_coo_mas=save_coo_mas)
        self.mg = mg
        self.static = static
        self.R = R
        # graphics
        self.outline = outline
        self.fill = fill
        self.type = type
        self.size = size
        # id
        self.name = time()
        # size block
        if (self.type=="block"):
            if (len(self.size)==4):
                s = deepcopy(self.size)
                self.size = [s[0],s[1], s[2],s[1], s[2],s[3], s[0],s[3]]

    def update(self):
        # занести инфу в общий массив
        pass

    def copy(self):
        return graphics_object(angle=self.angle,speed=self.speed,x=self.x,y=self.y,save_mas=self.save_mas,save_coo_mas=self.save_coo_mas, outline=self.outline,fill=self.fill,type=self.type,size=self.size)

class graphics_area(Graphics):

    def __init__(self,AREA_X,AREA_Y): # ,fps
        Graphics.__init__(self,AREA_X,AREA_Y)
        self.object = []
        # area end
        d = 2 # чтобы граней поля не видно было
        self.object.append(graphics_object(type="line",static=1,size=[0,0,0,AREA_Y+d]))
        self.object.append(graphics_object(type="line",static=1,size=[0,AREA_Y+d,AREA_X+d,AREA_Y+d]))
        self.object.append(graphics_object(type="line",static=1,size=[AREA_X+d,AREA_Y+d,AREA_X+d,0]))
        self.object.append(graphics_object(type="line",static=1,size=[AREA_X+d,0,0,0]))

    def update(self):
        try:
            if (self.flag==0): return
            self.canvas.delete("all")
            for obj in self.object:
                # physics
                if (obj.static==0):
                    # basic
                    if (obj.mg==1): obj.plus(g)
                    if (obj.R>0): obj.speed*=1-obj.R
                    obj.move() # вернуть сюда! (для того, чтобы все динамические объекты реагировали друг на друга)
                    # contact with more obj
                    for obj_new in self.object:
                        if (obj_new!=obj):
                            pass # нужно line_gradus_numba в vector
                    if (obj.type=="ball"):
                        if (obj.x-obj.size<=0 and 0<obj.angle<180 or obj.x+obj.size>=self.AREA_X and 180<obj.angle<360): # врезались левой или правой частью
                            #obj.angle = 360-obj.angle
                            obj.mirror(0) # нужно line_gradus_numba в vector
                            print("!!")
                        if (obj.y-obj.size<=0 and 90<obj.angle<270 or obj.y+obj.size>=self.AREA_Y and (obj.angle>270 or obj.angle<90)): # врезались верхней или нижней частью
                            #obj.angle = 540-obj.angle
                            obj.mirror(90)
                            print("!")
                        #print(obj.y+obj.size,obj.angle)

                    #obj.move()

                # area
                '''
                if (obj.type=="ball"):
                    if (ball.x-ball.radius<=0 and 0<ball.angle<180 or ball.x+ball.radius>AREA_X and 180<ball.angle<360): # врезались левой или правой частью
                        ball.angle = 360-ball.angle
                    if (ball.y-ball.radius<=0 and 90<ball.angle<270 or ball.y+ball.radius>=AREA_Y and (ball.angle>0 or ball.angle<90)): # врезались верхней или нижней частью
                        ball.angle = 540-ball.angle
                '''

                # image
                if (obj.type=="ball"): self.canvas.create_oval( [obj.x-obj.size,obj.y-obj.size], [obj.x+obj.size,obj.y+obj.size], fill=obj.fill, outline=obj.outline)
                elif (obj.type=="line"): self.canvas.create_line(obj.size[0],obj.size[1],obj.size[2],obj.size[3],width=1,fill=obj.fill)
                elif (obj.type=="block"):
                    for i in range (0,len(obj.size)-3,2):
                        self.canvas.create_line(obj.size[i],obj.size[i+1],obj.size[i+2],obj.size[i+3],width=1,fill=obj.fill)
                    self.canvas.create_line(obj.size[0],obj.size[1],obj.size[len(obj.size)-2],obj.size[len(obj.size)-1],width=1,fill=obj.fill)
                    #self.canvas.create_rectangle
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

    # добавление функции выключения окна по клику мыши
    I=0
    def destroy():
        global I
        I+=1
        if (I>=2): simulation.destroy()
    simulation.add_click(destroy)

    block = graphics_object(x=250,y=100,type="block",size=[100,100,150,250],angle=300,speed=1)
    ball = graphics_object(x=250,y=100,type="ball",fill="red",size=5,angle=300,speed=1)
    simulation.obj(block)
    simulation.obj(ball)
    while (simulation.flag):
        ball.x, ball.y = simulation.mouse_coo()
        simulation.update()
    #print(simulation.object)
