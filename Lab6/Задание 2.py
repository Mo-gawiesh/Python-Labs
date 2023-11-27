from tkinter import *
import time
import _thread

c = Canvas(width=500, height=500, bg='cyan')
c.pack()

circle = c.create_oval(50, 50, 100, 100, fil='red')
i = 5
j = 0


def move_circle():
    global i, j
    c.move(circle, i, j)
    print(c.coords(circle)[0], c.coords(circle)[1])

    if c.coords(circle)[0] == 400 and c.coords(circle)[1] == 50:
        i = 0
        j = 5
    elif c.coords(circle)[0] == 400 and c.coords(circle)[1] == 400:
        i = -5
        j = 0
    elif c.coords(circle)[0] == 50 and c.coords(circle)[1] == 400:
        i = 0
        j = -5
    elif c.coords(circle)[0] == 50 and c.coords(circle)[1] == 50:
        i = 5
        j = 0
    c.after(50, move_circle)


move_circle()
mainloop()
