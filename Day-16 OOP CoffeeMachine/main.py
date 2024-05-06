from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

coffee_on = True
while coffee_on: 

    order = input(f"What would you like? ({menu.get_items()}): ")


    if order == "off":
        coffee_on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order_menu = menu.find_drink(order)
        if order_menu:
            if coffee_maker.is_resource_sufficient(order_menu) and money_machine.make_payment(order_menu.cost):
                    coffee_maker.make_coffee(order_menu)
    