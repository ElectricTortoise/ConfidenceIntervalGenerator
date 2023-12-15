import scipy.stats as ss
import tkinter as tk
import random


def random_color():
    return "#{:06x}".format(random.randint(0,16777215))

def draw_rectangles(window, x1, y1,size):
    x2 = x1+size
    y2 = y1+size
    color = random_color()
    window.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
                        

master = tk.Tk()
master.title("Confidence Interval Generator")

width = 960
height = 540

window = tk.Canvas(master, width=width, height=height)
size = 2
for i in range(0,width,size):
    for j in range(0,height,size):
        draw_rectangles(window, i, j, size)

window.pack()

master.mainloop()