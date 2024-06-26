from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
start = -250
stop = 250
step = 20
num_steps = (stop-start) // step



class CarManager():
    def __init__(self):
        self.car_list = []
        self.add_car()
        self.car_speed = STARTING_MOVE_DISTANCE
        
        
    def add_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car  = Turtle(shape="square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y_pos = start + random.randint(0, num_steps)*step
            # starting position
            new_car.goto(300, random_y_pos)
            self.car_list.append(new_car)
        
        
    def move(self):
        for car in self.car_list:
            new_x = car.xcor() - self.car_speed
            car.goto(new_x, car.ycor())
            
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        
    
