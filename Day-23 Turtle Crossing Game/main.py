import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
level = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.add_car()
    car_manager.move()
    
    # detect collision with car
    for car in car_manager.car_list:
        if car.distance(player) < 25:
            game_is_on = False
            level.game_over()
            
    # detect of successful crossing
    if player.is_at_finish_line():
        player.reset_position()
        car_manager.level_up()
        level.level_up()


screen.exitonclick()