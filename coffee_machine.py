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

menu_instruction = """
Welcome to Cooffii Shop - Table Menu?
1. Espresso
2. Latte
3. Cappuccino
4. Check resources level
0. Turn off the machine\n
"""

start_machine = True

while start_machine:
    choice = int(input(menu_instruction))