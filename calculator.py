# Function to perform calculation and return result
def calculator():
    print("Welcome to Smart Calculator!")

    # Taking input from user
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    # Using conditional statements
    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "❌ Error: Cannot divide by zero!"

    else:
        return "❌ Invalid operator! Use +, -, *, or / only."

# Call the function and store the result
calculator()