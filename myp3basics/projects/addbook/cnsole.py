#!/usr/bin/env python3
#
# Author : Vishwas K Singh
# Email : vishwasks32@gmail.com
#
# Script of console interface for addressbook application

import os
import sys
import time
from user import user as u

def display_menu():
        ''' Function to display menu '''
        os.system('clear')
        print('Welcome to address book application')
        print('--'*20)
        print('Menu:')
        print(' '*20)
        print('1. Add ')
        print('2. Edit ')
        print('3. Search ')
        print('4. View all')
        print('5. Delete ')
        print('6. Quit')
        print('--'*20)

def verify_choice(inp_str):
        ''' Function to verify Choice '''
        if inp_str not in ['1','2','3','4','5','6']:
                return False
        else:
                return True

def save_details(det_str):
        ''' Function to write details to file '''
        try:
                hndle = open('address_book.txt','a')
                hndle.write(det_str)
                hndle.close()

        except FileNotFoundError:
                print("File Does not exist")
                print("Could not save details")

def new_user():
        os.system('clear')
        print('Add User: Enter Details ')
        print('--'*20)
        name = input('Enter the name: ')
        mob = input('Enter the mobile number: ')
        email = input('Enter the email id: ')
        address = input('Enter the address: ')
        dt_st = name +','+mob+','+email+','+address+ '\n'

        print(dt_st)
        save_details(dt_st)
        print('details saved')

def read_file():
        try:
                hndle = open('address_book.txt','r')
                dat = hndle.read()
                hndle.close()
                return dat

        except FileNotFoundError:
                print("File Does not exist")
                print("Could not read details")

def get_details(nme):
        dt = read_file().split('\n')
        dt_lst = []
        for i in dt:
                if i.split(',')[0] == nme:
                        dt_lst.append(i)

        return dt_lst

def display_details(us):
        os.system('clear')
        print('Showing Details')
        print('--'*20)
        print("Name: %s"%us.getname())
        print("Mobile: %s"%us.getmob())
        print("Email: %s"%us.getemail())
        print("Address: %s"%us.getaddress())

def view_all():
        os.system('clear')
        print('Please wait while we fetch details...')
        time.sleep(1)
        dats = read_file()
        dt = read_file().split('\n')
        usr_lst = []
        for idx in range(len(dt)):
                usr = dt[idx].split(',')
                if len(usr) > 1:
                        u1 = u(usr[0],usr[1],usr[2],usr[3])
                        usr_lst.append(u1)
        
        for item in usr_lst:
                display_details(item)
                chice = input("Press enter key to next/q to exit: ")
                if chice == 'q':
                        break

def delete_details():
        os.system('Clear')
        print('Delete details')
        print('--'*20)
        dats = read_file()
        dt = read_file().split('\n')
        usr_lst = []
        for idx in range(len(dt)):
                usr = dt[idx].split(',')
                if len(usr) > 1:
                        u1 = u(usr[0],usr[1],usr[2],usr[3])
                        usr_lst.append(u1)
        
        for item in usr_lst:
                display_details(item)
                chice = input("Press enter key(y/n/q): ")
                if chice == 'y':
                        usr_lst.remove(item)
                        time.sleep(1)
                        print('User Deleted Successfully')
                        time.sleep(1)

                elif chice == 'n':
                        pass

                elif chice == 'q':
                        break

        dt_lst = []
        for itr in usr_lst:
                dt_str = itr.getname() + ','+ itr.getmob()+ ','+ itr.getemail()+','+itr.getaddress()+'\n'
                dt_lst.append(dt_str)

        k = ""
        for i in dt_lst:
                k += i

        try:
                hndle = open('address_book.txt','w')
                hndle.write(k)
                hndle.close()

        except FileNotFoundError:
                print("File Does not exist")
                print("Could not save details")

        print('user details updated')
        time.sleep(1)

def search_details():
        os.system('clear')
        print('Search Details')
        print('--'*20)
        nme = input('Enter name to search details: ')
        time.sleep(1)
        print('Please wait while we fetch details....')
        time.sleep(1)
        dets = get_details(nme)
        if len(dets)==0:
                print("Sorry No details available at moment")
                time.sleep(2)
        
        usr_lst = []
        for idx in range(len(dets)):
                usr = dets[idx].split(',')
                u1 = u(usr[0],usr[1],usr[2],usr[3])
                usr_lst.append(u1)

        for item in usr_lst:
                display_details(item)
                chice = input("Press any key to next/exit: ")

def edit_details():
        os.system('clear')
        print("Edit Details of person")
        print('--'*20)
        nme = input('Enter name of person to edit')


if __name__ == '__main__':
        while True:
                display_menu()
                chice = str(input("Enter the Choice: "))
                if verify_choice(chice):
                        chice = int(chice)
                else:
                        print("Invalid Input!!")
                        print("Please input valid choice")
                        time.sleep(3)

                if chice == 1:
                        new_user()
                        print("User added Successfully")
                        print("Please wait!Saving Details......")
                        time.sleep(5)
                elif chice == 2:
                        pass
                elif chice == 3:
                        search_details()
                elif chice == 4:
                        view_all()
                elif chice == 5:
                        delete_details()
                elif chice == 6:
                        sys.exit(0)

