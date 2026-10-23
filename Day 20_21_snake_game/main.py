from turtle import Screen 
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # turn off the screen updates for a smoother animation

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food

    if snake.head.distance(food)  < 15:
        food.refresh() # refresh the food location everytime it;s eaten
        snake.extend_snake()
        scoreboard.increment_score()

    # Detect collision with the border
    if snake.head.xcor() > 290 or snake.head.xcor()  < -290 or snake.head.ycor() > 290 or snake.head.ycor() < - 290: 
        game_is_on = False
        scoreboard.game_over()
    
    # Detect collision with the tail
    for segment in snake.segments[1:]:  # because the head is the first segment in the snake, we don't want to check it against itself
        # python slice notation: snake.segments[1:] means "from the second element (index 1) to the end of the list". there's also [: :-1] to increment by 1 and start from the end (-2 would increment by 2 and start from the end)
        if snake.head.distance(segment) < 15:
            game_is_on = False
            scoreboard.game_over()
 
screen.exitonclick() # keep the window open until the user clicks on it 