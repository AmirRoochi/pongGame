from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.speed('fastest')
        self.setpos(position)
        self.shapesize(5, 1)
        self.color('white')

    def pad_pos(self):
        return self.pos()

    def move_up(self):
        if self.ycor() < 280:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -280:
            self.goto(self.xcor(), self.ycor() - 20)

















































    # def create_paddle(self, pos_list):
    #     seg = []
    #     for i in range(4):
    #         t = Turtle('square')
    #         t.setheading(90)
    #         t.speed("fastest")
    #         t.penup()
    #         t.shapesize(0.75)
    #         t.setpos(pos_list[i])
    #         t.color('white')
    #         seg.append(t)
    #
    #     return seg

    # def move_paddle(self):
    #     for seg_num in range(len(self.r_segments) - 1, 0, -1):
    #         new_x = self.r_segments[seg_num - 1].xcor()
    #         new_y = self.r_segments[seg_num - 1].ycor()
    #         self.r_segments[seg_num].goto(new_x, new_y)
    #     self.r_segments[0].forward(10)























