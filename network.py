
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

    def circle(self, x, y):
        self.canvas.create_oval(x-size, y-size, x+size, y+size)
    
    def cross(self, x, y):
        self.canvas.create_line(x-size, y-size, x+size, y+size)
        self.canvas.create_line(x-size, y+size, x+size, y-size)


class Perceptron:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def classify(self, x, y):
        return y > self.a * x + self.b

    def draw(self, window):
        s_x = 0
        s_y = 0
        if 0 <= self.b <= 100:
            s_x = 0
            s_y = self.b
        else:
            exit(0)

        e_x = 0
        e_y = 0
        x_intercept = -self.b/self.a
        if 0 < x_intercept < 100:
            e_x = x_intercept
            e_y = 0
        else:
            exit(0)

        window.line(s_x, s_y, e_x, e_y)

class Result:

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def draw(self, window):
        if self.value:
            window.circle(self.x, self.y)
        else:
            window.cross(self.x, self.y)

    def text(self):
        if self.value:
            return "o"
        else:
            return "x"


window = Window()

p1 = Perceptron(-0.5, 40)

points_x = [random.randint(0, 100) for i in range(100)]
points_y = [random.randint(0, 100) for i in range(100)]
results = [None] * 100

for i in range(100):
    result_type = p1.classify(points_x[i], points_y[i])
    results[i] = Result(points_x[i], points_y[i], result_type)

print("Results: ")
for i in range(10):
    print("  ", list(map(lambda x:x.text(),results[i:i+10])))

for item in results:
    item.draw(window)

p1.draw(window)
window.mainloop()