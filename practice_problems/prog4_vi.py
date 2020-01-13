#!/usr/bin/env python3
#
# Author: Vishwas K Singh
# Email: vishwasks32@gmail.com
#
# Script to convert Celcius Temperature to Farenheit
def temp_conv(temp_type, temp_val):
    ''' Function to convert Temperature from Celcius to farenheit
        and vice versa'''
    if(temp_type == 'f'):
        temp_faren = ((9/5)*temp_val) + 32
        return temp_faren

    elif(temp_type == 'c'):
        temp_cel = (5*(temp_val - 32))/9
        return temp_cel

if __name__=='__main__':
    print("Welcome to Temperature Converter")
    print("Select 1. Farenheit to Celcius\n\t2. Celcius to Farenheit")
    conv_type = input()
    if conv_type == '1':
        temp_type = 'c'
        temp_val = float(input("Enter the farenheit value to be converted: "))
        temp_celcius = temp_conv(temp_type,temp_val)
        print("%.2f degree farenheit converts to %.2f degree celcius."%(temp_val, temp_celcius))
    elif conv_type == '2':
        temp_type = 'f'
        temp_val = float(input("Enter the Celcius value to be converted: "))
        temp_farenheit = temp_conv(temp_type,temp_val)
        print("%.2f degree celcius converts to %.2f degree farenheit."%(temp_val, temp_farenheit))
    else:
        print("Invalid Input!! Exit..")

