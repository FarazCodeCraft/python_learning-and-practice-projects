# year = int(input("Enter the year number:"))
# if (year%4==0) and (year%100==0 or year%400==0):
#     print("yes its a leap year")
# else:
#     print("its not a leap year")







# login authentication
# default_username = "Faraz"
# default_password = "faraz1026"
# import getpass
# username = input("enter your name")
# password = getpass.getpass("Enter your password: ")
# print("Password received!")  # Do not print the password in real apps
# if (username==default_username and password == default_password):
#     print("you are login")
# elif (username!=default_username and password== default_password):
#     print("your username is incorrect")
# elif (username==default_username and password!= default_password):
#     print("your password is incorrect")
# else:
#     print("incorrect Information") 




# Admission Eligibility
m1=int(input("enter you marks"))
m2=int(input("enter you marks"))
m3=int(input("enter you marks"))
total_marks = 300 - (m1+m2+m3)
second_option= m1+m2
if (m1>=65 and m2>=55 and m3>=55):
    if total_marks>=180 or second_option>=140:
        print("Congratulation! You are Eligible")
    else:
        print("you are not eligble, try again")
else:
    print("you have failed the exam")