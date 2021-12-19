from tkinter import *
import random
import time

tk = Tk()
tk.title = "Game"
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)

        self.canvas.move(self.id, 245, 100)

    def get_x(self):
        return self.canvas.coords(self.id)[1]

    def get_y(self):
        return self.canvas.coords(self.id)[3]

    def draw(self):
        if (self.get_y()>10):
            self.canvas.move(self.id, 0, -1)
        else:
            self.canvas.move(self.id, 1, 0)
        self.canvas.after(10, self.draw)  # (time_delay, method_to_execute)


ball = Ball(canvas, "red")
ball.draw()  # Changed per Bryan Oakley's comment
tk.mainloop()