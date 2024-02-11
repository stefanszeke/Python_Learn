from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine




is_on = True

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
    

while is_on:
    menu.print_menu()
    drink_choice = input(f'What would you like? ({menu.get_items()}): ').lower()

    if drink_choice == "off":
        is_on = False
    elif drink_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        valid_drink = menu.find_drink(drink_choice)
        if valid_drink != None:
            cost = valid_drink.cost
        else:
            continue
        
        sufficient_resources = coffee_maker.is_resource_sufficient(valid_drink)
        if not sufficient_resources:
            continue
        payment_accepted = money_machine.make_payment(cost)
        if payment_accepted:
            coffee_maker.make_coffee(valid_drink)
        
    
        # sufficient_resources = coffee_maker.is_resource_sufficient(valid_drink)
        # payment_accepted = money_machine.make_payment(cost)
        # if sufficient_resources and payment_accepted:
        #     coffee_maker.make_coffee(valid_drink)


