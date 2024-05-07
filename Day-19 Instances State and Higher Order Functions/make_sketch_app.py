from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
    
def move_backwards():
    tim.backward(10)
    
def move_ccw():
    tim.right(10)

def move_cw():
    tim.left(10)

def clear():
    tim.reset()   

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_ccw)
screen.onkey(key="d", fun=move_cw)
screen.onkey(key="c", fun=clear)

screen.exitonclick()