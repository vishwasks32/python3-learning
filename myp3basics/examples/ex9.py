#!/usr/bin/env python3
#
# Author : Vishwas K Singh
# Email : vishwasks32@gmail.com

class user:
        '''A class for user in address book '''
        version = 0.1
        def __init__(self,name):
                ''' A Constructor '''
                self.name = name

        def getname(self):
                ''' Returns the name of instance '''
                return self.name

        def getver(self):
                ''' Returns the version '''
                return self.version


if __name__ == '__main__':
        # Creates an instance of the class described above
        f1 = user('vishwas')
        print(f1.getname())

