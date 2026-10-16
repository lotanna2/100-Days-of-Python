# import colorgram

# colors = colorgram.extract("image.jpg", 30) # Extracts 30 dominant colors from the image "image.jpg"

# rgb_colors = [] # List to store the RGB values of the extracted colors

# for color in colors: 

#   r = color.rgb.r
#   g = color.rgb.g
#  b = color.rgb.b

   # color_tuple = (r, g, b) # Create a tuple of RGB values
   # rgb_colors.append(color_tuple) # Append the tuple to the list of RGB colors

# print(rgb_colors) # Print the list of RGB colors



import turtle as turtle_module
import random

tim = turtle_module.Turtle() # Create a turtle object for drawing
screen = turtle_module.Screen()
screen.colormode(255) # Set the color mode to 255 for RGB values

tim = turtle_module.Turtle() # Create a turtle object named "tim" that can draw on the screen
tim.speed("fastest") # Set the speed of the turtle to the fastest setting
tim.hideturtle() # Hide the turtle cursor so it doesn't appear on the screen
tim.pensize(3) # Set the pen size to 20 pixels for drawing the dots
tim.penup() # Lift the pen so it doesn't draw lines when moving

tim.goto(-225, -225) # Move the turtle to the starting position (0, 0)


color_tuple_list = [
    [
        (233, 235, 240), (215, 166, 17), (230, 239, 234),
        (205, 153, 99), (225, 205, 103), (161, 55, 101),
        (113, 187, 213), (154, 31, 58), (8, 109, 166),
        (42, 13, 24), (160, 29, 25), (12, 23, 52),
        (34, 122, 62), (59, 23, 18), (9, 32, 26),
        (186, 156, 173), (63, 166, 88), (171, 57, 42),
        (156, 208, 215), (94, 183, 167), (205, 99, 95),
        (240, 200, 3), (213, 174, 198), (28, 37, 105),
        (187, 99, 110), (163, 209, 197), (220, 177, 173),
        (14, 105, 56)
    ]
]

colors = color_tuple_list[0] # Get the first list of color tuples from the nested list


dot_color = random.choice(colors) # Choose a random color from the list of colors for the dots
tim.dot(20, dot_color) # Draw a dot with a diameter of 20 pixels and the chosen color   

""" draw 100 dots in a grid pattern """

for row in range(10): # Loop through 10 rows
    for col in range(10): # Loop through 10 columns
        dot_color = random.choice(colors)
        tim.dot(20, dot_color)
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen.exitonclick() # Wait for a mouse click on the screen before closing the window