###  String in Python   ###

# A string is data type that stores a sequence of characters (text) written inside quotes  single (' ') or double (" ") quotes..

# Syntax
# name = "Aman"

# Here:
# name → variable
# "Aman" → string

# String can contain letters, numbers, spaces, and symbols.

# # # Examples 

# # String
# text = "This is a String. We are creating it in Python."
# print(text)


# # \n → New line
# text1 = "This is a String.\nWe are creating it in Python."
# print(text1)


# # \t → Tab
# text2 = "This is a String.\tWe are creating it in Python."
# print(text2)


# # \\ → Print a backslash (\)
# text3 = "This is a String.\\We are creating it in Python."
# print(text3)


# # \' → Print a single quote (')
# text4 = "This is a String.\'We are creating it in Python."
# print(text4)


# # \" → Print a double quote (")
# text5 = "This is a String.\"We are creating it in Python."
# print(text5)


# # \b → Backspace
# text6 = "This is a String.\bWe are creating it in Python."
# print(text6)


##  Example 2 :-

# name = "Aman kumar jha"
# city = 'Bengaluru'
# college = "JAIN University"
# number = "9661488432"   # This is a string, not an integer 
# print(name)
# print(city)
# print(college)
# print(number)



###     BASIC OPERATIONS IN STRING   ###

# STRING OPERATIONS
#        │
#        ├── +       → Concatenation (join)
#        ├── *       → Repetition
#        ├── len()   → Length
#        ├── []      → Indexing
#        ├── [-]     → Negative Indexing
#        └── [:]     → Slicing





#              ###1. + → Concatenation (Join)

# Why use?
# To join two or more strings.

# Where use?
# When you want to combine separate pieces of text.

# #           ## Example ##
# first = "Aman"
# last = "Jha"

# print(first + " " + last)







#       ##2. len() → Length  ##

# Why use?
# To find how many characters are present in a string.

# Where use?
# When checking password length, username length, text size, etc.

# #      ##  Example  ##

# password = "Aman123"
# first = "Aman"
# last = "Jha"

# # 👉 Use len() when you want to COUNT characters.

# print(len(password))
# print(len(first))
# print(len(last))







# #      ##3. [] → Indexing

# #Yes. In Python, string indexing always starts from 0.

# # Why use?
# # To get one specific character from a string.

# # Where use?
# # When you need a particular character.

# # Remember:

# #  A   m   a   n
# #  0   1   2   3

# # 👉 Use [] when you want ONE character.

# name = "Aman"

# print(name[0])








# #      ##4. [:] → Slicing

# # Why use?
# # To get a part of a string, instead of just one character.

# # Where use?
# # When extracting part of a name, word, sentence, etc.

# # Rule:

# # [start : end]
# #           ↑
# #        NOT included

# # So:

# # name[0:2]

# # means:

# # Index 0 → A ✅
# # Index 1 → m ✅
# # Index 2 → a ❌

# # 👉 Use slicing when you want a PART of the string.

# name = "Aman"

# print(name[0:2])







# #     ## 5. [-] → Negative Indexing

# # Why use?
# # To access characters from the end of the string.

# # Where use?
# # Very useful when you don't want to calculate the last character's positive index.

# #  A    m    a    n
# # -4   -3   -2   -1

# # 👉 Use negative indexing when you want to access characters FROM THE END.

# #     ## Example

# name = "Aman"

# print(name[-3:-1])