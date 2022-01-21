from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.color('white')
        self.penup()

    def liner(self):
        self.setpos(0, 300)
        self.pendown()
        self.pencolor('white')
        self.setheading(270)
        while self.ycor() != -300:
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
        self.penup()
        self.goto(0, 300)
        self.hideturtle()

    def liner_2(self):
        self.pencolor('yellow')
        self.setpos(-390, -290)
        self.pendown()
        self.setheading(90)
        self.forward(588)
        self.setheading(0)
        self.forward(775)
        self.setheading(270)
        self.forward(588)
        self.setheading(180)
        self.forward(775)
        self.hideturtle()

    def timer(self, pos):
        self.setpos(pos)
        self.write(self.counter, False, font=("style", 18, "normal"))
        self.hideturtle()

    def add_score(self, l_or_r):
        self.counter += 1
        self.clear()
        if l_or_r == 'right':
            self.timer((30, 270))
        elif l_or_r == 'left':
            self.timer((-43, 270))

    def get_score(self):
        return self.counter







