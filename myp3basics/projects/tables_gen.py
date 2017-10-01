#!/usr/bin/env python3
#
# Author : Vishwas K Singh
# Email : vishwasks32@gmail.com
#
# Script to Generate Tables
def sqre_gen(n):
        return pow(n,2)

def cube_gen(n):
        return pow(n,3)

def tab_gen(n):
        opt_lst = []
        for i in range(1,11):
                opt_lst.append(i*n)

        return opt_lst


if __name__ == '__main__':
        num = int(input('Enter the Number: '))
        opts = tab_gen(num)
        for i in range(1,11):
                print(str(num) + ' x ' + str(i)+ ' = ' + str(opts[i-1]))

        print()
        print('square of number is : %s'%(sqre_gen(num)))
        print('cube of number is : %s'%(cube_gen(num)))
