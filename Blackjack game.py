import random

def deal_card():
     """ the deal card above returns a random card from the deck """
     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
     card = random.choice(cards)
     return card

def calculate_score(cards):
     """this function is going to take a list of cards and return the score calculated from the card"""
     if sum(cards) == 21 and len(cards) == 2:
         return 0
     # '0' will represent the black jack (is a black jack) -- and this part of the code presents a blackjack

     if 11 in cards and sum(cards) > 21:
         cards.remove(11)
         cards.append(1)
     """this checks if there is an 11 in the cards and if the sum of all the cards is greater than 21 to change the ace to 1"""
     return sum(cards)


def compare(u_score, c_score):
     if u_score == c_score:
         return "Draw"
     elif c_score == 0:
         return "Lose, opponent has a black jack"
     elif u_score > 21:
         return "You went over, You lose"
     elif c_score > 21:
         return  "Opponent went over, You win"
     elif u_score > c_score:
         return "You win"
     else:
         return "you lose"

def play_game():
     user_cards = []
     # this holds the user's cards and the computer's card's
     computer_cards = []
     user_score = -1
     computer_score = -1
#     """ (using -1) and cant use '0' because that is blackjack """
     is_game_over = False
#     # this is used to help the computer know when to end the game when certain conditions are met while playing

     for _ in range(2):
         user_cards.append(deal_card())
         computer_cards.append(deal_card())
     """ repeat this block twice to deal 2 opening cards to both the player and dealer. """

     """ adding the new card to the user's card & computer card"""

     while not is_game_over:
         user_score = calculate_score(user_cards)
         """ this calculates the scores of the user's cards """
         computer_score = calculate_score(computer_cards)
         print(f"Your cards: {user_cards}, current score: {user_score}")
         print(f"computer's first card: {computer_cards[0]} ")

     if user_score == 0 or computer_score == 0 or user_score > 21:
         is_game_over = True
         # this starts out as false
     else:
         user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
         if user_should_deal == 'y':
             user_cards.append(deal_card())
         else :
             is_game_over = True


     while computer_score != 0 and computer_score < 17:
         computer_cards.append(deal_card())
         computer_score = calculate_score(computer_cards)

     print(f"Your final hand: {user_cards}, final score: {user_score}")
     print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
     print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
     print("\n" * 20)
     play_game()


