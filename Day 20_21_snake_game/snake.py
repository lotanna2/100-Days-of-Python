from turtle import Turtle

starting_points = [(0, 0), (-20, 0), (-40, 0)] # a tuple of starting points for the snake segments
move_distance = 20  # a constant for the distance the snake moves each time it moves

class Snake:
    def __init__(self): # def tells python you're defining a function (within a class, it is called a method) 
         #  and __init__ is a special method that runs automatically when you create a new snake object (it sets up the snake)
          #  self is a special variable that refers to the snake object you're creating
        self.segments = []
        self.create_snake() # create the snake
        self.head = self.segments[0] # set the head of the snake to the first segment

    def create_snake(self):
        # Create a turtle segment at each starting position.
        for position in starting_points:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)  # Add the new segment to the snake's list.

    def move(self):
        # Move each segment by targeting the segment number in front of it.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # Move the head forward by the distance specified in move_distance cited above
        self.head.forward(move_distance) # targeting the head of the snake (the first segment)

    def up(self): # method for moving the snake up
        self.head.setheading(90)
    

    def down(self): # method for moving the snake down
        self.head.setheading(270)
       

    def left(self): # method for moving the snake left
        self.head.setheading(180)
        

    def right(self): # method for moving the snake right
        self.head.setheading(0)
       