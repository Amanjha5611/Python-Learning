#       ###  String Functions / Methods — Concept   ###

str = "I am a coder."  #We can perform different operations on this string.



#**********************************************************
#    ***  1.) endswith() :-> Checking the ending   ********
#**********************************************************



#    #Concept :-
#     ----------
#             # endswith() checks whether a string ends with a particular word or character.
#   #Syntax
#    -------
# str.endswith("substring")

# What is a Substring?
# A substring is a small part of a string.
# In simple words:
# Substring = a part of a string
# Example
# text = "I am a coder."
# The following are substrings:
# "I"
# "am"
# "a"
# "coder"
# "cod"
# "oder"
# "am a"
# Because all of them are parts of the original string.

#.................................
##.......## Example 1. ##........
#.................................

print(str.endswith("er.")) #Output :- True because "I am a coder. end with er so output is True"



#.................................
##.......## Example 2. ##........
#.................................


print(str.endswith("ing")) # Output :- False because "I am a coder. Doesnot end with ing so the output is False"

#....................................................................................................................................
#....................................................................................................................................
#************************************************************************************************************************************







##       *******************************
##       ******  2. capitalize()  ******
##       *******************************



# Concept:-
# capitalize() makes the first character of the string uppercase and converts the remaining characters to lowercase.

#...........................................
#..................EXAMPLE 1 ...............
#...........................................

str = "i am a coder."
print(str.capitalize()) #Output is I am a coder.


#...........................................
#..................EXAMPLE 2 ...............
#...........................................

str = "HELLO AMAN"
print(str.capitalize()) # Output :- Hello aman











##       ...............................
##       ...***  3. replace()  ***...
##       ...............................


# replace() → Replace old text with new text
# Concept:-
#         replace() is used to replace one word/character with another.

# Syntax:-
#         str.replace(old, new)


#...........................................
#..................EXAMPLE 1 ...............
#...........................................

str = "I am a coder."
print(str.replace("coder", "student")) # Output :- I am a student.

#........... Here:-...........
# ............old → coder...........
# ..........new → student...........



#...........................................
#..................EXAMPLE 2 ...............
#...........................................

str = "apple apple apple"
print(str.replace("apple", "mango")) #Output: mango mango mango







##       ...............................
##       ...***  4. find()  ***...
##       ...............................


# find() → Find the first index

# Concept
# find() searches for a word/substring and returns the index of its first occurrence.



# #...........................................
# #..................EXAMPLE 1 ...............
# #...........................................


str = "I am a coder."
print(str.find("am"))









#       ...............................
#       ...***  5. count() ***...
#       ...............................


# Concept:-
# count() counts how many times a character or substring appears in a string.


# #...........................................
# #..................EXAMPLE 1 ...............
# #...........................................


str = "I am a coder."
print(str.count("am")) # Output :- 




# #...........................................
# #..................EXAMPLE 1 ...............
# #...........................................


str = "banana"
print(str.count("a")) # Output :- 3