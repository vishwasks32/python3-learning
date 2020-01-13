#!/usr/bin/env python3
#
# Author: Vishwas K Singh
# Email: vishwasks32@gmail.com
#
# Script to Program to calculate Simple Interest

principal_amt = float(input("Enter the Principal amount: "))
tym = float(input("Enter the tenure: "))
rate_of_interest = float(input("Enter the rate of interest: "))

simple_interest = (principal_amt * tym * rate_of_interest)/100

print("The Simple interest is %.2f"%(simple_interest))
