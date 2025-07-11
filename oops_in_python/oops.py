# class Student:
#     def __init__(self,name="Unknown", age=0, roll_no=0):
#       self.name = name
#       self.age = age
#       self.roll_no = roll_no
#     #   print("This is my first code in OOPs") 
# s1 = Student("Alice", 20, 101)
# s2 = Student("Bob", 22, 102)

# print(s1.age)


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def get_average(self):
#         sum = 0
#         for mark in self.marks:
#             sum += mark
#         return f"{self.name}'s average marks: {sum / len(self.marks)}"
    
# s1 = Student("Alice", [85, 90, 78,29,22,43,43])
# s1.get_average()
# s2 = Student("Bob", [88, 92, 80, 75, 95])
# s2.get_average()
# print(s1.get_average())
# print(s2.get_average()) 




# class AccountDetail():
#     def __init__(self,name,balance,account_no):
#         self.name = name
#         self.balance = balance
#         self.account_no = account_no
#     def deposit(self, amount):
#         self.balance += amount
#         return f"Deposited {amount}. New balance: {self.balance}"

#     def withdraw(self, amount):
#             self.balance -= amount
#             return f"Withdrew {amount}. New balance: {self.balance}"

#     def get_balance(self):
#         return f"Account holder: {self.name}, Balance: {self.balance}, Account No: {self.account_no}"  
# customer1 = AccountDetail("Faraz", 100, "123456789")
# print(customer1.get_balance())
# customer1.deposit(5000)
# customer1.withdraw(2000)
# print(customer1.get_balance())


# abstraction
#encapsulation


# #del keyword == it can delete object and its attributes
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}")

# s1 = Student("Alice", 20)
# s1.display()
# del s1  # Deleting the object
# print(s1.display()) # This will raise an error because s1 is deleted

# name = "Faraz"

#private attributes and methods == by using double underscore like    __name  or   __get_name()
# In private attributes, we cannot access the attributes or methods outside the class , only accessible within the class 


#inheritance == is a way to form new classes using classes that have already been defined. The new class is called a derived (or child) class, and the class it is derived from is called a base (or parent) class. 
# taking properties and methods from parent class to child class
# inherit is simple english works like a child inherits properties from his parents




# class Car:
#     @staticmethod
#     def start():
#         print("Car started") 
#     @staticmethod
#     def stop():
#         print("Car stopped")
# class Toyota(Car):
#     def __init__(self, model):
#         self.model = model


#     def display_info(self):
#         print(f"Model: {self.model}")
# car1 = Toyota("Corolla")
# car1.display_info()
# car1.start()
# car1.stop()

"""There is three types of inheritance"""
"""1.single inheritance
2.multiple inheritance
3.multilevel inheritance (including more than one parent class separated by comma)"""

# super method (are used to call the parent class methods in child class)
# classmethods (are used to call the class attribute in child class)
# propertymethod (when we give this decorator to a method, it can be accessed like an attribute and use latest value of the  other attribute)
# getter and setter

# 4.polymorphism
 
 
