# #Q1>) WAP to input user's name and print its length.

# name = input("Enter your name: ")

# print("Length of your name:", len(name))

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#  #Q2.) WAP to find the occurance of '$' in a string

# text = input("Enter a string: ")

# print("Occurrence of '$':", text.count("$"))

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# #Q.3) Conditional Statements


# # Conditional Statements
# # Grade students based on marks
# # marks >= 90, grade = “A”
# # 90 > marks >= 80, grade = “B”
# # 80 > marks >= 70, grade = “C”
# # 70 > marks, grade = “D”


# marks = int(input("Enter your marks :-"))

# if marks >= 90 :
#     grade = "A"

# elif (marks >= 80 and marks < 90) :
#     grade = "B"

# elif (marks >= 70 and marks < 80) :
#     grade = "C"

# else:
#     grade = "D"

# print("Gade of student ->" , grade)
# print("FAIL")


#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


#Q.4)WAP to check if a number entered by the user is odd or even.

# num = int(input("Enter your number :"))

# if (num % 2 == 0):
#     print("Even number")

# else :
#     print("Odd Number")


#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# #Q.5)WAP to find the greatest of 3 numbers entered by the user.

# a = int(input("Enter your first number :- "))
# b = int(input("Enter your first number :- "))
# c = int(input("Enter your first number :- "))

# if (a > b and b > c) :
#     print("greatest number is a")

# elif (b > a and a > c):
#     print("greatest number is b")

# else :
#     print("greatest number is c")



#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::




# #Q6.)WAP to check if a number is a multiple of 7 or not.

# num = int(input("Enter your number :-"))

# if num % 7 == 0 :
#     print("Number is a Multiple of 7")

# else:
#     print("Number is not multile of 7")