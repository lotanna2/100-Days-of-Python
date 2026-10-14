from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



#                   MAIN PROGRAM
#                         │
 #         ┌──────────────┼──────────────┐
 #         ↓              ↓              ↓
 #      MENU        COFFEE MAKER   MONEY MACHINE
 #        │              │              │
 #    Drinks        Ingredients       Money
 #    Prices        Resources         Payment
 #        │              │              │
 #        └──────────────┼──────────────┘
  #                      ↓
  #                Customer order ##

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
"""we can use the Menu class to get the items and find the drink that the user
 wants to order. We can use the CoffeeMaker class to check if there are 
 enough resources to make the drink and to make the drink. 
 We can use the MoneyMachine class to process the payment for the drink."""

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"what would you like? ({options}): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else: 
        drink = menu.find_drink(choice)
        if drink is None: 
            print("Sorry, that drink is not available.")
        else:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink) 
