import math

def calculator():
    while True:
        operation = input("Enter the operation you will be performing (+, -, *, /, sqrt, ^): ")
        num1 = float(input("Enter the first number in the calculation: "))
        if operation != 'sqrt':
            num2 = float(input("Enter the second number in the calculation: "))
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                result = "Undefined"
            else:
                result = num1 / num2
        elif operation == 'sqrt':
            result = math.sqrt(num1)
        elif operation == '^':
            result = num1 ** num2
        else:
            print("Invalid operation.")
            continue
        print(f"Your answer is: {result}")
        done = input("Are you finished (yes/no)? ")
        if done.lower() == 'yes':
            break
        else:
            continue

def main():
    calculator()