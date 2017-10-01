#!/usr/bin/env python3
#
# Author : Vishwas K Singh
# Email : vishwasks32@gmail.com
#
# Script to convert Celcius to Farenheit and vice versa
# Formula F = (C x 9/5) + 32
#         C = (F - 32) x 5/9

import os
import sys

os.system('clear')
print("Menu: ")
print("1. Celcius to Farenheit")
print("2. Farenheit to Celcius")
print("q to Quit")

while True:
        chice = input("Enter Choice(1/2/q): ")
        if chice == '1':
                chic_num = 1
        elif chice == '2':
                chic_num = 2
        elif chice == 'q':
                sys.exit(0)
        else:
                print("Invalid Input")

        if chic_num == 1:
                celci = float(input("Enter value in degree celcius: "))
                Fheit = (celci * (9 /5)) + 32
                print("%.2f  degree celcius is %.2f  degree farenheit"%(celci,Fheit))
        elif chic_num == 2:
                Fheit = float(input("Enter value in degree farenheit: "))
                celci = (Fheit - 32 ) * (5/9)
                print("%.2f  degree farenheit is %.2f  degree celcius"%(Fheit,celci))



