#!/usr/bin/env python3
# Author: Vishwas K Singh
# E-mail: vishwasks32@gmail.com
# Program to find largest subarray with largest sum using Kadane Algorithm
from sys import maxint

arr_num = input("Enter the array: ")
max_num = -maxint - 1
max_end_num = 0

for i in range(0,len(arr_num)):
    max_end_num += arr_num[i]
    if(max_num < max_end_num):
        max_num = max_end_num

    if max_end_num < 0:
        max_end_num = 0

print(max_num)
