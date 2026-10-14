##importanother_module 
##print(another_module.another_variable)

##from turtle import Turtle, Screen

##timmy = Turtle() ## Created a turtle object named timmy from a class called Turtle.
##print(timmy) ## This will print the object representation of timmy.
##timmy.shape("turtle") ## This method will change the shape of the turtle to a turtle shape.
##timmy.color("red") ## This method will change the color of the turtle to red.
##timmy.forward(150) ## This method will move the turtle forward by 150 units.

##my_screen = Screen() ## Created a screen object named screen from a class called Screen.
##print(my_screen.canvheight)
##my_screen.exitonclick() ## This method will keep the screen open until we click on it. 


from prettytable import PrettyTable
table = PrettyTable() ## Created a PrettyTable object named table from a class called PrettyTable.
table.add_column("pokemon Name", ["pikachu", "squirtle", "charmander"]) ## This method will add a column to the table with the name "pokemon Name" and the values ["pikachu", "squirtle", "charmander"].
table.add_column("Type", ["Electric", "water", "fire"]) ## This method will add a column to the table with the name "Type" and the values ["Electric", "water", "fire"].

table.align = "l" ## changes the attribute of the table to align the text to the left.

print(table)