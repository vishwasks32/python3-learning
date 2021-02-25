#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwasks32@gmail.com
# Script to right justify a text
#
import os
def right_justify(inp_txt):
    sze = os.get_terminal_size()
    return ' '*(sze[0] - len(inp_txt))+inp_txt

if __name__ == '__main__':
    inp_txt = input('Enter the text to be right justified: ')
    jstifd_txt = right_justify(inp_txt)
    print(jstifd_txt)
