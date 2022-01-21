
from turtle import Screen
from paddle import Paddle
import time
from scoreboard import Scoreboard
from ball import Ball

s = Screen()
s.bgcolor("black")
s.setup(800, 600)
s.title('Pong Game')
s.tracer(0)
r_pad = Paddle((355, 0))
l_pad = Paddle((-360, 0))
bll = Ball()
center_liner = Scoreboard()
center_liner.liner()
border_liner = Scoreboard()
border_liner.liner_2()
r_score = Scoreboard()
l_score = Scoreboard()
r_score.timer((30, 270))
l_score.timer((-43, 270))
s.onkeypress(fun=r_pad.move_up, key="Up")
s.onkeypress(fun=r_pad.move_down, key="Down")
s.onkeypress(fun=l_pad.move_up, key="w")
s.onkeypress(fun=l_pad.move_down, key="s")
s.listen()

game_on = True
stat = True
while game_on:
    counter = 0
    s.update()
    bll.move(stat)
    if bll.xcor() > 350 and bll.distance(r_pad) < 50:
        bll.bounce()
        stat = False
    elif bll.xcor() < -360 and bll.distance(l_pad) < 50:
        bll.bounce()
        stat = True
    if bll.xcor() > 400:
        l_score.add_score('left')
        bll.center_ball()
        time.sleep(1)
    elif bll.xcor() < -400:
        r_score.add_score('right')
        bll.center_ball()
        time.sleep(1)
    if r_score.get_score() == 15 or l_score.get_score() == 15:
        game_on = False






s.exitonclick()
