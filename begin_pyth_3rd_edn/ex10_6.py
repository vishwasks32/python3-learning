#!/usr/bin/env python3.6                           
                                                   
#Author: Vishwas K Singh                           
#Email: vishwasks32@gmail.com                      
# Program: Adding line numbers to a python script  
#          Listing10.6                             
# numberlines.py                                  
                                                 
import fileinput                                
                                               
for line in fileinput.input(inplace=True):         
		line = line.rstrip()                      
		num = fileinput.lineno()                 
		print('{:<50} # {:2d}'.format(line,num))
