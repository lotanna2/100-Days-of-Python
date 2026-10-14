import random

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5

def choose_difficulty():
    level = input("Choose difficulty level (easy/hard): ").lower()
    if level == "easy":
        return EASY_LEVEL_TURN
    elif level == "hard":
        return HARD_LEVEL_TURN
    else:

        print("Invalid choice. Defaulting to easy.")
        return EASY_LEVEL_TURN



def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    
    turns = choose_difficulty()
    print(f"You have {turns} attempts to guess the number.")
    number_to_guess = random.randint(1, 100) #  number to guess is the randomly generated

    while turns > 0:  # starts the function 
        guess = int(input("Make a guess: "))
        if guess < number_to_guess:
            print("Too Low")
        elif guess > number_to_guess:
            print("Too High")
        elif abs(guess - number_to_guess) <= 5: # checks if the guess is within 5 numbers absolute value (above or below) of the correct answer
            print("You're very close!")
        else:
            print(f"You got it! The answer was {number_to_guess}")
            return # Exit the function if all guessed correctly
        turns -= 1 # Decrease the number of turns left 
        if turns > 0:
                print(f"You have {turns} attempts remaining to guess the number.")
        else: 
            print(f"You've run out of guesses. The number was {number_to_guess}.")
if __name__ == "__main__":
    play_game()