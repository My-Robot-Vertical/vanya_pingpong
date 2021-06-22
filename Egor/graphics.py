from tkinter import *

graphics_version = "1.0"

class coo:

    def __init__(self,x,y):
        self.x = x
        self.y = y

class Graphics:

    def __init__(self,AREA_X,AREA_Y):
        self.window = Tk()
        self.window.title('graphics_area')
        self.canvas = Canvas(self.window,width=AREA_X,height=AREA_Y,bg="white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.click)

        self.AREA_X = AREA_X
        self.AREA_Y = AREA_Y
        self.mouse_error = coo(0,0)

        self.flag = 1

    def update(self):
        if (not self.flag): return
        self.window.update()

    def destroy(self):
        if (self.flag): self.window.destroy()
        self.flag = 0

    def mouse_coo(self):
        if (not self.flag): return 0,0
        return self.window.winfo_pointerx()-self.mouse_error.x,self.window.winfo_pointery()-self.mouse_error.y

    def click(self,event):
        if (not self.flag): return
        # calibrating
        self.mouse_error.x = self.window.winfo_pointerx() - event.x
        self.mouse_error.y = self.window.winfo_pointery() - event.y
        #off_window()
        #out_window.destroy()
        #print(event.x,event.y,self.window.winfo_pointerx(),self.window.winfo_pointery())

'''
AREA_X = 300
AREA_Y = 300

out_window = Tk()
out_window.title('pingpong')
canvas = Canvas(out_window,width=AREA_X,height=AREA_Y,bg="white")

flag_window = 1

def off_window():
    global flag_window
    flag_window = 0

def test_window():
    return flag_window

def mouse_coo():
    return out_window.winfo_pointerx()-1,out_window.winfo_pointery()-82

def click(event):
    off_window()
    out_window.destroy()
    #print(event.x, event.y, mouse_coo())

canvas.bind("<Button-1>", click)
canvas.pack()
'''
