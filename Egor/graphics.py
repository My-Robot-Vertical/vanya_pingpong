from tkinter import *

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
