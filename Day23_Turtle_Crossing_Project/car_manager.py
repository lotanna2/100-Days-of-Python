from turtle import Turtle
import random 

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = [] # Initialize an empty list to keep track of all the cars created
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS)) # Set a random color for the car from the COLORS list
        new_car.goto(300, random.randint(-250, 250)) # go to the right edge of the screen at a random y-coordinate from -250 to 250
        self.all_cars.append(new_car) # Add the newly created car to the list of all cars

    def move_cars(self):
        for car in self.all_cars:
            car.setx(car.xcor() - self.car_speed) # Move the car to the left by the current car speed


    def level_up(self):
        self.car_speed = self.car_speed + MOVE_INCREMENT