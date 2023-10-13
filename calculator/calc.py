from colorama import init, deinit
import os

from art import logo

def clear():
    init(autoreset=True)
    os.system("cls" if os.name == "nt" else "clear")
    deinit()

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)
    num1 = float(input("Pick a number: "))

    should_continue = True
    while should_continue:
        for operation in operations:
            print(operation)

        operator = input("Choose an operator from the line above: ")

        num2 = float(input("What's the next number? "))

        calculation_function = operations[operator]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")

        should_continue = input(
            f"Type 'y' to continue calculating {answer}, or Type 'n' to start a new calculation: "
        ).lower()
        if should_continue == "y":
            num1 = answer
        else:
            clear()
            should_continue = False
            calculator()


calculator()
