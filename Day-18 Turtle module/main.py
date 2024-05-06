# Turtle Documentation: https://docs.python.org/3/library/turtle.html
# Colors: https://trinket.io/docs/colors
# Turtle Colors: https://cs111.wellesley.edu/reference/colors

import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
#tim.shape("turtle")
#tim.color("spring green")

colors = ["blue", "chartreuse", "dark olive green", "gold", "sienna", "maroon", "deep pink", "medium violet red", "blue violet"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# draw a square
tim.reset()
for _ in range(4):
    tim.right(90)
    tim.forward(100)

# draw dashed line
tim.reset()
for _ in range (20):
    tim.forward(10)
    tim.pu()
    tim.forward(10)
    tim.pd()

# draw different shape with diff colors
tim.reset()
num_sides = 3
while num_sides <=10:
    #print(num_sides)
    angle = 0
    tim.color(random_color())
    while int(angle) != 360:
        tim.forward(100)
        angle += 360/num_sides
        #print(angle)
        tim.right(360/num_sides)
    num_sides += 1

# draw a random walk
tim.reset()
angle = [0, 90, 180, 270]
tim.pensize(10)
tim.speed(0)
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(angle))
    
# draw circle

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        
tim.reset()
tim.speed(0)
draw_spirograph(5)

        
    


screen = t.Screen()
screen.exitonclick()
