from tkinter import *
from tkinter import font
import keyboard, time, random





tails = []
direction = "left"


tk = Tk()
canvas = Canvas()
canvas.pack(expand=YES, fill=BOTH)
size = 15
offset = 3
width, height = 450 + 2 * offset, 450 + 2 * offset
rows, cols = (width - 2 * offset) / size, (height - 2 * offset) / size
tk.geometry("{0}x{1}".format(width, height))
tk.title("Snake")

class Apple:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        canvas.create_rectangle(self.x + 3, self.y + 3, self.x + size - 3, self.y + size - 3, fill="red")


class Head:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        canvas.create_rectangle(self.x, self.y, self.x + size, self.y + size, fill="yellow")

class Tail:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        canvas.create_rectangle(self.x, self.y, self.x + size, self.y + size, fill="green")


apple = Apple(int(cols / 2) * size + offset, int(rows / 2) * size - size * 3 + offset)
head = Head(int(cols / 2) * size + offset, int(rows / 2) * size + offset)


def count(list):
    c = 0
    for i in list:
        c += 1
    return c

def draw():
    for i in tails:
        i.draw()
    head.draw()
    apple.draw()
    tk.update()
    canvas.delete("all")



t = time.time()
while keyboard.is_pressed('q') == False:
    if (keyboard.is_pressed('up')):
        direction = "up"
    elif (keyboard.is_pressed('down')):
        direction = "down"
    elif (keyboard.is_pressed('left')):
        direction = "left"
    elif (keyboard.is_pressed('right')):
        direction = "right"

        
    if (time.time() - t >= 0.12):

        for i in reversed(range(count(tails))):
            tails[i].x = tails[i - 1].x
            tails[i].y = tails[i - 1].y
        try:
            tails[0].x = head.x
            tails[0].y = head.y
        except:
            pass

        if (direction == "up"):
            head.y -= size
        elif (direction == "down"):
            head.y += size
        elif (direction == "left"):
            head.x -= size
        elif (direction == "right"):
            head.x += size

        if (apple.x == head.x and apple.y == head.y ):
            apple = Apple(random.randint(0, cols) * size + offset, random.randint(0, rows) * size + offset)
            tails.append(Tail(head.x, head.y))
        t = time.time()
        draw()

