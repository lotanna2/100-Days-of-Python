## from turtle import Screen, Turtle

## tim = Turtle()

## for _ in range(4):
 ##   tim.forward(100)
  ##  tim.right(90)


import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():  # function to generate a random color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

 # directions = [0, 90, 180, 270]
tim.speed("fastest")
tim.circle(100)

def draw_spirograph(size_of_gap):  # function to draw a spirograph
  for _ in range(int(360/size_of_gap)):  # draw a spirograph with 36 circles
          tim.pencolor(random_color())
          current_heading = tim.heading()  # get the current heading of the turtle
          tim.setheading(current_heading + size_of_gap)  # turn the turtle by the specified gap
          tim.circle(100)

draw_spirograph(5)  # draw a spirograph with a gap of 5 degrees

screen = t.Screen()
screen.exitonclick()







## for sides in range(3, 11): ## draw shapes from triangle (3 sides) to decagon (10 sides)

   ## angle = 360 / sides

   ## t.color(random.choice(colors))

   ## for _ in range(sides): ## moves the turtle forward and turns it right by the calculated angle
    ##  t.forward(100)
     ## t.right(angle)
    

## t.done()


##def draw_shape(num_sides):   # function to draw a shape with a given number of sides
 ##  angle = 360 / num_sides
##   for _ in range(num_sides):
##     t.forward(100)
 ##    t.right(angle)

##for shape_side_n in range(3, 11):   # draw shapes from triangle (3 sides) to decagon (10 sides)
 ##   t.color(random.choice(colors))
  ##  draw_shape(shape_side_n)
    


##t.done()



##    ##t.forward(10)  # draw the dash
    ##t.pendown()

    ##t.penup()
    ##t.forward(10)  # move without drawing


##t.done()

##screen = Screen()
##screen.exitonclick()

## timmy_the_turtle = Turtle1()
## timmy_the_turtle.shape("turtle")
## timmy_the_turtle.color("red")

