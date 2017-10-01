#!/usr/bin/env python3
#
# Author : Vishwas K Singh
# Email : vishwasks32@gmail.com
# 
# Script to reverse a string

inp_str = str(input('Enter the string to be reversed: '))

k = ''
for i in range(len(inp_str)-1,-1,-1):
        k += inp_str[i]

print("Reversed String is : %s"%(k))

