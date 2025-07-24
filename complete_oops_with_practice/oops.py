# Complete oops in python (object oriented programming system)
# why we use oops? Because procedural and functional programming are not more helpful in real world case so that is why we use oops
# """
# Create a Python class named `ComplexNumber` to represent complex numbers.
# Theory:
# A complex number is a number that comprises a real part and an imaginary part.
# It is typically written in the form a + bi, where 'a' is the real part,
# and 'b' is the imaginary part, and 'i' is the imaginary unit (√-1).
# Operations:
# 1. Addition (+)
# 2. Subtraction (-)
# 3. Multiplication (*)
# 4. Division (/)
# 5. Comparison (==, !=)
# """
# # To make this class, I have to understand the logic or operations of real class of complex numbers that is built-in in python
# # a = 1 + 2j
# # print(a)
# # print(type(a))
# class ComplexNumbers():
#     def __init__(self,real=0,imaginary=0):
#         self.real = real
#         self.imaginary = imaginary
#     def __str__(self):
#         if self.real == 0:
#             return f"{self.imaginary}i"
#         elif self.imaginary < 0:
#             return f"{self.real}{self.imaginary}i"
#         else:
#             return f"({self.real}+{self.imaginary}i)"
#     def __add__(self,other):
#         real_part = 0
#         imaginary_part = 0
#         real_part = self.real + other.real
#         imaginary_part = self.imaginary + other.imaginary
#         ans = ComplexNumbers(real_part,imaginary_part)
#         return ans
#     def __sub__(self,other):
#         real_part = 0
#         imaginary_part = 0
#         real_part = self.real - other.real
#         imaginary_part = self.imaginary - other.imaginary
#         ans = ComplexNumbers(real_part,imaginary_part)
#         return ans
#     def __mul__(self,other):
#         real_part = 0
#         imaginary_part = 0
#         real_part = self.real*other.real - self.imaginary*other.imaginary
#         imaginary_part= self.real*other.imaginary + other.real*self.imaginary
#         ans = ComplexNumbers(real_part,imaginary_part)
#         return ans
#     def __truediv__(self,other):
#         real_part = 0
#         imaginary_part = 0
#         real_part = (self.real*other.real + self.imaginary*other.imaginary)/ (other.real**2 + other.imaginary**2)
#         imaginary_part = (self.imaginary*other.real - self.real*other.imaginary) / (other.real**2 + other.imaginary**2)
#         ans = ComplexNumbers(real_part,imaginary_part)
#         return ans
#     def __eq__(self,other):
#         if self.real == other.real or self.imaginary == other.imaginary:
#             return True
#         else:
#             return False





#Encapsulation in python
"""
Question: Suppose there is a software in school in which teachers store result and details related to school and students, now in reult days
one of student find that their number is little low and he can be fail so he somehow get school software, 
Now you have to make that software, in which you have to store details in such a way that no one can access
"""
# class Student():
#     __school_name= "Nimmal school and college"
#     number_of_students = 0
#     def __init__(self,stu_name,stu_roll,stu_class,stu_marks):
#         self.stu_name = stu_name
#         self.stu_roll = stu_roll
#         self.stu_class = stu_class
#         self.__marks = stu_marks

#     def get_marks(self):
#         return f"your marks are {self.__marks}"
#     def set_marks(self,new_marks,password):
#         if password == Student.__auth():
#             self.__marks = new_marks
#         else:
#             return f'who are you to change numbers'
#     def __auth():
#         return "0000"
#     @staticmethod
#     def get_school_name():
#         return f"{Student.__school_name}"
#     def set_school_name():
#         pass
# Student.number_of_students
# print(Student.number_of_students)
# Student.__school_name = "new"
# print(Student.__school_name)
# print(Student.get_school_name())
# student_1 = Student("saad ali",1,12,1066)
# # print(student_1.stu_name,student_1.stu_class,student_1.get_school_name(),student_1.get_marks())
# student_1.set_marks(1088,"0000")
# print(student_1.get_marks())
# #now we created a class in which no one can only change student marks when he knows password 






"""
INHERITANCE IN PYTHON AND SUPER KEYWORD IN PYTHON
inheritance means taking parents properties and functionalities in real life, same concept in oops
FUNNY EXAMPLE: Let say got create a person and he became a father, so god think that why I put effort on passing prperties and method to child, so god just copy paste father qualities in child, that is inheritance
POINT: like in in real life, child take properties from parents, not parent takes form child, same concept here
SUPER() KEYWORD: super() keyword is used to access parents methods (not properties) and super key word work internally (only in inherited classes scopes)
"""


# class Student():
#     __school_name= "Nimmal school and college"
#     __number_of_students = 0
#     def __init__(self,stu_name,stu_roll,stu_class=None,stu_marks=None):
#         self.stu_name = stu_name
#         self.stu_roll = stu_roll
#         self.stu_class = stu_class
#         self.__marks = stu_marks
#         Student.__number_of_students += 1
#     def __display(self):
#         return f"{self.stu_name,self.stu_roll,self.stu_class,self.__get_marks()}"
#     def __str__(self):
#         return f"{self.__display()}"   
#     @staticmethod
#     def get_number_of_student():
#         return f'{Student.__number_of_students}'
#     def set_number_of_students(new_number):
#         Student.__number_of_students = new_number   
#     def __get_marks(self):
#         return f"your marks are {self.__marks}"
#     def set_marks(self,new_marks,password):
#         if password == Student.__auth():
#             self.__marks = new_marks
#         else:
#             return f'who are you to change numbers'   
#     def __auth():
#         return "0000"
#     @staticmethod
#     def get_school_name():
#         return f"{Student.__school_name}"
#     def set_school_name():
#         pass


# stu1=Student('faraz',1,13,486)
# print(stu1)
# stu2=Student('saad',2,13,586)
# print(stu2)
# stu3=Student('ammar',3,13,506)
# print(stu3)
# stu4=Student('zain',4,13,386)
# print(stu4)
# print(Student.get_number_of_student())
# print(Student.get_school_name())
# # print(stu3.__get_marks)        here is the error that student has no attribut get_marks bcz we have set it as private modifiers

# # now we have created a normal student class that funcitoning well, now we all going to create another class of students but this time these student are of gradutaion

# class bsStudents(Student):
#     def __init__(self, stu_name, stu_roll, stu_year, stu_gpa,):
#         super().__init__(stu_name, stu_roll,None,None)
#         self.stu_year = stu_year
#         self.stu_gpa = stu_gpa
#     def __str__(self):
#         return f"Name:{self.stu_name}| Roll number: {self.stu_roll} | year:{self.stu_year} | GPA:{self.stu_gpa}"

# bs_stu1 = bsStudents('umair',1,"3rd",4.7)
# print(bs_stu1)

# # NOW WE INHERIT A NEW CLASS FOR BS STUDENTS TO OUR ORIGINAL CLASS STUDENT



#NOW WE ARE GOING TO PRACTICE INHERITANCE

# class Insta:
#     def __init__(self):
#         self.__name = "instagramian"
#         self._reels = "all types"
#         self.name = "mayank"
#     def login(self):
#         return "loggged innnnnnnnnnnnnnnnn",self.name,self._reels,self.__name
        
    
#     def logout(self):
#         return "loggggged   out" 

# class InstaUser(Insta):
#     def __init__(self):
#         super().__init__()
#     def login(self):
#         return super().login()




# user1 = InstaUser()
# print(user1.login())
# print(user1.name)



# class Insta:
#     def __init__(self):
#         self.__name = "instagramian"
#         self._reels = "all types"
#         self.name = "mayank"
    
#     def login(self):
#         return "loggged innnnnnnnnnnnnnnnn", self.name, self._reels, self.__name
    
#     def logout(self):
#         return "loggggged   out" 

# class InstaUser(Insta):
#     def __init__(self):
#         super().__init__()  # FIXED

# user1 = InstaUser()
# print(user1.login())  # add () to call the method
# print(user1.name)     # this will now work

# TYPES OF INHERITENCE  




# 1.SIMPLE
# class GrandFather():
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age
#     def speak(self):
#         return f"He speaks very more but wisely"
# class Father(GrandFather):
#     def __init__(self, name, age,occupation):
#         super().__init__(name, age)
#         self.occupation = occupation
#     # def speak(self):
#     #     return f'father speak carefully'
#     def show_occupation(self):
#         return f'father occupation is: {self.occupation}'   
# dada = GrandFather('fazal',65)
# print(dada.speak())
# papa = Father('asif', 55,"Business man")
# print(papa.occupation)
# print(papa.speak())
# # so these is general inheritance




#2.HIERARCHICAL
# make an example of youtube in which there is main user class and that gives properties to logged in users and logged out users
# class User():
#     def __init__(self,name,id=None, key = None):
#         self.name = name
#         self.id = id
#         self.key = key
#     def __key(self):
#         return "0000"
# class LoginUser(User):
#     def __init__(self, name, id=None, key=None):
#         super().__init__(name, id, key)
#     def like_videos(self):
#         if self.id == None or self.key == None:
#             return "please login to get more features"
#         else:
#             return "here is your like videos"
# class LogOut(User):
#     def __init__(self, name, id=None, key=None):
#         super().__init__(name, id, key)
#     def like_videos(self):
#         if self.id == None or self.key == None:
#             return "please signup to get name and key to get more features"
#         else:
#             return "please sign in to get more features"

# loginuser1 = LoginUser('raja g',234,0000)
# print(loginuser1.like_videos())
# user2 = LogOut('faraz')
# print(user2.like_videos())



# 3.MULTILEVEL INHERITENCE
# make a grandfather class and then father and then child. you can access grandfather properties in child.
# EXAMPLE: first you ask money for your wallet,  