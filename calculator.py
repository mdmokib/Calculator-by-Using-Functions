from art_logo import logo
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mult(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
def mod(n1, n2):
    return n1 % n2
operations = {
    "+": add,
    "-":sub,
    "*":mult,
    "/":div,
    "%":mod,
}
def calcultor1():
    print(logo)
    num1=int(input("Enter the an integer: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:   
        choose_operation = input ("Pick an oiperation which one you want to apply now: ")  
        num2=int(input("Enter the next integer: ")) 
        calculation=operations[choose_operation]
        answer=calculation(num1, num2)
        print(f"{num1} {choose_operation} {num2} = {answer}")
        if input(f"If you want to continue with {answer} type 'y' otherwise type 'n' to restart the Calculation.") == "y":
            num1=answer
        else:
            should_continue = False   
            calcultor1()
calcultor1()


