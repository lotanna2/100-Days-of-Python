import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif" # the path to reach my image
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x, y): # this function will print the coordinates of the mouse click
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor) # this will listen and call the function whenever the screen is clicked


data = pd.read_csv("50_states.csv") # read the CSV file containing the states and their coordinates

all_states = data.state.to_list() # create a list of all the states from the CSV file
guessed_states = [] # create an empty list to store the states guessed by the user


while len(guessed_states) < 50: # keep asking for states until all 50 are guessed
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title() # Ask the player for a state name and capitalize each word in the answer with 'Title()'.


    if answer_state == "Exit": # if the user types "Exit", break out of the loop
        missing_states = [state for state in all_states if state not in guessed_states] # add the states that have not been guessed yet to the missing_states list
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv") # save the missing states to a new CSV file and calls it "states_to_learn.csv"
        break
       # previous code
       # missing_states = []
       # for state in all_states: 
       #     if state not in guessed_states:
       #         missing_states.append(state)
      

    if len(guessed_states) == 50: # if all 50 states are guessed, congratulate the player
        screen.textinput(title="Congratulations!", prompt="You've guessed all 50 states!")
        break # exit the loop after congratulating the player

    if answer_state in all_states and answer_state not in guessed_states: 
        guessed_states.append(answer_state)
        t = turtle.Turtle() # create a new turtle to write the state name
        t.hideturtle()
        t.penup()
        display_data = data[data.state == answer_state] # filter the data to get the row corresponding to the guessed state
        t.goto((display_data.x.item()), (display_data.y.item())) # item grabs the first element of the pandas series
        t.write(answer_state)
        # t.write(display_data.state.item()) it gets the state data, the state row and then the state name from the CSV file 
        # it could also be t.write(answer_state) since answer_state contains the name of the guessed state


turtle.mainloop() # this will keep the window open and listen for mouse clicks

