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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

resources["money"] = 0

def check_resources(resources, MENU, action):
    ingredients = MENU[action]["ingredients"]
    enough_resource = True
    for key1, values1 in resources.items():
        for key2, values2 in ingredients.items():
            if key1 == key2 and values1 < values2 and key1 != "money":
                enough_resource = False
                return key1
    if enough_resource:
        return 0
    
def get_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    return 0.25*quarters + 0.10*dimes + 0.05*nickels + 0.01*pennies

def check_coins(resources, menu, total_coins, action):
    price = menu[action]["cost"]
    if total_coins >= price:
        resources["money"] += price
        change = round(total_coins - price, 2)
        if change > 0:
            print(f"Here is ${change} dollars in change.")
        return True
    elif total_coins < price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def deduct_resources(resources, menu, action):
    for key1, values1 in resources.items():
        for key2, values2 in menu[action]["ingredients"].items():
            if key1 == key2 and key1 != "money":
                resources[key1] -= values2
    
coffee_status = True # means on
while coffee_status:
    action = input("What would you like? (espresso/latte/cappuccino): ")
    if action == "report":
        for key, value in resources.items():
            if key == "money":
                print(f"{key.title()}: ${value}")
            elif key in ["milk", "water"]:
                print(f"{key.title()}: {value}ml")
            else:
                print(f"{key.title()}: {value}g")
    elif action in ["espresso", "latte", "cappuccino"]:
        result = check_resources(resources, MENU, action)
        if result == 0:
            total_coins = get_coins()
            print("Total coins", total_coins)
            if check_coins(resources, MENU, total_coins, action):
                deduct_resources(resources, MENU, action)
                print(f"Here is your {action}. Enjoy!")
        else:
            print(f"Sorry there is not enough {result}.")
    elif action == "off":
        coffee_status = False
        print("Coffee machine is under maintenance.")