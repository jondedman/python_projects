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
    "money": 0
}


def update_resources(money_in):
    resources['water'] -= chosen_coffee['ingredients']['water']
    resources['coffee'] -= chosen_coffee['ingredients']['coffee']
    change = round(money_in - chosen_coffee['cost'], 2)
    print(f"Here is your change ${change}")
    resources['money'] += money_in
    print(resources)


def cost():
    money_in = 0
    while money_in < chosen_coffee['cost']:
        to_pay = round(chosen_coffee['cost'] - money_in, 2)
        if to_pay == 0:
            break
        print(f" still ${to_pay} to pay")

        money_in += (float(input("How many quarters? "))) * 0.25
        to_pay = round(chosen_coffee['cost'] - money_in, 2)
        if to_pay <= 0:
            break
        print(f" still ${to_pay} to pay")

        money_in += (float(input("How many nickles? "))) * 0.10
        to_pay = chosen_coffee['cost'] - money_in
        if to_pay <= 0:
            break
        print(f" still ${to_pay} to pay")

        money_in += (float(input("How many dimes? "))) * 0.05
        to_pay = chosen_coffee['cost'] - money_in
        if to_pay <= 0:
            break
        print(f" still ${to_pay} to pay")

        money_in += (float(input("How many cents? "))) * 0.01
        to_pay = MENU['espresso']['cost'] - money_in
        print(f" still ${to_pay} to pay")

    print(f"enjoy your {name}!")
    update_resources(money_in)


def check_resource():
    if chosen_coffee['ingredients']['water'] > resources['water']:
        print("Sorry...all out of water")
    elif chosen_coffee['ingredients']['coffee'] > resources['coffee']:
        print("Sorry...all out of coffee")
    else:
        print(f"Please insert ${chosen_coffee['cost']}")


def choice():
    option = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return option


running = True
while running:
    option = choice()

    if option in MENU:
        name = option
        chosen_coffee = MENU[option]
        check_resource()
        cost()
    elif option == "report":
        print(resources)
    elif option == "off":
        print("Turning off")
        running = False
    else:
        print("Invalid choice. Please select from espresso, latte, cappuccino.")
