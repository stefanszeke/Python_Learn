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
    "milk": 150,
    "coffee": 100,
}

coins_values = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}
coins_inserted = {
    "quarters": 0,
    "dimes": 0,
    "nickels": 0,
    "pennies": 0,
}

# TODO: 1. Print report of all coffee machine resources

is_on = True

def is_resource_sufficient(order_ingredients) -> bool:
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins() -> float:
    # quarters: int = int(input("How many quarters?: "))
    coins_inserted["quarters"] += int(input("How many quarters?: "))
    coins_inserted["dimes"] += int(input("How many dimes?: "))
    coins_inserted["nickels"] += int(input("How many nickels?: "))
    coins_inserted["pennies"] += int(input("How many pennies?: "))

    # for coin in coins_inserted:
    #     coins_inserted[coin] += locals()[coin]
        
    total = 0
    
    for coin in coins_inserted:
        total += coins_inserted[coin] * coins_values[coin]
    
    print(f"Total inserted: ${total}")
    return total
            
inserted_money = 0
while is_on:
    if inserted_money <= 0:
        inserted_money = process_coins()
    inserted_money = round(inserted_money, 2)
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ")
    
    if drink_choice == "off":
        is_on = False
    elif drink_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        if drink_choice in MENU:
            cost = MENU[drink_choice]["cost"]
            print(f"The cost of {drink_choice} is ${cost}")
        else:
            print("Sorry, we don't have that drink.")
            continue
            
        drink = MENU[drink_choice]
        if drink["cost"] > inserted_money:
            print(f'Sorry that\'s not enough money ({inserted_money}). Money refunded.')
            inserted_money = 0
            continue
        if is_resource_sufficient(drink["ingredients"]):
            print(f'serving {drink_choice}')
            for item in drink["ingredients"]:
                resources[item] -= drink["ingredients"][item]
            profit += drink["cost"]
            inserted_money = 0


