#!/usr/bin/env python3
#
# Author: Vishwas k Singh
# Email: vishwasks32@gmail.com
# Script to swap two numbers in different locations
# Without using temp variable

def swap(num1,num2):
    num2 = num1 + num2
    if num2 > num1:
        num1 = num2 - num1
        num2 = num2 - num1
    else:
        num1 = num1 - num2
        num2 = num1 - num2

    return (num1,num2)

if __name__ == '__main__':
    num1 = int(input('Enter the First Number(Location A): '))
    num2 = int(input('Enter the second Number(Location B): '))

    (num1,num2) = swap(num1,num2)
    print("The number in Location A is %d"%(num1))
    print("The number in Location B is %d"%(num2))


