
from tkinter import Tk, Canvas, Frame, BOTH
import random

size = 3

class Window(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("I'm Learning")
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self)
        self.canvas.pack(fill=BOTH, expand=1)
    
    def line(self, start_x, start_y, end_x, end_y): 
        self.canvas.create_line(start_x, start_y, end_x, end_y)

    def circle(self, x, y, colour):
        self.canvas.create_oval(x-size, y-size, x+size, y+size, outline=colour)
    
    def cross(self, x, y, colour):
        self.canvas.create_line(x-size, y-size, x+size, y+size, fill=colour)
        self.canvas.create_line(x-size, y+size, x+size, y-size, fill=colour)


class Perceptron:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def classify(self, p):
        return p.y() > self.a * p.x() + self.b

    def draw(self, window):
        s_x = 0
        s_y = 0
        if 0 <= self.b <= 300:
            s_x = 0
            s_y = self.b
        else:
            exit(0)

        e_x = 0
        e_y = 0
        x_intercept = -self.b/self.a
        if 0 < x_intercept < 300:
            e_x = x_intercept
            e_y = 0
        else:
            exit(0)

        window.line(s_x, s_y, e_x, e_y)


class Point:

    def __init__(self, x, y, ty):
        self._x = x
        self._y = y
        self.ty = ty

    def draw(self, window, colour):
        if self.ty:
            window.circle(self._x, self._y, colour)
        else:
            window.cross(self._x, self._y, colour)

    def text(self):
        if self.ty:
            return "o"
        else:
            return "x"

    def x(self):
        return self._x

    def y(self):
        return self._y

class Result:

    def __init__(self, point, value):
        self.point = point
        if value:
            self.colour = "#f50"
        else:
            self.colour = "#05f"

    def draw(self, window):
        self.point.draw(window, self.colour)

    def text(self):
        return self.point.text() + "-" + self.colour


window = Window()

p1 = Perceptron(-0.5, 140)

points_x = [random.randint(0, 300) for i in range(100)]
points_y = [random.randint(0, 300) for i in range(100)]
types = list(map(lambda x:bool(x),[random.randint(0, 1) for i in range(100)]))

print("Types")
print(types)

points = []

for i in range(100):
    points.append(Point(points_x[i], points_y[i], types[i]))

results = []

for p in points:
    results.append(Result(p, p1.classify(p)))

print("Results: ")
for i in range(10):
    print("  ", list(map(lambda x:x.text(),results[i:i+10])))

for item in results:
    item.draw(window)

p1.draw(window)
window.mainloop()