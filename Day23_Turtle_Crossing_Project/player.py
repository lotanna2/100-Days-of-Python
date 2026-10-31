from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.setheading(90)

    
    def move_up(self):
        if self.ycor() < FINISH_LINE_Y:
            self.sety(self.ycor() + MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)


    def is_at_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False
    


