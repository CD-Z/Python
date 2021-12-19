from tkinter import *


canvas_width = 500
canvas_height = 150
x =10


def paint(event):
    print(event)
    python_green = "#476042"
    x1, y1 = (event.x - 10), (event.y - 10)
    x2, y2 = (event.x + 10), (event.y + 10)
    w.create_oval(x1, y1, x2, y2, fill=python_green)

master = Tk()
master.title("Painting using Ovals")
w = Canvas(master,
               width=canvas_width,
               height=canvas_height)
w.pack(expand=YES, fill=BOTH)
master.bind("<Button-1>", paint)
Button(master, text="Hello").pack(side=BOTTOM)
message = Label(master, text="Press and Drag the mouse to draw")
message.pack(side=BOTTOM)


w.create_oval(x, 10, x + 10, 20, fill="#348029")

x = x +1




master.update()
master.mainloop()

