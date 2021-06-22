from graphity import *

simulation = graphics_area(300,300)

ball = graphics_object(x=250,y=100,type="oval",size=5,angle=300,speed=1) # ,fps=70
simulation.obj(ball) # ,fps=70

g = Vector(angle=0,speed=0.7)

while (simulation.flag and 1):
    #simulation.object[0].x, simulation.object[0].y = simulation.mouse_coo()
    ball.x, ball.y = simulation.mouse_coo()
    #print(ball.x, ball.y)
    #ball.draw()
    #ball.delay()
    #print(ball.real_fps)
    simulation.update()
