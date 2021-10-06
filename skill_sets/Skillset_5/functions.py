
def get_requirements():
    print("Python Selection Structures")
    print("\nProgram requirements:\n")
    print("1. Use Python selection structure\n")
    print("2. Prompt user for two numbers, and a suitable operator\n")
    print("3. Test for correct numeric operator\n")
    print("4. Replicate displasy below\n")

def get_input():
    print("Python Calculator")
    num1 = input("Enter num1: ")
    num2 = input("Enter num2: ")
    print("\nSuitable operators: +,-,*,/,//(integer division, %(modulo operator), **(power)")
    operator = input("Enter operator: ")

    if num1.isnumeric() == True and num2.isnumeric() == True:
        n1 = float(num1)
        n2 = float(num2)
        operate(n1, n2, operator)

    else: 
        print("Enter numbers not language")

def operate(num1, num2, operator):
    if operator == "+":
        num3 = num1 + num2
        print(num3)

    elif operator == "-":
        num3 = num1 - num2
        print(num3)
    
    elif operator == "*":
        num3 = num1 * num2

    elif operator == "/":
        if (num2 == 0):
            print("Can't divide by zero")

    elif operator == "//":
        if (num2 == 0):
            print("Can't divide by zero")
        else:
            num3 = num1 // num2
            print(num3)

    elif operator == "%":
        if (num2 == 0):
            print("Can't divide by zero")

        else: 
            num3 = num1 % num2
            print(num3)

    elif operator == "**":
        num3 = num1 ** num2
        print(num3)

    else:
        print("Illegal operator!")



    
    