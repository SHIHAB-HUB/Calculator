operator = input("Enter an operator (+, -, *, /): ")

# Taking Inputs
num1 = float(input("Number 1: "))
num2 = float(input("Number 2: "))

# functions for Arithmetic operation

def sum(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2



if (operator == '+'):
    print(f"Result = {sum(num1,num2)}")
elif (operator == '-'):
    print(f"Result = {sub(num1,num2)}")
elif (operator == '*'):
    print(f"Result = {multiply(num1,num2)}")
elif (operator == '/'):
    print(f"Result = {divide(num1,num2)}")
else:
    print("You enter an wrong operator.")
