from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


# Output
# What would you like? (latte/espresso/cappuccino/): report
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# What would you like? (latte/espresso/cappuccino/): latte
# Please insert coins.
# How many quarters?: 12
# How many dimes?: 12
# How many nickles?: 12
# How many pennies?: 12
# Here is $2.42 in change.
# Here is your latte ☕️. Enjoy!
# What would you like? (latte/espresso/cappuccino/): report
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# What would you like? (latte/espresso/cappuccino/): latte
# Sorry there is not enough water.
# Sorry there is not enough milk.
# What would you like? (latte/espresso/cappuccino/): off
