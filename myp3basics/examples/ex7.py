#!/usr/bin/env python3
#
# Author : Vishwas K Singh
# Email: vishwasks32@gmail.com
#

# To open a file
hndle = open("prjct3.txt", mode='r')

# Read all contents of the file to dat1
dat1 = hndle.read()

for eachLine in dat1:
        print(eachLine)

hndle.close()
