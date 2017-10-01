#!/usr/bin/env python3
#
# Author : Vishwas K Singh
# Email : vishwasks32@gmail.com
#

def check_palindrome(inp_str):

        rev_str = ''
        for idx in range(len(inp_str)-1,-1,-1):
                rev_str += inp_str[idx]

        if inp_str == rev_str:
                return True
        else:
                return False


if __name__ == '__main__':

        inp_st = str(input('Enter the String: '))

        if check_palindrome(inp_st):
                print("It is a palindrome")
        else:
                print("It is not a palindrome")
