#!/usr/bin/env python3.6

#Author: Vishwas K Singh
#Email: vishwasks32@gmail.com
# Program: Slicing Example
#          Listing2.2

# Split up a URL of the form http://www.somrthing.com

url = input('Please enter the URL: ')
domain = url[11:-4]  # Not a right method, Please fine tune

print("domain name: " + domain)
