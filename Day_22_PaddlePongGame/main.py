from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("paddle pong game")
screen.setup(width=800, height=600)
screen.tracer(0) # controls the animation speed, used to turn it off here


r_paddle = Paddle(position=(350, 0))
l_paddle = Paddle(position=(-350, 0))
ball = Ball() # if i needed to add a paddle, i can just wirte another t_paddle = Paddle(position=(-350, 0)) without having to change the code in the main loop
scoreboard = Scoreboard() # create an instance of the scoreboard class

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True 

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update() # updates the screen to show the paddle and everything else that has happened
    ball.move()  

    if ball.ycor() > 300 or ball.ycor() < -280:
        # need to bounce
        ball.bounce_y()

    #Detect collision with paddles after it passes a certain point on the screen
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320: # this checks if the ball has passed a distance of 340px and is at a distance of 50px to the paddle 
        ball.bounce_x()

    #Detect when right paddle misses
    if ball.xcor() > 380: 
        ball.reset_position()

    #Detect when right paddle misses
    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()