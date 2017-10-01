#!/usr/bin/env python3
#
# Author: Vishwas K Singh
# Email : vishwasks32@gmail.com
#
# A number to word converter application(1 to 10)
# version : 0.1

import os
import sys

def cnvter(num):
        cnv_dict = {'1':'one','2':'two','3':'three','4':'four','5':'five',
                    '6':'six','7':'seven','8':'eight','9':'nine','10':'ten'
                    }
        if num in cnv_dict.keys():
                return cnv_dict[num]
        elif num == 'q':
                return 0
        else :
                return 1

if __name__ == '__main__':
        if os.name == "posix":
                os.system('clear')
        elif os.name == "NT":
                os.system('cls')

        print("    My Number to Word Converter    \n")
        print(" Press q to quit \n")
        while True:
                inp_str = str(input("Enter the (Number / q): "))
                res = cnvter(inp_str)
                if res == 1:
                        print('Invalid Input')
                elif res == 0:
                        print("Program exiting")
                        sys.exit(0)
                else:
                        print("In words : %s"%(res))

