# Even number filtering from a list
# list = [1,2,3,4,5,6,7,8,9,10]
# even_list = [i for i in list if i % 2 == 0]
# print(list)
# print(even_list)




# # Flattening a list of lists
# list2 = [[1,2,4,5], [2,5,9], [1,9,8,4,6], ["rajaa"]]
# flatten_list = [n for lists in list2 for n in lists ]                        # flatten_list = [item for sublist in list for item in sublist]
# print(list2)
# print(flatten_list)



# # for i in "raja g":
# #     print(i)


# list = [["raja g"]]
# for i in list:
#     for n in i:
#         print(n)


#generating the list of first letters of list item
# list = ["apple", "mango", "banana", "guava", "orange"]
# first_letter_list = [ letter[0] for letter in list]
# print(first_letter_list)



# list = [1,2,3,4,5,6,7,8,9,10]
# square_list = [ square**2 for square in list if square % 2 == 0]
# print(square_list)



# list1 = ["1",2,"3",4,5,6,"123","1b", "91", 999,100, "ba", "56"]
# list2 = [int(x) for x in list1 if isinstance(x, int) or isinstance(x, str) and x.isdigit()]


# print(list2)



# string = "223"
# print(string.isdigit())





# generate a fibonacci sequence 

# 1. using normal python function
# def fibaonacci(n):
#     fib = [0,1]
#     for i in range(2,n):
#         fib.append(fib[i-1] + fib[i-2])
#     print(fib)
# fibaonacci(5)




# 2.Using list comprehension
fib = [0,1]
n = int(input("Enter your number:"))
fib_list = [fib.append(fib[n-1] + fib[n-2]) for n in range(2,n)]
print(fib_list)