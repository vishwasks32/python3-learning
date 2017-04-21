#!/usr/bin/env python3.6

#Author: Vishwas K Singh
#Email: vishwasks32@gmail.com
# Program: Sequence Membersip Example
#          Listing2.4

#Check a user name and PINcode

database = [
				['albert', '1234'],
				['dilbert', '4242'],
				['smith', '7524'],
				['jones', '9843']
			]

username = input('User name: ')
pin = input('PIN code: ')
# For correct working please insert the else part
if [username,pin] in database:
		print('Access granted')
