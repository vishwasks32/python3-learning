#!/usr/bin/env python3.6                           
                                                   
#Author: Vishwas K Singh                           
#Email: vishwasks32@gmail.com                      
# Program: A Program for finding the sender of an email
#          Listing10.10                             
# find_sender.py

import fileinput, re
pat = re.compile('From: (.*)<.*?>$')
for line in fileinput.input():
		m = pat.match(line)
		if m:
				print(m.group(1))
