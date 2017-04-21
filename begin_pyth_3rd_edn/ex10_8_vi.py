#!/usr/bin/env python3.6                           
                                                   
# Author: Vishwas K Singh                           
# Email: vishwasks32@gmail.com                      
# Program: A simple database example
#          Listing10.8 (modified)                      
# database.py

import sys,shelve

def store_person(db):
		"""
		Query user fro data and store it
		in the shelf object
		"""

		pid = input("Enter unique ID number: ")
		person = {}
		person['name'] = input("Enter name: ")
		person['age'] = input('Enter age: ')
		person['phone'] = input('Enter the phone number: ')
		db[pid] = person

def lookup_person(db):
		"""
		Query for ID and desired field, and fetch the 
		corresponding data from the shelf object
		"""
		pid = input('Enter ID number: ')
		field = input('What would you like to know? (name, age, phone)')
		field = field.strip().lower()

		print(field.capitalize() + ':', db[pid][field])

def print_help():
		print('The available commands are: ')
		print('store  (s): Stores information about a person')
		print('lookup (l): Looks up a person from ID number')
		print('quit   (q): Saves changes and exit')
		print('help   (h): Prints this message')


def enter_command():
		cmd = input('enter command (h for help): ')
		cmd = cmd.strip().lower()
		return cmd

def main():
		database = shelve.open('database.dat') # You may want to 
		                                       # change this name

		try:
				while True:
						cmd = enter_command()
						if cmd == 'store' or cmd == 's':
								store_person(database)
						elif cmd == 'lookup' or cmd == 'l':
								lookup_person(database)
						elif cmd == 'help' or cmd == 'h':
								print_help()
						elif cmd == 'quit' or cmd == 'q':
								return

		finally:
				database.close()

if __name__ == '__main__':
		main()

