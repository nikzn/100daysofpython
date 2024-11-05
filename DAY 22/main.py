import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

is_game_on=True
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("MY PONG GAME")
screen.tracer(0)



r_paddle=Paddle((380,0))
l_paddle=Paddle((-380,0))

ball=Ball()
score = Scoreboard()






screen.listen()
screen.onkey(key="Up",fun=r_paddle.move_forward)
screen.onkey(key="Down",fun=r_paddle.move_downward)
screen.onkey(key="w",fun=l_paddle.move_forward)
screen.onkey(key="s",fun=l_paddle.move_downward)



while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    score.update_scoreboard()
    if ball.xcor()>380:
        ball.reset()
        score.update_lpaddle()

    if ball.xcor() < -380:
        ball.reset()
        score.update_rpaddle()

    if ball.ycor() > 260 or ball.ycor() < -260:
        ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor()>350 or ball.distance(l_paddle)<50 and ball.xcor()<-350:
        ball.bounce_x()

screen.exitonclick()


