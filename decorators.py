# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before")
#         result = func(*args, **kwargs)
#         print("After")
#         return result
#     return wrapper

# @my_decorator
# def add(a, b):
#     print(f"Sum: {a + b}")

# add(5, 7)
# add(1,3 ,56,6)









# # Timing Fucntion Execution
# # write a decorator that measures a time a function takes to execute
# import time
# def time_finder(func):
#     def wrapper(*args, **kwargs):
#         print(f"start time")
#         start= time.time()
#         print(start)
#         func(*args,**kwargs)
#         end = time.time()
#         print(end)
#         print(f"end time")
#         print(f"the function{func.__name__} take {end-start} time to execute")
#     return wrapper
# @time_finder
# def exa(n):
#     time.sleep(n)
# exa(3)
# def sleep(n):
#     time.sleep(5)
# sleep(9)
# a =time.time()
# print(a) 










# """ Debugging function calls
# In this example, we create a decorator that give us function name and its arguments when it calls"""
# def debugger(func):
#     print("my name is faraz")
#     def wrapper(*args,**kwargs):
#         args_value = ", ".join(str(arg) for arg in args)   if args else "0"
#         kwargs_value =", ".join( [f"{key} = {value}" for key,value in kwargs.items()] ) if kwargs else "0"
#         print(f"this function has name {func.__name__} and args value {args_value} and kwargs value {kwargs_value}")
#         func()
#     return wrapper
# # @debugger
# # def greetings(*args, **kwargs):
# #     print("hello")
# # greetings(1,2,name="faraz",roll=1)

# @debugger
# def student(*args,**kwargs):
#     print("Hello")
# student(name="faraz",cast= "raja", work="hard")
# student(1,2,2,'afsadfasd') 

   







# "PROBLEM 3"
# "CACHE RETURN VALUES"
# "implement a decorator that caches the return values of a function, so that when it is called with the same arguments, the cached value is returned instead of re-executing the function"
# import time
# def cache(func):
#     cache_value={}
#     print(f"{cache_value} is 1")
#     def wrapper(*args):
#         print(f"{cache_value} is 2")
#         if args in cache_value:
#             return cache_value[args]
#         print(f"{cache_value} is 3")
#         result = func(*args)
#         cache_value[args] = result
#         print(f"{cache_value} is 4")
#         return result
#     return wrapper
# @cache
# def long_running_function(a,b):
#     time.sleep(3)
#     return a+b
# print(long_running_function(1,3))
# print(long_running_function(1,3))









# logs funtion call
# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} with {args} {kwargs}")
#         return func(*args, **kwargs)
#     return wrapper
# @log
# def multiply(x, y):
#     return x * y
# print(multiply(3, 4))








# decorator that times a function
# import time
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"Execution Time: {end - start:.5f} seconds")
#         return result
#     return wrapper

# @timer
# def slow(m):
#     time.sleep(m)
#     print("Finished!")

# slow(3)














# Decorators to count calls
# def count_calls(func):
#     def wrapper(*args, **kwargs):
#         wrapper.calls += 1
#         print(f"Call {wrapper.calls}")
#         return func(*args, **kwargs)
#     wrapper.calls = 0
#     return wrapper

# @count_calls
# def greet():
#     print("Hello!")

# greet()
# greet()
# greet()







# Authentication check
    # def require_login(func):
    #     def wrapper(user):
    #         if user == "admin":
    #             return func(user)
    #         else:
    #             print("Access denied.")
    #     return wrapper

    # @require_login
    # def dashboard(user):
    #     print(f"Welcome to dashboard, {user}!")

    # dashboard("admin")
    # dashboard("guest")






# Input Validation
# def check_positive(func):
#     def wrapper(n):
#         if n < 0:
#             print("Only positive numbers allowed.")
#         else:
#             return func(n)
#     return wrapper

# @check_positive
# def square(n):
#     print(n * n)

# square(5)
# square(-3)






# Debug Decorator
# def debug(func):
#     def wrapper(*args, **kwargs):
#         print(f"Function {func.__name__} called with {args}, {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Function {func.__name__} returned {result}")
#         return result
#     return wrapper

# @debug
# def divide(a, b):
#     return a / b
# divide(10, 2)


# Limit function calling
# def func_limit(func):
#     def wrapper(*args, **kwargs):    
#         if wrapper.calls > 3:
#              wrapper.calls +=  1
#              return func(*args, **kwargs)
#         else:
#             return "your limit has been completdd"
            
#     wrapper.calls = 0
#     return wrapper
# @func_limit
# def greet():
#     print("Hello!")

# print(greet())
# greet()
# greet()




# user = {'is_logged_in': False}   # here in this case our user is not logged in
# def require_login(func):
#     def wrapper(*args, **kwargs):
#         if wrapper.calls < 3:
#             wrapper.calls += 1
#             if user['is_logged_in']:
#                 return func(*args, **kwargs)
#             else:
#                 print("You must log in first!")
#         else:
#             return "your tries are ended"
#     wrapper.calls = 0
#     return wrapper

# @require_login
# def view_dashboard():
#     print("Welcome to your dashboard!")
# view_dashboard()  
# view_dashboard()  
# user['is_logged_in'] = True        # here in this case user is logged in 
# view_dashboard()  
# user['is_logged_in'] = False
# print(view_dashboard())


# def why_not():
#     print("you are the first to one who brings me to at all")
# why_not.new = 123
# print(why_not.new)



# my_dict = {"new": "first item", "chl": 123}
# print(my_dict["chl"])
# my_dict["new"]=23423
# print(my_dict["new"])


# my_set = set({ })
# print(type(my_set))
# squares = {x: x**2 for x in range(5)}
# print(squares)

# unique_chars = {char for char in 'hello'}
# print(unique_chars)







# DUMMY PASSWORD CHECKER
# def limit_checker(func):
#     def wrapper(*args):
#         if wrapper.calls < 3:
#             wrapper.calls += 1
#             return func(*args)
#         else:
#             print("You have tried lot of times, failed to try again")
#     wrapper.calls = 0
#     return wrapper
# @limit_checker
# def pass_ent():
#     print("you have entered wrong password, please try again")
# pass_ent()
# pass_ent()
# pass_ent()
# pass_ent()



