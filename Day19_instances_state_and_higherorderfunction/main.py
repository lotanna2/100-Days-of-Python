import random
from turtle import Turtle, Screen


is_race_on = True # a boolean variable is created to keep track of whether the race is on or not
screen = Screen()
screen.setup(width=500, height=400) # the screen size is set to 500 pixels wide and 400 pixels high
user_bet = screen.textinput(
    title="Make your bet", 
    prompt="Enter your bet: "
    ) # a text input dialog is displayed to the user to enter their bet
colors = ["red", "orange", "yellow", "green", "blue", "purple"] # a list of colors is created for the turtles
random_distance = random.randint(0, 10) # a random distance is generated between 0 and 10 for the turtles to move forward in each iteration of the race

all_turtles = [] # an empty list is created to store the turtle objects
starting_y = -100 # the starting y position for the turtles is set to -100

for turtle_colors in colors: # a for loop is used to create a turtle object for each color in the colors list
    new_turtle = Turtle(shape="turtle") # a new turtle object is created
    new_turtle.penup() # the pen is lifted up so that it doesn't draw when moving to the starting position
    new_turtle.color(turtle_colors) # the color of the turtle is set to the current color in the colors list
    new_turtle.goto(x=-230, y =starting_y) # the turtle is moved to the starting position (x=-230, y=starting_y)
    all_turtles.append(new_turtle) # the new turtle object is added to the all_turtles list

    starting_y = starting_y + 30 # the starting y position is incremented by 30 for the next turtle

if user_bet: # if the user has entered a bet, the race will start
    is_race_on = True # the boolean variable is set to True to indicate that the race is on

while is_race_on: # a while loop is used to keep the race going until a turtle crosses the finish line
    for turtle in all_turtles: # a for loop is used to move each turtle forward by a random distance
        if turtle.xcor() > 230: # if the turtle's x position is greater than 230, it has crossed the finish line
            is_race_on = False # the race is over, so the boolean variable is set to False
            winning_color = turtle.pencolor() # the color of the winning turtle is stored in a variable
        
            if winning_color == user_bet: # if the winning color is the same as the user's bet, a message is printed to the console
                print(f"You've won! The {winning_color} turtle is the winner!")
            else: # if the winning color is not the same as the user's bet, a message is printed to the console
                print(f"You've lost! The {winning_color} turtle is the winner!")

        else: # if the turtle has not crossed the finish line, it will move forward by a random distance
            random_distance = random.randint(0, 10) # a random distance is generated between 0 and 10
            turtle.forward(random_distance) # the turtle moves forward by the random distance

        
screen.exitonclick()
# def move_forwards(): # the screen.onkey() method is used to listen for key presses and call a function when a specific key is pressed
#     tim.forward(10)

# def move_backwards():
#     tim.backward(10)

# def turn_counter_clockwise():
#    tim.left(10) # the turtle will turn left by 10 degrees when the a key is pressed

# def turn_clockwise():
#     tim.right(10) # the turtle will turn right by 10 degrees when the d key is pressed

# def clear_screen():
#     tim.clear()
#     tim.penup() # the pen is lifted up so that it doesn't draw when moving to the starting position
#     tim.home() # the turtle is moved to the starting position (0, 0)
#     tim.pendown() # the pen is put down so that it can draw again





 # screen.listen()
 # screen.onkey(key="space", fun = move_forwards) # when the space key is pressed, the move_forwards function will be called
 # screen.onkey(key="s", fun = move_backwards) # when the s key is pressed, the move_backwards function will be called
 # screen.onkey(key="w", fun = move_forwards) # when the w key is pressed, the move_forwards function will be called
 #screen.onkey(key="a", fun = turn_counter_clockwise) # when the a key is pressed, the turn_counter_clockwise function will be called
 #screen.onkey(key="d", fun = turn_clockwise) # when the d key is pressed, the turn_clockwise function will be called
 #screen.onkey(key="c", fun = clear_screen) # when the c key is pressed, the clear_screen function will be called
 #screen.exitonclick() # the screen will close when the user clicks on it