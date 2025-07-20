# # funtion in python
# def faraz(age,height):
#     return print(f"you are very tall bcz your height is {height} and still your are just {age} year old ")
# my_self = faraz(19.5,5.5)
# print( my_self)
# print(type(my_self))

# print function always return none value
# age = 18
# print(age)
# print(type(age))
# height = 19
# result = print(age+height)
# print(result)
# print(type(result))

# basic calculator function
# num1 = float(input("Enter your first number:"))
# num2 = float(input("Enter your second number:"))
# operators = input("Enter the operator")  
# if operators == "+":
#     result = num1+num2
# elif operators == "-":
#     result = num1 - num2
# elif operators == "/":
#     result = num1 / num2
# elif operators == "*":
#     result = num1 * num2
# elif operators == "%":
#     result = num1 % num2
# else:
# #     print("Please enter valid numbers and operators")
# # print(result)




# # Function to perform calculation and return result
# def calculator():
#     print("Welcome to Smart Calculator!")

#     # Taking input from user
#     num1 = float(input("Enter the first number: "))
#     operator = input("Enter an operator (+, -, *, /): ")
#     num2 = float(input("Enter the second number: "))

#     # Using conditional statements
#     if operator == "+":
#         return num1 + num2

#     elif operator == "-":
#         return num1 - num2

#     elif operator == "*":
#         return num1 * num2

#     elif operator == "/":
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "❌ Error: Cannot divide by zero!"

#     else:
#         return "❌ Invalid operator! Use +, -, *, or / only."

# # Call the function and store the result
# result = calculator()


# # Now print the result outside the function
# print("✅ Result:", result)          
# # result
# # print(type(result))


# def new_calculator():
#     print("Welcome to our new calculator")
#     number1 = float(input("Enter your first number"))
#     number2 = float(input("Enter your second number"))
#     operator = input("Enter your operator")
#     if operator=="+":
#         return number1+number2
# def chk_method(*args):
#     for arg in args:
#         print(arg)
# practice = chk_method(1,2,3,4,5,6,7,8,9)
# print(practice)
# print(type(practice))


#Function argument describer
def all_arguments(fx):
    def wrapper(*args, **kwargs):
        print(f"Function name is {fx.__name__} and it holds values {fx.__code__.co_varnames}")
        return fx(*args, **kwargs)
    return wrapper
@all_arguments
def greetings(name, age):
    return f"Hello {name}, you are {age} years old!"
# Call the decorated function
result = greetings("Faraz", 19)
print(result)
print(type(result))

