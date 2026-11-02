import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move_up, "Up")

car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    if random.randint(1, 6) == 1:  # Randomly create a car with a 1 in 6 chance each loop iteration
        car_manager.create_car()
    car_manager.move_cars()
    time.sleep(0.1)
    screen.update()



    # Check for collision with any car in the list of all cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20: # goes through all the cars in the list and checks if the player is too close to any of them, indicating a collision
            game_is_on = False
            scoreboard.game_over()
            break
    # Check if the player reached the top and update the level accordingly
    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.reset_position()
        car_manager.level_up()

screen.exitonclick()