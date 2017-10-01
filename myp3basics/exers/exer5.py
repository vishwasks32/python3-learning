#!/usr/bin/env python3
#
# Author : Vishwas K Singh
# Email : vishwasks32@gmail.com
#

def iseven(num):
        if num%2 == 0:
                return True
        else:
                return False

if __name__ == '__main__':
        # Direct Conversion program fails if anything other than number is 
        # Entered
        inp_num = float(input('Enter the number: '))
        if iseven(inp_num):
                print('The number is even')
        else:
                print('The number is odd')
