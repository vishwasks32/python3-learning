#!/usr/bin/env python3
#
# Author : Vishwas K Singh
# Email : vishwasks32@gmail.com

class user:
        ''' A class for user in address book '''
        mob = ''
        email = ''
        address = ''

        def __init__(self,name,mob,email,address):
                self.name = name
                self.mob = mob
                self.email = email
                self.address = address

        def getname(self):
                return self.name

        def getmob(self):
                return self.mob

        def getemail(self):
                return self.email

        def getaddress(self):
                return self.address

        def setmob(self,mob):
                self.mob = mob

        def setemail(self,email):
                self.email = email

        def setemail(self,email):
                self.email = email

        def setaddress(self,address):
                self.address = address

