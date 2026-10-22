from turtle import Screen , Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # turn off the screen updates for a smoother animation

snake = Snake()

screen.listen() # listen for keyboard events
screen.onkey(snake.up, "Up") # when the user presses the up arrow, move the snake
screen.onkey(snake.down, "Down") # when the user presses the down key
screen.onkey(snake.left, "Left") # when the user presses the left key
screen.onkey(snake.right, "Right") # when the user presses the right key

game_is_on = True

while game_is_on:
    screen.update() # update the screen to show the new positions of the segments
    time.sleep(0.1) # wait for 100 milliseconds
    snake.move() # move the snake


screen.exitonclick() # keep the window open until the user clicks on it 