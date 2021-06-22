#from random import * # x0 = randint(0, 100)
#from copy import deepcopy
from time import sleep,time
from math import sin, cos, radians, degrees, atan2

from numba import njit

'''
vector angle:

  135 180 225
      \|/
   90 -o- 270
      /|\
    45 0 315

'''

Vector_version = "1.0"

class coo:

    def __init__(self,x,y):
        self.x = x
        self.y = y

class Vector:

    def version(self=0, S=0):
        if (isinstance(self, float) or isinstance(self, str)): S = str(self)
        elif (S!=0): S = str(S)
        #version = "1.0"
        #print(S)
        if (S==0):
            return Vector_version
        if (S==Vector_version):
            return 1
        else:
            print("<physics_core> have more version!!!")
            return 0

    def __init__(self,angle=0,speed=0,x=0,y=0,save_mas=[0,0,0,0],save_coo_mas=[0,0]):
        self.angle = angle
        self.speed = speed
        self.x = x
        self.y = y
        self.save_mas = save_mas
        self.save_coo_mas = save_coo_mas
        #self.privat_old_coo = [x,y]
        #self.size = 0
        #self.radius = 0
        #self.fps = 100
        #self.g = 0.7

    def save(self): self.save_mas = [self.angle,self.speed,self.x,self.y]
    def becup(self): [self.angle,self.speed,self.x,self.y] = self.save_mas
    def save_coo(self): self.save_coo_mas = [self.x,self.y]
    def becup_coo(self): [self.x,self.y] = self.save_coo_mas

    def constrain_angle(self): self.angle = constrain_angle_numba(self.angle)
    def move(self): self.x,self.y = move_numba(self.angle,self.speed, self.x,self.y)
    def plus(self, new_vector): self.speed,self.angle = plus_numba(self.speed,self.angle,new_vector.speed,new_vector.angle)
    def inversion(self): self.angle = inversion_numba(self.angle)
    def mirror(self, mirror_angle): self.angle = mirror_numba(self.angle,mirror_angle)

    def copy(self):
        return Vector(angle=self.angle,speed=self.speed,x=self.x,y=self.y,save_mas=self.save_mas,save_coo_mas=self.save_coo_mas)

@njit
def constrain_angle_numba(angle):
    while (angle<0): angle+=360
    while (angle>=360): angle-=360
    return angle

@njit
def move_numba(angle, speed, x,y):
    angle = constrain_angle_numba(angle)
    x-=speed*sin(radians(angle))
    y+=speed*cos(radians(angle))
    return x,y

@njit
def plus_numba(speed_1,angle_1,speed_2,angle_2):
    angle_1 = constrain_angle_numba(angle_1)
    angle_2 = constrain_angle_numba(angle_2)
    # вычисляем дельты
    dx = sin(radians(angle_1))*speed_1+sin(radians(angle_2))*speed_2
    dy = cos(radians(angle_1))*speed_1+cos(radians(angle_2))*speed_2
    # убираем очень малые значения
    if (abs(dx)<0.000001*speed_1): dx = 0
    if (abs(dy)<0.000001*speed_1): dy = 0
    #print(dx, dy)
    # находим новые параметры
    speed_1 = (dy**2+dx**2)**(1/2)
    angle_1 = degrees(atan2(dx,dy))
    angle_1 = constrain_angle_numba(angle_1)
    return speed_1,angle_1

@njit
def inversion_numba(angle):
    angle+=180
    return constrain_angle_numba(angle)

@njit
def mirror_numba(angle,mirror_angle):
    angle = constrain_angle_numba(angle)
    mirror_angle = constrain_angle_numba(mirror_angle)
    angle = inversion_numba(angle) - 2*(90+angle-mirror_angle)
    return constrain_angle_numba(angle)


if __name__=="__main__":
    Vector.version("1.0")

    g = Vector()
    g.speed = 1
    g.angle = 90
    #g.constrain_angle()
    #g.move()
    #print(g.angle)
    if (0): # sum test
        a = Vector()
        a.speed = 1
        a.angle = 0#270
        g.plus(a)
        print(g.speed,g.angle)
    if (0): # copy test
        g1 = g.copy()
        print(g1.speed,g1.angle)
        g1.inversion()
        print(g1.speed,g1.angle)
        g.plus(g1)
        print(g.speed,g.angle)
    if (1): # mirror test
        #g.angle = 45
        g.mirror(45)
        print(g.angle)
