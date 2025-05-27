print("Enter an operator: +, -, *, /, //, %, **")
operator = input("Operator: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

match operator:
    case '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    case '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    case '*':
        print(f"{num1} * {num2} = {num1 * num2}")     
    case '/':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Cannot divide by zero.")
    case '//':
        if num2 != 0:
            print(f"{num1} // {num2} = {num1 // num2}")
        else:
            print("Error: Cannot divide by zero.")
    case '%':
        if num2 != 0:
            print(f"{num1} % {num2} = {num1 % num2}")
        else:
            print("Error: Cannot take modulus by zero.")
    case '**':
        print(f"{num1} ** {num2} = {num1 ** num2}")
    case _:
        print("Invalid operator")                   