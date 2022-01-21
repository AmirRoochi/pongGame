from turtle import Turtle
import random

ANGELS = [20, 30, 40, 50, 60, 70]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(0.75)
        self.penup()
        self.setpos(0, 0)
        self.speed(1)
        self.left(45)

    def move(self, status):
        self.forward(1)
        if 298 < self.ycor() < 300 and status:
            self.right(random.randint(40, 45))
        elif 298 < self.ycor() < 300 and not status:
            self.left(random.randint(45, 50))
        elif -295 > self.ycor() > -300 and not status:
            self.right(random.randint(45, 50))
        elif -295 > self.ycor() > -300 and status:
            self.left(random.randint(40, 45))

    def bounce(self):
        list_b = [160, 170, 180]
        self.right(random.randint(160, 180))
        spd = self.speed()
        spd += 0.1
        self.speed(spd)

    def center_ball(self):
        self.goto(0, 0)









