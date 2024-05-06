from art import logo
import os

print(logo)

# Calculator
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def power(n1, n2):
    return n1 ** n2

def root(n1, n2):
    return n1 ** (1/n2)

def modulo(n1, n2):
    return n1 % n2

operations = {
    "+": add, 
    "-": subtract,
    "x": multiply,
    "/": divide,
    "^": power,
    "sqrt": root,
    "%": modulo,
    }
def calculator():
    num1 = float(input("What's the first number?: "))
    num2 = float(input("What's the second number?: "))
    for symbol in operations:
        print(symbol)
        
    operation_symbol = input("Pick an operation from the line above: ")
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    calculator_finish = False

    while not calculator_finish:
        y_or_n = input(f"Type 'y' to continue with {answer}, or type 'n' to exit.\n")
        if y_or_n == "y":
            operation_symbol = input("Pick an operation: ")
            num3 = float(input("What's the next number? "))
            next_answer = operations[operation_symbol](answer, num3)
            print(f"{answer} {operation_symbol} {num3} = {next_answer}")
            answer = next_answer
        else:
            calculator_finish = True
            os.system("cls")
            calculator()
calculator()
