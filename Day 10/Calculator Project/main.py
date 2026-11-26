
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
