# Calculator project
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1+n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operatons ={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

# print(operatons["*"](4,8))
def calculator():
    shoud_accumulate=True
    num1=float(input("What is first number..? :"))

    while shoud_accumulate:
        for symbol in operatons:
            print(symbol)
        operation_symbol=input("Pick a symbol :")
        num2=float(input("What is second number..? :"))
        answer=operatons[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        CHOICE=input(f"type 'Y' to continue with {answer} , or type 'N' to start new calculation : ")

        if CHOICE=='Y':
            num1=answer
        else:
            shoud_accumulate=False
            print("\n"*100)
            calculator()

calculator()