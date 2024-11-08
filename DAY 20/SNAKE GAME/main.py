from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")

game_is_on=True
starting_position=[(0,0),(-20,0),(-40,0)]
segments=[]


snake=Snake()
food=Food()
score=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280  :
        # game_is_on=False
        # score.gamfeover()
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            # game_is_on=False
            # score.gameover()
            score.reset()
            snake.reset()




screen.exitonclick()