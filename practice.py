# # print(""" Python is fun.
# # "quotes" and double 'quotes' are tricky""")
# # customer_name,customer_age,customer_city="faraz",18.5,"gujar khan"
# # print("customer detail is shown ahead      ", customer_name, customer_age, "and he belongs to",         customer_city)
# print(f"Python is fun.\n\'qoutes\' and \"double quotes\" are tricky.")
# name = 'faraz'
# age =18
# city = "gujar khan"
# data=f"My name is {name} amd my age is {age} and I am currently living in {city}      yo yo"
# print(data)

# a= 22.99
# print(type(a))
# a=int(a)
# print(a)

# print(type(a))
# b=2
# print(type(b))
# b=float(b)
# print(type(b))
# print(b)


# Input function
# Write program of students result card
# name=input("enter your name: ") 
# age=input("enter your age: ") 
# total_marks=int(input("enter your total marks: ")) 
# obtained_marks=int(input("enter your ob marks: "))
# result=f"Dear {name} of age {age} ,\nYou have scored {obtained_marks} from total {total_marks} marks.\nYour percentage is {obtained_marks/total_marks*100}" 
# print(result)



# assignment2
# student_name=input("enter your name : ")
# sub1=float(input())
# sub2=float(input())
# sub3=float(input())
# total_marks= sub1+sub2+sub3
# percentage=(total_marks/300)*100
# result=f"dear {student_name} , you have scored {total_marks} with percentage of {percentage}%"
# print(result)




# assignment2b
# dict_task ={ "student_name": "faraz","age": 19, "height": 5.6 , "student status": " not hardworking"}
# print(dict_task) 
# print(dict_task["student status"])
# dict_task["learning stage"]= "just starting"

# print(dict_task)
# print(dict_task["learning stage"])





# my_dict = {}
# my_dict['name']=str(input("enter your name: "))
# my_dict['age']=int(input("enter your age: "))
# my_dict['height']=float(input("enter your height: "))
# print(my_dict)


# if 5<8:
#     print(" 5 is less than 8")
# marks = int(input("Enter your marks: "))
# if marks>90:
#     print("you are topper of class")
# elif marks>70:
#     print("you are average student of class")
# elif marks>50:
#     print("you are not good student")
# else:
#     print("you have to leave class")
    




# Program for checking that user is allowed to drive or not
# Program for checking that user is allowed to drive or not
# age = int(input("Enter your marks: "))

# if age > 18:
#     print("yes user is above 18 ")
#     user_liscense = str(input("you have liscense?   yes/no:  "))
#     if user_liscense.lower() == "yes":
#         print("And user have liscense too so you are aoowed to drive")
#     else:
#         print("but you have no liscense so you are not allowed")
# else:
#     print("user is under 18 and this signifies that he will not have liscense so you aer not allowed")


# leap year program
# yearaa = int(input("Enter year faraz: "))
# if yearaa % 4== 0:
#     print(f"{yearaa} is a leap year")
# else:
#     print(f"{yearaa} is not a leap year")



# Funtion Arguments: there are four types of function arguments
# 1.requires    2.default      3.kerword arguments(postional arguments: no use of name)        4.Arbitrary arguments
# arbitrary positional arguments *   stored as tuple which is immutable
# arbitrary keyword arguments   **   stored as dictionary which is key value pair
# def calculate_total(*item_total):
#     items = sum(item_total)
#     print(f"your total bill is {items}")
# calculate_total(1,3,4,5,56,6,4)





# STRING METHODS


# string indexing == accessing string's index which start from 0 in positive and from -1 from negative
# name = 'faraz'
# print(name[3])       # here output is a   
# print(name[-1]) # here output is z 
# space is also included in index


# String Slicing
# access of subsets of string (range of string)
# name = "Abdul"
# print(name[0:4])
# print(name[0:4:2])                      [   start(including) :    end(exclusive)   :    step(how many characters jump)  ]
#by default       start has value 0 and  end has value equal to the length of string


# reverse_string = 'New string'
# print(reverse_string[::-1])   # here output is in reverse order bcz we have reverse the step part


# #string method
# example = "Hello Faraz"
# #len()
# print(len(example)   )


# pi = 3.145666565
# formatted_pi = f"formatted pi is {pi:.3f}"
# print(formatted_pi)

# my_string = "python course"
# print(my_string[2:10:2])
#we take three inputs from user and then make a function in which we use condition to return some answer in function and then call this funtion using some variable
# pi = 3.143434534
# print("value of pi is {}".format(pi))
# print("{:.3f}".format(pi))



#MIDDLE CHARACTER USING 
#for even characters , centre characters are 2
#for odd characters , centre character is easy to track

# name = input("Enter your name:")
# def mid_str(word):
#     middle = int(len(word)/2)
#     if len(word) % 2 == 0:
#         return word[middle-1:middle+1]
#     else:
#         return word[middle]


# print(mid_str(name))




My_word = "regression analysis"
print(My_word[3:-3])

again_word = "classification"
print(again_word[len(again_word)-4::])


print(again_word[::-1])


palandrom = "talat"
def is_palandrom(s):
    if s==s[::-1]:
        print("yes it is palandrom")
    else:
        print("not palandrom")
is_palandrom(palandrom)
