#!/usr/bin/env python3.6

#Author: Vishwas K Singh
#Email: vishwasks32@gmail.com
# Program: Reversing and printing Command-line arguments
#          Listing10.5
# reverseargs.py

import sys
args = sys.argv[1:]
args.reverse()
print(' '.join(args))
