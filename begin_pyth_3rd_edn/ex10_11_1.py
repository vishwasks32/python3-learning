#!/usr/bin/env python3.6                           
                                                   
#Author: Vishwas K Singh                           
#Email: vishwasks32@gmail.com                      
# Program: A Program for finding the sender of an email
#          Listing10.11                         
# find_sender.py

import fileinput, re
pat = re.compile(r'[a-z\-\.]+@[a-z\-\.]+',re.IGNORECASE)
addresses = set()
for line in fileinput.input():
		for address in pat.findall(line):
				addresses.add(address)

for address in sorted(addresses):
		print(address)
