# Complete oops in python (object oriented programming system)
# why we use oops? Because procedural and functional programming are not more helpful in real world case so that is why we use oops
"""
Create a Python class named `ComplexNumber` to represent complex numbers.
Theory:
A complex number is a number that comprises a real part and an imaginary part.
It is typically written in the form a + bi, where 'a' is the real part,
and 'b' is the imaginary part, and 'i' is the imaginary unit (√-1).
Operations:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Comparison (==, !=)
"""
# To make this class, I have to understand the logic or operations of real class of complex numbers that is built-in in python
# a = 1 + 2j
# print(a)
# print(type(a))
class ComplexNumbers():
    def __init__(self,real=0,imaginary=0):
        self.real = real
        self.imaginary = imaginary
    def __str__(self):
        if self.real == 0:
            return f"{self.imaginary}i"
        elif self.imaginary < 0:
            return f"{self.real}{self.imaginary}i"
        else:
            return f"({self.real}+{self.imaginary}i)"
    def __add__(self,other):
        real_part = 0
        imaginary_part = 0
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        ans = ComplexNumbers(real_part,imaginary_part)
        return ans
    def __sub__(self,other):
        real_part = 0
        imaginary_part = 0
        real_part = self.real - other.real
        imaginary_part = self.imaginary - other.imaginary
        ans = ComplexNumbers(real_part,imaginary_part)
        return ans
    def __mul__(self,other):
        real_part = 0
        imaginary_part = 0
        real_part = self.real*other.real - self.imaginary*other.imaginary
        imaginary_part= self.real*other.imaginary + other.real*self.imaginary
        ans = ComplexNumbers(real_part,imaginary_part)
        return ans
    def __truediv__(self,other):
        real_part = 0
        imaginary_part = 0
        real_part = (self.real*other.real + self.imaginary*other.imaginary)/ (other.real**2 + other.imaginary**2)
        imaginary_part = (self.imaginary*other.real - self.real*other.imaginary) / (other.real**2 + other.imaginary**2)
        ans = ComplexNumbers(real_part,imaginary_part)
        return ans
    def __eq__(self,other):
        if self.real == other.real or self.imaginary == other.imaginary:
            return True
        else:
            return False


#testing
a = ComplexNumbers(2,7)
b = ComplexNumbers(1,3)
print(a!=b)
























