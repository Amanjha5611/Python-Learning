#Loops are uded when we want to run the same code multiple times.

##EXAMPLE:-

"""
Q.)Print number from 1 to 5?
ANS-> (1.) Without a loop , we write many print() statements.
      (2.)Wtih loop we write the logic once and Python repeats it.
"""


"""
1.)for loop
"""

"""SYNTAX:->
             for variable in sequence :
                 # statement/code to execute/some work
"""

"""Explanation """
# 1.  A  for  loop is used to repeat code over a sequence. 
# 2.  A sequence can be a string, range, list, tuple, etc. 
# 3.  In each round, Python takes one value from the sequence. 
# 4.  The loop stops automatically when all values are finished.


"""Flow chart"""
    #    ┌─────────────┐
    #    │    START    │
    #    └──────┬──────┘
    #           ↓
    #    ┌─────────────┐
    #    │  i = 1      │
    #    └──────┬──────┘
    #           ↓
    #    ┌─────────────┐
    #    │  i <= 5 ?   │
    #    └──────┬──────┘
    #       Yes │   │ No
    #           ↓   ↓
    #    ┌─────────┐  ┌─────────┐
    #    │ print(i)│  │   STOP  │
    #    └────┬────┘  └─────────┘
    #         ↓
    #    ┌─────────┐
    #    │  i += 1 │
    #    └────┬────┘
    #         │
    #         └──────────→ back to
    #                      i <= 5?


"""... Example 1: Loop with  range() ..."""
from doctest import Example


for i in range(1, 6):
    print(i)


"""...Example 2: Loop through a string..."""

words = "Aman"

for letter in words:
    print(letter)

#example 3 :->

nums = [1, 2, 3, 4, 5]

for el in nums:
    print(el)


##example 4 :-> 
vegetables = ["potato", "tomato", "onion", "carrot"]
for val in vegetables:
    print(val)


#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#



"""
2.)while Loop 
"""

"""SYNTAX:->
while condition:
    # statements , Some work
"""

"""EXPLANATION"""
#1.)A while loop runs as long as the condition is true.
#2.)Before every round Python checks the condition.
#3.)if the condition is True , the loop block runs.
#4.)if the condition is False , the loop stops.

"""Flow chart"""
    #    ┌─────────────┐
    #    │    START    │
    #    └──────┬──────┘
    #           ↓
    #    ┌─────────────┐
    #    │  i = 1      │
    #    └──────┬──────┘
    #           ↓
    #    ┌─────────────┐
    #    │  i <= 5 ?   │
    #    └──────┬──────┘
    #       Yes │   │ No
    #           ↓   ↓
    #    ┌─────────┐  ┌─────────┐
    #    │ print(i)│  │   STOP  │
    #    └────┬────┘  └─────────┘
    #         ↓
    #    ┌─────────┐
    #    │  i += 1 │
    #    └────┬────┘
    #         │
    #         └──────────→ back to
    #                      i <= 5?



count = 1
while count <= 5:
    print("Hello ")
    count += 1

print("Now count is :", count)


i = 1 
while i <= 108:
    print(i ,"HAR HAR MAHADEV")
    i += 1

print("Now i is :", i)


""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""



"""break statement in python"""

#  Explanation 
#  1.  break  is used to stop a loop immediately. 
#  2.  When Python sees  break  , it exits the loop. 
#  3.  Code after the loop continues normally. 
"""
Syntax:->
break
"""


# #Example 1:-> Stop the loop when i is 3

for numbers in range(1,8):
    if numbers == 4:
        break
    print(numbers)
##Output: 
# 1 
# 2 
# 3 
# Explanation: 
#  1.  The loop starts from  1  . 
#2.  When  number  becomes  4  ,  break  runs. 
# 3.  The loop stops before printing  4  . 



# Example 2:->

i = 1
while i<= 109:
    print(i , "HAR HAR MAHADEV")
    if i == 108:
        break
    i += 1

""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""



"""continue statement in python"""

""" Syntax :->
continue
"""
# #  Explanation 
# #  1.  continue  skips the current round of the loop. 
# #  2.  It does not stop the full loop. 
# #  3.  After  continue  , Python moves to the next round. 

#Example 1:-> Skip the number 3.
for i in range(1,6):
    if i == 3:
        continue
    print(i)

# # Output: 
# ##  1 
# ##  2 
# ##  4 
# ##  5 
# ##  Explanation: 
# ##  1.  When number is 3, continue runs. 
# ##  2.  print(number) is skipped for 3. 
# ##  3.  The loop continues with 4 and 5. 


""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

"""
pass statement in python
Pass is a null statement in python. It is used as a placeholder for future code.
When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.

 pass  means “do nothing”. It is used when Python needs  a statement, but we do not 
 want to write logic yet. It does not stop or skip the loop like  break  or  continue.
"""
#Syntax:-> 
#pass

## Example 1:->
for i in range(1 , 4):
    pass
# Output:  No output appears because  pass  does nothing. 

## Example 2:-> Placeholder inside condition.
for i in range(1 , 4):
    if i == 2:
        pass
    print(i)

"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

"""
else  with Loops 
"""

# Explanation 
# 1.  A loop can have an  else  block. The  else  block runs  when the loop finishes normally. 
# 2.  If the loop stops because of  break , the  else  block  does not run.

##::::::::::::::::::::::::::::::::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


"""
range()
range() is used to generate a sequence of numbers, mainly with for loops
Range function retruns a sequence of numbers starting from 0 by default,
and increments by 1 (by default), and stops before a specified number.
range(start?,stop?,step?)
"""

"""
Syntax:->
range(stop)
range(start, stop)
range(start, stop, step)
"""


# Explanation 
# 1.  range()  creates a sequence of numbers. 
# 2.  It is commonly used with  for  loops. 
# 3.  The stop value is excluded. 
# 4.  step  controls the gap between numbers. 


##Example 1:-> range(stop)
for numbers in range(5):
    print(numbers)
#  Output: 
#  0 
#  1 
#  2 
#  3 
#  4 
#  Explanation: 
#  1.  range(5)  starts from  0. 
#  2.  It stops before  5. 

# example 2:-> range(Start, stop)
for i in range(1, 6):
    print(i)

# Output: 
#  1 
#  2 
#  3 
#  4 
#  5 

#Example 3:-> range(start, stop, step)
for numbers in range(2, 11, 2):
    print(numbers)

# Output: 
# 2 
# 4 
# 6 
#  8 
#  10 
