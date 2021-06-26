from tkinter import *

#graphics_version = "1.0"

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

        self.click_fun = []

        self.flag = 1

    def update(self):
        try:
            if (not self.flag): return
            self.window.update()
        except TclError:
            self.destroy()

    def destroy(self):
        try:
            self.window.destroy()
        except TclError:
            pass
        self.flag = 0

    def mouse_coo(self):
        try:
            if (self.flag):
                return self.window.winfo_pointerx()-self.mouse_error.x,self.window.winfo_pointery()-self.mouse_error.y
        except TclError:
            self.destroy()
        return 0,0


    def click(self,event):
        # calibrating
        self.mouse_error.x = self.window.winfo_pointerx() - event.x
        self.mouse_error.y = self.window.winfo_pointery() - event.y
        # more function
        for f in self.click_fun:
            f()
        #off_window()
        #out_window.destroy()
        #print(event.x,event.y,self.window.winfo_pointerx(),self.window.winfo_pointery())

    def add_click(self,f):
        self.click_fun.append(f)

if __name__=="__main__":
    def test():
        print("!")

    def test2():
        print("!!")

    area = Graphics(300,300)
    area.add_click(test2)
    area.add_click(test)
    while (area.flag):
        area.update()


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
