from random import random

import redis
from tkinter import *

# r = redis.StrictRedis(host='10.115.2.20', port=6379, db=0, charset='utf-8', decode_responses=True)
r = redis.StrictRedis(host='192.168.0.145', port=6379, db=0, charset='utf-8', decode_responses=True,
                      password="Pat-02los20")

master = Tk()


def print_leaderboard():
    players = r.zrevrange("player", 0, 4, withscores=True)
    i = 1
    for player in players:
        Label(master, text=f"Position {i}: Name: {player[0]} Score: {player[1]}").grid(row=i)
        i = i + 1


def check_position(num):
    fith = r.zrevrange("player", 4, 4, withscores=True)
    n = (name.get())
    if fith == [] or fith[0][1] < num:
        r.zadd("player", {n: num})


def participate():
    num = round(((random() + random() + random() - random()) * random() * 2), 2)
    check_position(num)
    print_leaderboard()
    print(name)
    print(r.zrevrange("player", 0, 0, withscores=True))


master.title("Painting using Ovals")
name = Entry(master)
name.grid(row=6)

print(name)

b1 = Button(master, text="Participate", command=participate).grid(row=7)

master.update()
master.mainloop()
