#!/usr/bin/env python3.6                           
                                                   
#Author: Vishwas K Singh                           
#Email: vishwasks32@gmail.com                      
# Program: Simple Script that counts the words in sys.stdin
#          Listing11.1                         
# somescript.py

import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print('WordCount: ', wordcount)
