#!/usr/bin/env python3
#
# Author: Vishwas K Singh
# Email: vishwasks32@gmail.com
#
# Script to swap two numbers

num1 = int(input("Enter the number in location A: "))
num2 = int(input("Enter the number in location B: "))

temp = num1
num1 = num2
num2 = temp

print("The numbers in locations A: %i, B: %i"%(num1,num2))
