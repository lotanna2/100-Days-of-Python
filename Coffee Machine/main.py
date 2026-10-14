MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

profit = 0 ## initial profit in the machine

resources = { ## initial resources in the machine
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients): ## a function to check if the resources are sufficient for the order
   for items in order_ingredients:
       if order_ingredients[items] >= resources[items]: ## check if the order ingredients are greater than or equal to the resources
           print(f"Sorry there is not enough {items}.")
           return False
   return True

def process_coins(): ## a function to process the coins inserted by the user
    print ("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25 ## calculate the total amount of money inserted by the user to pay for the drink
    total += int(input("how many dimes?: ")) * 0.10 ## add the amount of dimes inserted by the user to the total
    total += int(input("how many nickels?: ")) * 0.05 ## add the amount of nickels inserted by the user to the total
    total += int(input("how many pennies?: ")) * 0.01 ## add the amount of pennies inserted by the user to the total
    return total ## sends the final total back to where the function was called

def is_transaction_successful(money_received, drink_cost): ## a function to check if the transaction is successful
    """Returns True when the payment is accepted, or False if money is insufficient." ## a docstring to explain what the function does"""
    if money_received >= drink_cost: ## check if the money received is greater than or equal to the cost of the drink   
        global profit ## declare the profit variable as global so that it can be accessed and modified outside of the function
        profit += drink_cost ## add the cost of the drink to the profit
        return True
    else: 
        print("Sorry that's not enough money. Money refunded.") ## if the money received is less than the cost of the drink, print a message to the user  
        return False

def make_coffee(drink_name, order_ingredients): ## a function to make the coffee
    """Deduct the required ingredients from the resources.""" ## a docstring to explain what the function does
    for item in order_ingredients: ## loop through the order ingredients
        resources[item] -= order_ingredients[item] ## we're looking inside the resources and deducting the order ingredients from them
    print(f"Here is your {drink_name} ☕️. Enjoy!") ## print a message to the user that their drink is ready

is_on = True ## a variable to keep the machine running 

while is_on:
    choice = input("what would you like? (espresso/latte/cappuccion)")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit:.2f}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]): ## check if the resources are sufficient for the order by getting the ingredients of the drink from the MENU dictionary and passing it to the function
            payment = process_coins() ## process the coins inserted by the user and get the total amount of money inserted
            if is_transaction_successful(payment, drink["cost"]): ## check if the transaction is successful by passing the total amount of money inserted and the cost of the drink to the function
                make_coffee(choice, drink["ingredients"]) ## make the coffee by passing the drink name and its ingredients to the function