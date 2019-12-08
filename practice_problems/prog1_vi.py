#!/usr/bin/env python3
#
# Author: Vishwas K Singh
# Email: vishwasks32@gmail.com
#
# Script to Program to find Sum, Diff, Prod, Avg, Div

num1 = input("Enter the first Number: ")
num2 = input("Enter the second Number: ")

# Check if the user has entered the number itself
try:
    # Convert the numbers to double always, which would handle integers 
    # and also floating point numbers
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("The entered input is not a number")
    exit(0)
except TypeError:
    print("The entered input is not a number")
    exit(0)
# Perform operation on numbers
# Sum
print("Sum of the two Numbers is: %.2f"%(num1+num2))
# Difference - always will positive
print("Difference of two numbers is: %.2f"%(abs(num1-num2)))
# average 
print("Average of two numbers is: %.2f"%((num1+num2)/2))
# product
print("Product of the two numbers is %.2f"%(num1*num2))
# division
if num2 == 0:
    print("Cannot perform division as second number is zero")
else:
    print("Division of the two numbers is %.2f"%(num1/num2))
