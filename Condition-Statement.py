###.........................................###
###...........if Statement in Python...........
###.........................................###


# The if statement is used to check a condition.
# Simple definition:-
# If the condition is True, the code inside if will execute. If the condition is False, it will not execute.

#........
# Syntax:-
#.......
# if condition:
#     statement

# Notice the colon : after the condition and indentation before the statement.


###:::::::::::EXAMPLE:::::::::::###

# age = 20

# if age >= 18:
#     print("You are eligible")

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::




###...........................................###
###...........elif Statement in Python........###
###...........................................###




#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::




# ###...........................................###
# ###...............Nesting in Python...........###
# ###...........................................###

# # Simple Definition:-Nesting means putting one condition inside another condition.

# # In simple words:- One if statement inside another if statement = Nested if.

# # #...........................
# # Basic Structure / Syntax:-::
# #.............................
# # if condition1:
# #     if condition2:
# #         print("Both conditions are True")

# # Notice the indentation. The second if is inside the first if.

# ###:::::::::::EXAMPLE:::::::::::###

# marks = int(input("Enter your marks: "))

# if marks >= 40:
#     if marks >= 90:
#         print("Grade A")
#     else:
#         print("Pass")
# else:
#     print("Fail")



#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::




# elif means "else if".
# It is used when we have more than one condition to check.

# Simple definition
# elif checks another condition when the previous if or elif condition is False.

#........
# Syntax:-
#.......
# if condition1:
#     statement
# elif condition2:
#     statement



###:::::::::::EXAMPLE 1 :::::::::::###

marks = 75

# if marks >= 90:
#     print("Grade A+")
# elif marks >= 60:
#     print("Grade B")

###:::::::::::EXAMPLE 2 :::::::::::###

# Light = input("Enter traffic light colour ")

# if Light == "RED":
#     print("STOP")

# elif Light == "YELLOW":
#     print("WAIT")

# elif Light == "GREEN":
#     print("GO")




#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::





###...........................................###
###................else in Python.............###
###...........................................###



# Simple Definition
# else is used when all the previous conditions are False.

# Think of it as: “If nothing above is true, do this.”


#........
# Syntax:-
#.......
# else:
#     # Statement.



###:::::::::::EXAMPLE 1 :::::::::::###

# age = 17

# if age >= 18:
#     print("You can vote")
# else:
#     print("You cannot vote")


# ###:::::::::::EXAMPLE 2 :::::::::::###

# light = input("Enter traffic light color: ")

# if light == "red":
#     print("Stop")

# elif light == "yellow":
#     print("Wait")

# elif light == "green":
#     print("Go")

# else:
#     print("Invalid color")



#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::***THE-END***::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::