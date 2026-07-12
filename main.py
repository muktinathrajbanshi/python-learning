# print("Hello World")
#
# print("Hello" " World")
#
# print("""Hello
# World
# Hi There""")
import math
import token
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
# a = 10
# b = 5
# c = a * b
# print(c)
# 1.4 Division                  /
# a = 10
# b = 5
# c = a / b
# print(c)
# 1.5 Modulus                   %
# a = 11
# b = 5
# c = a % b
# print(c)
# 1.6 Exponentiation            **
# a = 5
# b = 3
# c = a ** b
# print(c)
# 1.7 Floor division             //
# a = 17
# b = 3
# c = a // b
# print(c)

# Operators Precedence
# 2+2*2      2+2*2
# 4*2        2+4
# 8           6
# () > ** > *,/ > % > +,-
# PEMDAS/BOOMAS
# print(2+2*2)
# print(4+6*(2+3-1)/4)

# Math Module
# 1. Representation:
# 1.1 math.pi
import math
from xml.sax.handler import DTDHandler

# print(math.pi)
# 1.2 math.e
# print(math.e)

# 1.3 math.tau
# print(math.tau)

# 2. Basic Maths:
# 2.1 math.pow()
# print(math.pow(2, 3))

# 2.2 math.sqrt()
# print(math.sqrt(25))

# 2.3 math.ceil()
# x = 25.64
# print(math.ceil(x))

# 2.3 math.floor()
# x = 25.64
# print(math.floor(x))

# 2.4 math.gcd()
# print(math.gcd(48, 60))

# 3. Angle Conversions:
# 3.1 math.degree()
# import math
# print(math.degrees(math.pi/6))
# 3.2 math.radians()
# import math
# print(math.radians(30))
# print(math.pi/6)
# 4. Trigonometric:
# 4.1 math.sin()
# import math
# print(math.sin(math.pi/6))

# 4.2 math.cos()
# import math
# print(math.cos(math.pi/6))
# 4.3 math.tan()
# import math
# print(math.tan(math.pi/4))
# 5. Logarithmic:
# 5.1 math.log()
# import math
# print(math.log(10))

# 5.2 math.log10()
# import math
# print(math.log10(100000))

# x = -55.46

# print(round(x))
# print(abs(x))

# Conditional Statements
# 4.1 if Statements
# age = 22
#
# if age>18:
#     print("Yes You can vote")
#     print("Yes You can vote")
#     print("Yes You can vote")
#     print("Yes You can vote")
#
# if age<=18:
#     print("go study")
#     print("go study")
# print("go study")

# 4.2 if-else Statements
# age = 18
#
# if age>18:
#     print("Yes You can vote")
#     print("Yes You can vote")
#     print("Yes You can vote")
#     print("Yes You can vote")
#
# else:
#     print("go study")

# 4.3 if-elif-else Statements
# age = 18
#
# if age>18:
#     print("Yes You can vote")
#     print("Yes You can vote")
#     print("Yes You can vote")
#     print("Yes You can vote")
#
# elif age==18:
#     print("Go apply for id card")
#     print("Go apply for id card")
#     print("Go apply for id card")
#
# else:
#     print("go study")
# 4.4 Nested ladders
# age = 19
# citizenship = True
#
# if age>18:
#     if citizenship:
#         print("Yes You can vote")
#         print("Yes You can vote")
#         print("Yes You can vote")
#         print("Yes You can vote")
#     else:
#         print("You are not a valid user")
#
# elif age==18:
#     print("Go apply for id card")
#     print("Go apply for id card")
#     print("Go apply for id card")
#
# else:
#     print("go study")

# Comparison Operators
# 5.1 Equals
# x = 5
# y = 7
# print(x==y)

# 5.2 Not equal
# x = 5
# y = 7
# print(x!=y)

# 5.3 Greater than
# x = 5
# y = 7
# print(x>y)
# 5.4 Less than
# x = 5
# y = 7
# print(x<y)
# 5.5 Greater than or equal to
# x = 5
# y = 7
# print(x>=y)
# 5.6 Less than or equal to
# x = 5
# y = 7
# print(x<=y)

# Logical Operators
# 6.1 And Operator
# x=4
# y=7
# if x==5 and y==7:
#     print("yes")
# 6.2 Or Operator
# x=4
# y=7
# if x==5 or y==7:
#     print("yes")
# 6.3 Not Operator
# x=5
# y=6
# if x==5 and not y==7:
#     print("yes")
# x=4
# y=6
# if x!=5:
#     print("yes")

# Loops
# 7.1 For Loops
# nums = [54, 23, 876, 133, 45]
# for i in nums:
#     print(i)
# 7.2 While Loops
# x = 5
# while x < 10:
#     print("hi")
#     x=x+1
# 7.3 Nested Loops
# x = 7
# while x < 10:
#     for i in range(x):
#         print(x)
#     x=x+1

# Loop Control
# 7.1.1 Break
# x = 7
# while x < 10:
#     for i in range(x):
#         print(x)
#     break
#     x=x+1
#     print("Terminated")
# 7.1.2 Continue
# for i in range(10):
#     if i==5:
#         continue
#         print("hi there")
#     else:
#         print(i)
# 7.1.3 Pass
# for i in range(10):
#     if i==5:
#         pass
#     else:
#         print(i)

# 1-minute Exercise
# Print the Pattern by taking User Input
# Sample Input:
#          5
# Sample Output:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# n = int(input("Enter any number: "))
#
# for i in range(n):
#     for j in range(1, n-i+1):
#         print(j, end=" ")
#     print("")

# Lists
# list = [5, 5.7, "Str", True, ["a", "b", "c"]]
#
# print(list[4][1])

# 8.1 2D Lists
list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# print(list[-2:-1])
# print(list[1][1])
# print(list)
# print(list[2][0])
# list[2][0] = 143
# print(list)

# 8.2 Range
# range(5, 10)
# range(5)

# 8.3 Sets
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6}

# set1.update(set2)
# print(set1)
# print(set1[0])
# set1.add(8)
# set1.add(5)
# set1.add(0)
# set1.remove(2)

# print(set1)


# 8.4 Tuples
# tpl1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# tpl2 = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")

# tpl = tpl1 + tpl2
# print(tpl)
# print(tpl[0])
# print(tpl[:5])
# print(tpl[5:])

# List Methods:
# append(): Adds an element at the end of the list
# clear(): Removes all the elements from the list
# count(): Returns the number of elements with the specified value
# extend(): Add the elements of a list (or any iterable), to the end of the current list
# index(): Returns the index of the first element with the specified value
# insert(): Adds an element at the specified position
# pop(): Removes the element at the specified position
# remove(): Removes the first item with the specified value
# reverse(): Reverses the order of the list
# sort(): Sorts the list





