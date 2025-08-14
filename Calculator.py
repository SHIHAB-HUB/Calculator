operator = input("Enter an operator (+, -, *, /): ")

num1 = float(input("Number 1: "))
num2 = float(input("Number 2: "))

if (operator == '+'):
    print(f"Result = {num1+num2}")
elif (operator == '-'):
    print(f"Result = {num1-num2}")
elif (operator == '*'):
    print(f"Result = {num1*num2}")
elif (operator == '/'):
    print(f"Result = {num1/num2}")
else:
    print("You enter an wrong operator.")
