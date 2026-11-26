from art import logo
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operation = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}

result = operation["*"](n1 = 4 ,n2 =8)
print(result)

def calculator():
    print(logo)
    calculation_process = True
    num1 = float(input("Enter number"))
    while calculation_process:
        for symbol in operation:
            print(symbol)
        operator = input("pick symbol from above")
        num2 = float(input("Enter Next number"))
        result = operation[operator](num1,num2)
        print(result)

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if choice == "y":
            num1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()