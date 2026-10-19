from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards(): # the screen.onkey() method is used to listen for key presses and call a function when a specific key is pressed
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_counter_clockwise():
    tim.left(10) # the turtle will turn left by 10 degrees when the a key is pressed

def turn_clockwise():
    tim.right(10) # the turtle will turn right by 10 degrees when the d key is pressed

def clear_screen():
    tim.clear()
    tim.penup() # the pen is lifted up so that it doesn't draw when moving to the starting position
    tim.home() # the turtle is moved to the starting position (0, 0)
    tim.pendown() # the pen is put down so that it can draw again





screen.listen()
screen.onkey(key="space", fun = move_forwards) # when the space key is pressed, the move_forwards function will be called
screen.onkey(key="s", fun = move_backwards) # when the s key is pressed, the move_backwards function will be called
screen.onkey(key="w", fun = move_forwards) # when the w key is pressed, the move_forwards function will be called
screen.onkey(key="a", fun = turn_counter_clockwise) # when the a key is pressed, the turn_counter_clockwise function will be called
screen.onkey(key="d", fun = turn_clockwise) # when the d key is pressed, the turn_clockwise function will be called
screen.onkey(key="c", fun = clear_screen) # when the c key is pressed, the clear_screen function will be called
screen.exitonclick() # the screen will close when the user clicks on it