#!/usr/bin/env python3
#
# Author: Vishwas K Singh
# Email: vishwasks32@gmail.com

def isPerfectSquare(num):
        for i in range(1,num):
                if pow(i,2) == num:
                        return True
        return False

if __name__ == '__main__':
        inp_num = int(input('Enter an Integer: '))
        if isPerfectSquare(inp_num):
                print('It is a perfect square')
        else:
                print('It is not a perfect square')
