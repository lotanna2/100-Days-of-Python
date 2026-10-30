from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10 # defined the amount the ball needs to move
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move #use the amount the ball needs to move when it moves
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_move *= -1 # reverses the move method by multiplying by -1

    def bounce_x(self): # reverses the move method by multiplying by -1 for x axis
        self.x_move *= -1
        self.move_speed *= 0.6 # increase the speed of the ball each time it bounces on the paddle

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()