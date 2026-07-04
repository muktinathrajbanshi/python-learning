# print("Hello World")
#
# print("Hello" " World")
#
# print("""Hello
# World
# Hi There""")
from xml.dom.minidom import Element

# Types of Datatypes
# 1. Numeric data types: integer, float, complex
# a = 5
# print(type(a))

# a = complex(3,5)
# print(a)
# print(type(a))

# 2. String data types : strings
# string = "I Love coding as coding is easy and coding is fun"
# print(string.lower())
# print(type(string))
# print(string.replace("World", "learners"))
# print(string.swapcase())
# print(string.capitalize())
# print(string.count("coding"))
# print(string.find("coding"))
# print(string.rfind("coding"))


# String Methods
# 2.1 islower()
# 2.2 isupper()
# 2.3 lower()
# 2.4 upper()
# 2.5 replace()
# 2.6 swapcase()
# 2.7 capitalize()
# 2.8 count()
# 2.9 find()
# 2.10 rfind()
# 2.11 Many More...

# 3. Sequence types : list, tuple, range.
# a = ["apple", "banana", "mango"]
# print(a)

# 4. Binary types : bytes, bytearray, memoryview.


# 5. Mapping data type : dictionary


# 6. Boolean type : boolean
# a = True
# b = False

# print(type(a))



# 7. Set data types : set, frozenset.



# 1-minute exericise
# Display the middlemost character of a string given as input from the User, if no middle index is present, display the
# character just after the middle index


# Sample Input:                                sample output
# Element                                          m
# MuktinathTech                                    t
# Is this aslo a string ?                          s


# s = input("Enter the String: ")
# print(s[len(s)//2])


# Types of Type-Conversion
# 1. Implicit Conversion - automatic type conversion
# a = 5
#
# print(type(a))
#
# a = 67.8
#
# print(type(a))
#
# print(a)



# 2. Explicit Conversion - manual type conversion
# a = "5"
#
# b = int(a)
# print(type(a))
#
# print(type(b))
#
# print(b)

# Formatted Strings
# a = "John"

# b = 4

# msg = a + " has " + str(b) + " cars."
# msg = f"{a} has {b} cars."

# print(f"{a} has {b} cars.")
# print(f"""{a} has
# {b} cars.""")


# Comments
# Program to display the Fibonacci sequence up to n-th term

# nterms = int(input("How many terms? "))

# first two terms
# n1, n2 = 0, 1
# count = 0

# check if the number of terms is valid
# if nterms <= 0:
#     print("Please enter a positive integer")

# if there is only one term, return n1
# elif nterms == 1:
#     print("Fibonacci sequence upto", nterms, ":")
#     print(n1)
# generate fibonacci sequence
# else:
#     print("Fibonacci sequence:")
#     while count < nterms:
#         print(n1, end=" ")
#         nth = n1 + n2
#         # update values
#         n1 = n2
#         n2 = nth
#         count += 1

# Arithmetic Operations
# 1.1 Addition                  +
# a = 10
# b = 5
# c = a + b
# print(c)

# 1.2 Subtraction               -
# a = 10
# b = 5
# c = a - b
# print(c)
# 1.3 Multiplication            *
a = 10
b = 5
c = a * b
print(c)
# 1.4 Division                  /
# 1.5 Modulus                   %
# 1.6 Exponentiation            **
# 1.7 Floor division             //