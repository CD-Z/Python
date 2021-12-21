from tkinter import *
import random
import time

# tk.resizable(0, 0)
# tk.wm_attributes("-topmost", 1)


def create_ball(event):
    print(event)
    master.balls.add(Ball(master.tk.canvas, "#e67921", event.x, event.y))


class Ball:
    def __init__(self, canvas, color, x, y):
        self.canvas = canvas
        self.id = canvas.create_oval(x, y, x + 15, y + 15, fill=color)

    def get_x(self):
        return self.canvas.coords(self.id)[1]

    def get_y(self):
        return self.canvas.coords(self.id)[3]

    def draw(self):
        if self.get_y() > 10:
            self.canvas.move(self.id, 0, -1)
        else:
            self.canvas.move(self.id, 1, 0)
        #self.canvas.after(10, self.draw)


class Window:
    def __init__(self):
        self.tk = Tk()
        self.tk.title = "Game"
        self.tk.canvas = Canvas(self.tk, width=500, height=400, bd=0, highlightthickness=0, borderwidth=2, relief="solid")
        self.balls = set()

        self.tk.canvas.pack(expand=True, fill=BOTH)
        self.tk.grid_columnconfigure(0, weight=1)
        self.tk.grid_rowconfigure(0, weight=1)
        self.tk.bind("<Button-1>", create_ball)
        self.ball = Ball(self.tk.canvas, "red", 10, 100)
        print("KFDLKJÖF")

    def update(self):
        self.ball.draw()
        for ball in self.balls:
            ball.draw()
        self.tk.canvas.after(10, self.update)


master = Window()
master.update()
master.tk.mainloop()
