# # Q1.)
# n = int (input("Enter n :"))
# for i in range (1 , n+ 1):
#     print (i)

# #Q2.)
# def add_digits(n):
#     total = 0

#     while n > 0:
#         digit = n % 10
#         total += digit
#         n = n // 10

#     return total


# num = int(input("Enter a number: "))
# print("Sum of digits:", add_digits(num))


# # Q3.)
# def sum_square_digits(n):
#     total = 0

#     while n > 0:
#         digit = n % 10
#         total += digit ** 2
#         n = n // 10

#     return total


# num = int(input("Enter a number: "))
# print("Sum of square of digits:", sum_square_digits(num))


# # Q4.)
# def is_armstrong(n):
#     original = n
#     total = 0
#     digits = len(str(n))

#     while n > 0:
#         digit = n % 10
#         total += digit ** digits
#         n = n // 10

#     return total == original


# num = int(input("Enter a number: "))

# if is_armstrong(num):
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")