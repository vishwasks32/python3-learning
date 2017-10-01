#!/usr/bin/env python3
#
# Author : Vishwas K Singh
# Email: vishwasks32@gmail.com

# A Calculator script
# Version 0.1

import os
import sys

def add_num(a,b):
        return a+b
def sub_num(a,b):
        return a-b
def mul_num(a,b):
        return a*b
def div_num(a,b):
        return a/b

if __name__ == '__main__':
        os.system('clear')
        print('Welcome to calculator v0.1')
        print("Menu: ")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        while True:
                chice = input('Enter The choice(1/2/3/4/5): ')
                while chice not in ['1','2','3','4','5']:
                        print("invalid choice!!")
                        chice = input('Enter The choice(1/2/3/4/5): ')

                chice = int(chice)
                if chice == 5:
                        sys.exit(0)

                num1 = float(input("Enter the First Number: "))
                num2 = float(input("Enter the Second Number: "))

                if chice == 1:
                        print(add_num(num1,num2))
                elif chice == 2:
                        print(sub_num(num1,num2))
                elif chice == 3:
                        print(mul_num(num1,num2))
                elif chice == 4:
                        if num2 != 0.0:
                                print(div_num(num1,num2))
                        else:
                                print("Invalid Number")
