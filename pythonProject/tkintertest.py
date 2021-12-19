from tkinter import *


canvas_width = 500
canvas_height = 150
write_pos = 150


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


message = Label(master, text="Press and Drag the mouse to draw")
Button(master, text="Hello").pack(side=BOTTOM)
message.pack(side=BOTTOM)

master.mainloop()
