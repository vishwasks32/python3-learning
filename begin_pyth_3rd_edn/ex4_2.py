#!/usr/bin/env python3.6

#Author: Vishwas K Singh
#Email: vishwasks32@gmail.com
# Program: Dictionary method Example
#          Listing4.2

# A simple database using get()

# Insert database (people) from ex4_1
people = {
				'Alice':{
						'phone': '2341',
						'addr': 'Foo drive 23'
						},
				'Beth': {
						'phone': '9102',
						'addr': 'Bar street 42'
						},
				'Cecil':{
						'phone': '3158',
						'addr': 'Baz avenue 90'
						}
				}

labels = {
				'phone': 'phone number',
				'addr': 'address'
		 }

print('=' * 80)
name = input('Name: ')

# Are we looking for a phone number or an address?
request = input('Phone number (p) or address (a)?')

# user the correct key:
if request == 'p':
		key = 'phone'
if request == 'a':
		key = 'addr'

# Use get to provide default values:
person = people.get(name, {})
label = labels.get(key,key)
result = person.get(key,'not available')

print("{}'s {} is {}.".format(name, label,result))
print('=' * 80)
