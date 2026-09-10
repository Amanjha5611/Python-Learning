# print("Hello CodeWithAman!")




    # variable #
# name = "Aman kumar jha"
# age = 21
# price =123.33
# print(name)
# print(age)
# print(price)



     #Data Types #

# name = "Aman kumar jha"
# age = 21
# price = 123.33
# old = True
# a = None
# print(type(name))
# print(type(age))
# print(type(price))
# print(type(old))
# print(type(a))




# #Sum of two number
# a = 1
# b = 2
# sum = a+b
# print(sum)



#       #Comment in python#
# #single line comment
# print("HelloWOrld!")
# """
# This is multi
# line comment
# """



##    OPERATORS   ##

# ##  1.)Arithmetic Operator (+,-,*,/,%,**) ##

# a = 5
# b = 2
# sum = a+b
# diff = a-b
# pro = a*b
# div = a/b
# mod = a%b
# power = a**b
# print(sum)
# print(diff)
# print(pro)
# print(div)
# print(mod) # % means give remainder
# print(power) # ** means a power b (a^b)


# ##  2.)Relational/Comparison Operator (== , != , > , < , >= , <= ) #

# a = 50
# b = 20

# print(a == b) #False
# print(a != b) #True
# print(a > b)  #True
# print(a < b)  #False
# print(a >= b) #True
# print(a <= b) #False



##   3.)Assignment Operator (= , += , -= , *= , /= , %= , **=)  ##
num = 10

# num = num + 10 # num + 10 = 11 + 10 = 21
# print("num",num )

# num += 5
# print("num",num )

# num -= 5
# print("num",num )

# num *= 5
# print("num",num )

# num /= 5
# print("num",num )

# num %= 5
# print("num",num )

# num **= 2
# print("num",num )



##   4.)Logical Operator(not , and , or) ##

#    For not operator:-NOT operator reverses the value.

# a = 1
# b = 2
# print(not (a > b)) 
# print(not (a < b)) 

# #   For and operator(A^B):-AND gives True only when both A and B are True.

# val1 = True
# val2 = True
# print("and operator is" , val1 and val2)
# val3 = True
# val4= False
# print("and operator is" , val3 and val4)
# val5 = False
# val6 = True
# print("and operator is" , val5 and val6)
# val7 = False
# val8 = False
# print("and operator is" , val7 and val8)
# print("Simple meaning Both Must be True ")
# # print("and operator is" , val1 and val2)
# # print("and operator is" , val1 and val2)
# # print("and operator is" , val1 and val2)
# print("and operator is" , val7 and val8)
# print("Simple meaning Both Must be True ")



# #   For or operator:-OR gives True when at least one of A or B is True.

# val1 = True
# val2 = True
# print("or operator is" , val1 or val2)
# val3 = True
# val4= False
# print("or operator is" , val3 or val4)
# val5 = False
# val6 = True
# print("or operator is" , val5 or val6)
# val7 = False
# val8 = False
# print("or operator is" , val7 or val8)
# print("Simple meaning Atleast one Must be True ")
# # print("OR operator is" , val1 or val2)
# # print("OR operator is" , val1 or val2)
# # print("OR operator is" , val1 or val2)
# # print("OR operator is" , val7 or val8)
# # print("Simple meaning At least one Must be True ")



###     TYPE CONVERSION   ###
###Type conversion means changing the data type of a value from one type to another.
### Type Conversion can be automatic
#When Python automatically changes one compatible data type into another, it is called implicit type conversion.

# a = 1
# b = 2.33
# sum = a + b
# print(sum)
# #output = 3.33

# ##   EROR   ##
# a = "2"
# b = 1.33
# sum = a + b
# print(sum)



###    Type Casting   ###

### Type casting means explicitly changing a value from one data type to another data type ###
### Type casting is NOT automatic. It is explicit (manual).

### Why do we need Type Casting?
# Sometimes the data we receive is in the wrong data type for the operation we want to perform.

# Rule to Write Type Casting in Python
# The basic syntax/rule is:-
# new_variable = data_type(value)

###   Example - 1 :-   ###

# a =int("2")
# b = 1.33
# sum = a + b
# print(sum)



###   Input in Python   ###
#input( ) statement is used to accept values (using keyboard) from user
# input( )  #result for input( ) is always a str
# int ( input( ) )  #int
# float ( input( ) )   #float

#Example 1
# input("Enter your name :- ")

#Example 2
# name = input("Enter your name :- ")
# print("Wel-Come" , name)

#Example 3
# val = input("Enter some value :-")
# print(type(val),val)

#Output = Enter some value :-Aman
#<class 'str'> Aman

# val = input("Enter some value :-")
# print(type(val),val)
#  Output
# Enter some value :-21
# <class 'str'> 21

#Example
# val = int(input("Enter some value :-"))
# print(type(val),val)
# #    OutPut
# Enter some value :-21
# <class 'int'> 21


# val = input("Enter some value :-")
# print(type(val),val)