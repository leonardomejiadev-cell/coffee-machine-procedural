"""
Coffee Machine Program
A simple coffee machine simulator that manages resources, processes payments,
and dispenses coffee drinks.
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def run_coffee_machine():
    """
    Main function that runs the coffee machine program.
    Continuously prompts user for drink selection and processes orders
    until the machine is turned off.
    """
    is_on = True
    while is_on:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_choice == "off":
            turn_off_machine()
            is_on = False
        elif user_choice == "report":
            print_report()
        elif user_choice in MENU:
            process_order(user_choice)
        else:
            print("Invalid selection. Please choose espresso, latte, or cappuccino.")


def turn_off_machine():
    """Turns off the coffee machine and exits the program."""
    print("Turning off the coffee machine. Goodbye!")
    exit()


def print_report():
    """Prints the current status of all resources and profit."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def process_order(drink):
    """
    Processes a complete coffee order from checking resources to dispensing the drink.

    Args:
        drink (str): The type of coffee drink ordered (espresso/latte/cappuccino).
    """
    if check_resources(drink):
        payment = process_coins()
        if is_transaction_successful(drink, payment):
            make_coffee(drink)


def check_resources(drink):
    """
    Checks if there are sufficient resources to make the requested drink.

    Args:
        drink (str): The type of coffee drink to check.

    Returns:
        bool: True if sufficient resources are available, False otherwise.
    """
    for ingredient in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    """
    Prompts the user to insert coins and calculates the total amount.

    Returns:
        float: The total monetary value of coins inserted.
    """
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(drink, payment):
    """
    Checks if the payment is sufficient for the drink and processes the transaction.

    Args:
        drink (str): The type of coffee drink ordered.
        payment (float): The amount of money inserted by the user.

    Returns:
        bool: True if payment is sufficient, False otherwise.
    """
    drink_cost = MENU[drink]["cost"]

    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")

        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry, that's not enough money. Money refunded: ${payment}")
        return False


def make_coffee(drink):
    """
    Deducts the required ingredients from resources and dispenses the drink.

    Args:
        drink (str): The type of coffee drink to make.
    """
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
    print(f"Here is your {drink} ☕️. Enjoy!")


if __name__ == "__main__":
    run_coffee_machine()

