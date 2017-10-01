#!/usr/bin/env python3
#
# Author : Vishwas K Singh
# Email : vishwasks32@gmail.com
#
# Program: A Number to Words Converter Program
# Version : 1

import os
import sys

def convtr(num):

	''' Function converter
	    convtr(string) -> 0,1, num_in_words '''

	conv_dict = {
			'1':'One','2':'Two','3':'Three','4':'Four','5':'Five',
			'6':'Six','7':'Seven','8':'Eight','9':'Nine','10':'Ten',
			'11':'Eleven','12':'Twelve','13':'Thirteen','14':'Fourteen',
			'15':'Fifteen','16':'Sixteen','17':'Seventeen','18':'Eighteen',
			'19':'Nineteen','20':'Twenty'
		}

	if num == 'q':
		return 0
	elif num in conv_dict.keys():
		num_in_words = conv_dict[num]
		return num_in_words
	else:
		return 1


if __name__ == '__main__':
	os.system('clear')
	print('          My Converter v1        ')
	print('')
	print(' Note: Press q to exit ')
	print('')
	while True:
		num = input('Enter the Number : ')
		num = str(num)
		res = convtr(num)
		if res == 0:
			os.system('clear')
			sys.exit(0)
		elif res == 1:
			print('Invalid Input!!')
		else:
			print('In Words : %s'%(res))

		print('')
