from turtle import color
import scipy.stats as ss
import tkinter as tk
import random


def random_color():
    colorVal = random.randint(0,16777215)
    return "#{:06x}".format(colorVal), colorVal

def draw_rectangles(window, x1, y1,size):
    x2 = x1+size
    y2 = y1+size
    color = random_color()
    window.create_rectangle(x1, y1, x2, y2, fill=color[0], outline="")
    return color[1]
  

#Rectangle class
#(x1,y1) are the top left coordinates, (x2,y2) are the bottom right coordinates, fill is the color of the rectangle, hexVal is the hexcadecimal value associated with the color
class Rectangle():              
    def __init__(self, x1, y1, x2, y2, fill, hexVal): 
        window = tk.Canvas(master, width=width, height=height)
        window.create_rectangle(x1, y1, x2, y2, fill=color[0], outline="")
        window.pack()



master = tk.Tk()
master.title("Confidence Interval Generator")

width = 960
height = 540

window = tk.Canvas(master, width=width, height=height)
window.pack()

size = 10
colorSum = 0
for i in range(0,width,size):
    for j in range(0,height,size):
        colorVal = draw_rectangles(window, i, j, size)
        colorSum = colorSum + colorVal

numRectangles = width*height/(size**2)
print(numRectangles)
colorAvg = int(colorSum/numRectangles)
print("Population mean, μ =", colorAvg)


master.mainloop()