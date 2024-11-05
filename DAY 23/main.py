import time
from turtle import Screen


from player import Player
from cars import Cars
from scoreboard import Scoreboard

isGameOn=True
screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)


player=Player()
cars=Cars()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(key="Up",fun=player.move_forward)
screen.onkey(key="Down",fun=player.move_backward)

while isGameOn:
    time.sleep(0.1)
    screen.update()
    cars.create_random_car()
    cars.move_cars()
    for car in cars.all_cars:
        if car.distance(player)<20:
            isGameOn=False
            scoreboard.game_over()

    if player.is_at_finishing_line():
        player.go_to_starting_line()
        cars.level_up()
        scoreboard.update_scoreboard()




screen.exitonclick()
