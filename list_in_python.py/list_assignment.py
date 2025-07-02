# print in the same line using loop
# i = 1
# while i <= 3:
#     print("Hello Hello Hello", end = "******")
#     i +=1
# STAT PATTERN USING LOOPS
# Triangle pattern
# n = 5  #number of rows
# for q in range(1,n+1):
#     print("*"*q)
# TRIANGLE IN REVERSE
# n = 6 # number of rows
# for i in range(n,0,-1):
#     print("*"*i)
# PYRAMID PATTERN
# n = 5
# for i in range(1,n+1):
#     while n > 0:
#         print(" "*n, end="")       
#         n -=1
#         break
#     print("*"*(2*i-1))    
# PYRAMID SHORTCUT METHOD
# n = 7
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("8"*(2*i - 1))



# FACRORIAL OF A NUMBER using function and loop
# def factorial(n):
#     result = 1
#     while n >= 1:
#         result = result*n
#         n -=1
#     return result
      
    
# my = factorial(7)
# print(my)

# FIBONACCI SEQUENCE

# def fibonacci(n):
#     a,b = 0,1 
#     count = 0
#     while count < n:
#         print(a,end=" ", sep=" ")    # 0 1 1 2 3
#         # a = b
#         # b = a + b 
#         a,b = b, a+b 
#         count += 1 # 0 1 2 3 4 

# fibonacci(10)



