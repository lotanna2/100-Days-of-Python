import random
from accounts_data import data

def format_account(account):
    """Format and returns a readable string of the account details. """
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description } from {country}"

def check_answer(guess, a_followers, b_followers):
    """Returns True if the player guessed correctly, otherwise False """

    if a_followers > b_followers: 
        return guess == "a"
    else:
        return guess == "b"
    
# If A has more followers, the function checks whether the player guessed "a".
# If B has more followers, it checks whether the player guessed "b".
# The comparison (guess == "a" or "guess == "b") returns True if the guess is correct,
# and False if the guess is wrong.

def game():
    score = 0
    should_continue = True

    account_b = random.choice(data)

    while should_continue:
         # A becomes the previous B
        account_a = account_b
        account_b = random.choice(data)

        # Ensure A and B are not the same
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"\n Compare A: {format_account(account_a)}")
        print("VS")
        print(f" Compare B: {format_account(account_b)}")

        guess = input("who has more followers? Type 'A' or 'B' :").lower()


        a_follower_count = account_a["followers"]
        b_follower_count = account_b["followers"]
        
    # Extract follower counts from each account dictionary so they can be compared numerically

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # at this point we have "check_answer" function returning True or False based on the player's guess
    # we have "format_account" function to format the account details for display
    # we have the main game loop in the "game" function that handles the game flow
    # we have the logic to ensure A and B are not the same account
    # we can use the functions and logic above to build the game

    # however, we dont have the logic to keep track of the player's score and whether to continue the game

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")