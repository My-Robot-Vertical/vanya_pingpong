from graphity import *

simulation = graphics_area(300,300) # ,fps=70

ball = graphics_object(x=250,y=100,type="ball",fill="red",size=5,angle=300, speed=1,mg=1) # ,R=0.01
simulation.obj(ball) # ,fps=70

g = Vector(angle=0,speed=0.7)

I=0
def destroy():
    global I
    I+=1
    if (I>=2): simulation.destroy()
    print(I)
#simulation.add_click(destroy)
simulation.add_click(simulation.destroy)

while (simulation.flag and 1):
    #ball.x, ball.y = simulation.mouse_coo()

    #print(ball.x, ball.y)
    #ball.draw()
    #ball.delay()
    #print(ball.real_fps)
    simulation.update()
    if (ball.y>simulation.AREA_Y and 0):
        sleep(1)
        break
    #print(ball.x, ball.y)
    sleep(0.01)

#print(len(simulation.object))
simulation.destroy()
