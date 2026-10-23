from turtle import Turtle, position

starting_points = [(0, 0), (-20, 0), (-40, 0)] # a tuple of starting points for the snake segments
move_distance = 20  # a constant for the distance the snake moves each time it moves
up = 90  # constants for the direction the snake is facing
down = 270
left = 180
right = 0


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
            self.add_segment(position)
         
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)  # Add the new segment to the snake's list.
        

    def extend_snake(self): # Add a new segment to the snake's list at the last position (calling the add_segment function we use at the begining).
        self.add_segment(self.segments[-1].position()) # we are getting a hold of the last segment's position . so we're essentially adding a new segment to the snake at the same position as the last segment . position() is a method that returns the position of the turtle object

    def move(self):
        # Move each segment by targeting the segment number in front of it.
        for seg_num in range(len(self.segments) - 1, 0, -1): # range(start, end, step) is a function that returns a list of numbers from start to end, incremented by step
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # Move the head forward by the distance specified in move_distance cited above
        self.head.forward(move_distance) # targeting the head of the snake (the first segment)

    def up(self): # method for moving the snake up
        if self.head.heading() != down:  #  if the current heading is not pointed down then it can move up
            self.head.setheading(up)
    

    def down(self): # method for moving the snake down
        if self.head.heading() != up:  #  if the current heading is not pointed up then it can move down
            self.head.setheading(down)
       

    def left(self): # method for moving the snake left
        if self.head.heading() != right:  #  if the current heading is not pointed right then it can move left
            self.head.setheading(left)
        

    def right(self): # method for moving the snake right
        if self.head.heading() != left:  #  if the current heading is not pointed left then it can move right
            self.head.setheading(right)
       