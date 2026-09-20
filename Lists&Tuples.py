# #            Lists in Python 

# #  SYNTAX:-
# # list_name = [value1 , vlaue2 , value]


# # # Example :-> 

# Student = ["Aman" , 21 , "Python" , 84.4]
# print(Student)



# #    CREATING LISTS
# #    Example :-> 1

# numbers = [10, 20, 30, 40]
# names = ["Aman", "Pratik", "Arush"]
# mixed = ["Aman", 100, 99.9, True]
# empty_list = []
# Nested_list =[[1,2],[3,4]]

# print(numbers)   #//[10, 20, 30, 40]
# print(names)     #//['Aman', 'Pratik', 'Arush']
# print(mixed)     #//['Aman', 100, 99.9, True]
# print(empty_list) #//[]
# print(Nested_list)#//[[1, 2], [3, 4]]






# ##...........ACCESSING VALUES...........##

# ##SYNTAX:-> list_name[index]

# # #    Example :-> 2

# Students = ["Aman", "Pratik", "Arush", "Sakshi"]
# print(Students[0])     ##Aman
# print(Students[1])     ##Pratik
# print(Students[-2])    ##Arush
# print(Students[-1])    ##Sakshi






# ##...........UPDATING VALUES...........##

# ##SYNTAX:-> list_name[index] = new_value

# # # #    Example :-> 3

# marks = [ 90, 89, 78]
# marks[2] = 87
# print(marks)          ##[90, 89, 87]









# ##...........List Methods ...........##

# #  Method  Purpose  Example  Result 


# # # # #    Example :-> 3

# numbers = [10, 20, 30]
# numbers.count(10)
# numbers.append(40)          ##[10, 20, 30, 40]
# numbers.extend([50,60])     ##[10, 20, 30, 40, 50, 60]
# numbers.insert(6,70)        ##[10, 20, 30, 40, 50, 60, 70]
# numbers.remove(10)          ##[20, 30, 40, 50, 60, 70]
# numbers.pop(2)              ##[20, 30, 50, 60, 70]
# numbers.index(30)           ##[20, 30, 50, 60, 70]
# numbers.sort()             ##[20, 30, 50, 60, 70]
# numbers.reverse()          ##[70, 60, 50, 40, 30, 20, 10]
# numbers.copy()             ##[70, 60, 50, 40, 30, 20, 10]

# print(numbers)





# # ##...........LIST SLICING...........##

# # #Syntax 
# # # list_name[start:end:step] 

# # #Explanation :-

# ## 1.  Slicing is used to get a part of a list. 
# ## 2.  The start index is included. 
# ## 3.  The end index is excluded. 
# ## 4.  Step controls the gap between selected items. 


# # # # #    Example :-> 4

#  #PYTHON CODE :-

# numbers = [10, 20, 30, 40, 50, 60] 
# print(numbers[1:4]) #[20, 30, 40]
# print(numbers[:3])  #[10, 20, 30]
# print(numbers[3:])  #[40, 50]
# print(numbers[::2]) # numbers[::2] meaning = [start : stop : step] [10, 30, 50]
# print(numbers[::-1]) #[60, 50, 40, 30, 20, 10]






# # ##...........List Comprehensions ...........##


# # List comprehension is a short way to create a new list using a for loop in one line.

# #List comprehension is a short and easy way to create a new list from an existing sequence.
# #We use list comprehension mainly to create a new list quickly and in fewer lines of code.

# # Syntax :- new_list = [expression for item in sequence] 

# # With condition:- new_list = [expression for item in sequence if condition] 

# # 1.  List comprehension is a short way to create a new list. 
# # 2.  It is commonly used when each item needs to be processed. 
# # 3.  It can also filter values using  if . 
# # 4.  It makes code shorter and cleaner.


# # ## # # # #    Example :-> I
# mylist = [1, 2, 3, 4, 5]
# newlist = []
# for val in mylist:
#   newlist.append(val * val)
# print(mylist)
# print(newlist)


# # Example II :-> With Condition 

# numbers = [1, 2, 3, 4, 5, 6]

# for n in numbers:
#   even_numbers = [number for number in numbers if number % 2 == 0]
# print(even_numbers)


# #     OR

# list = [1, 2, 3, 4, 5, 6]
# newlist = [] #We create an empty list. Why? Because we want to put the even numbers into this list.

# for list in list : #Take each value from numbers, one by one, and store the current value in number.
#     if(list % 2 == 0):
#         newlist.append(list) #This line runs only when the if condition is True.
# print(newlist)


# mylist = [1, 2, 3, 4, 5, 6]
# newlist = []

# for number in mylist:
#     newlist.append(number*2)
# print(newlist)


# mylist = [1, 2, 3, 4, 5, 6]
# newlist = []

# for numbers in mylist:
#     if(numbers % 2 == 0):
#         newlist.append(numbers)
# print(newlist)





# # ##...........Nested Lists  ...........##





# # A nested list is a list inside another list.

# # Syntax :- list_name = [[item1, item2], [item3, item4]] 
# # Explanation :-
# # 1.  A nested list means a list inside another list. 
# # 2.  It is useful for matrix-like data, rows and columns, or grouped values. 
# # 3.  To access nested list values, use multiple indexes. 

# # # Easy rule :-
# # list[row][column]

# ###    Example 

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     []
# ]
# ## numbers[0][1] means: first select the first inner list, then select the second value from it.
# print(matrix[0]) 
# print(matrix[1])
# print(matrix[0][0])
# print(matrix[0][1])
# print(matrix[0][2])
# print(matrix[1][0])
# print(matrix[1][1])
# print(matrix[1][2])





# # # ##...........Nested Lists  ...........##
# # # ##...........Updating Nested List Value   ...........##


# matrix = [ 
# [1, 2, 3], 
# [4, 5, 6] 
# ] 
# matrix[1][0] = 40 
# print(matrix)


