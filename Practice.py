# # """
# # Q1.)
# # print numbers from 1 to 5 using while loop
# # """

i = 1 
while i <= 5 :
    print(i)
    i += 1
print("Lop is ends here...")

# # #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# # """
# # Q2.)
# # print numbers from 5 to 1 using while loop
# # """
i = 5
while i >= 1 :
    print(i)
    i -= 1
print("Lop is ends here...")

# # #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# # """
# # Q3.)
# # print numbers from 1 to 100 
# # """

i = 1 
while i <= 100:
    print(i)
    i += 1 
print ("LOOP is ends here...")

# # #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# # """
# # Q4.)
# # print numbers from 100 to 1 
# # """

i = 100
while i >= 1:
    print(i)
    i -= 1
print ("LOOP is ends here...")

# #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::



# # """
# # Q5.)
# # print the multiplication table of a number n.
# # """

n = int (input ("ENter the number for which you want to print the multiplication table:"))
i = 1
while i <= 10 :
    print(n*i)
    i += 1

# #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# # """
# # Q6.)
# # print the elements of the followint list using a whileloop.
# # [1,4,9,16,25,36,49,64,81,100]
# # """
""""          code:-            """

nums = [1,4,9,16,25,36,49,64,81,100]

index = 0
while index < len(nums): #"len() gives the count, indexing starts at 0, so the last index is len(nums) - 1. That's why we use < len(nums)."
    print(nums[index])
    index += 1


# #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# # """
# # Q7.)
# # Search for a number in x in this truple using loop:
# # (1,4,9,16,25,36,49,64,81,100)"""

"""          Code:-            """

nums = (1,4,9,16,25,36,49,64,81,100)

x = 36 

i = 0 
while i < len(nums):
    if (nums[i] == x):
        print("Number found at index:", i)
    i += 1


# #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# # """
# # Q8.)print the elements of the followint list using a for loop.
# # [1,4,9,16,25,36,49,64,81,100]
# # """

nums = [1,4,9,16,25,36,49,64,81,100]

for el in nums:
    print(el)

# # """
# # Q9.)Search for a number in x in this truple using a forloop:
# # (1,4,9,16,25,36,49,64,81,100)
# # """

nums = (1,4,9,16,25,36,49,64,81,100)
x = 25
index = 0

for el in nums:
    if el == x :
        print("Numbers found at index:", index) 
    index  += 1

# #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# # """
# # LET'S PRACTICE USING for & range()
# # """

# # """Q1.)Print numbers from 1 to 100"""

for number in range (1,101):
    print(number)



# # """Q2.)Print numbers from 100 to 1"""

for i in range (100,0,-1):
    print(i)




# # """Q3.)Print multiplication table of a """

n = int(input("Enter the number for which you want to print the multiplication table:"))

for i in range(1,11):
    print(n*i)

# ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# # """
# # LET'S PRACTICE 
# # """

# # """Q1.)WAP to find the sum of first n numbers,(Using while) """

n = int (input("Enter the number :"))

i = 1
sum = 0
while i <= n :
    sum += i
    i +=1
print("The sum of first", n , "numbers is :", sum)


# """          OR              """

# # n = int (input ("Enter the number :-> "))

i = 1
sum = 0

for i in range(1, n+1):
    sum += i

print("The sum of first", n , "numbers is :-> " , sum)



# """WAP to find the factorial of first n numbers, (using for) """

n = int(input("Enter the number :->"))

fact = 1

for i in range(1, n+1):
    fact *= i

print("The factorial of first ", n , "number is :-> ", fact)

# """        OR        """

n = int (input("Enter the number :->"))

fact = 1
i = 1

while i <= n :
    fact *= i
    i += 1

print("The factorial of first ", n , "number is :-> ", fact)