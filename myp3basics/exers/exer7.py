#!/usr/bin/env python3
#
# Author : Vishwas K Singh
# Email : vishwasks32@gmail.com

def isPrime(num):
        for i in range(2,num):
                if num%i == 0:
                        return False

        return True

if __name__ == '__main__':
        inp_num = int(input('Enter an integer: '))
        if isPrime(inp_num):
                print("Integer is Prime")
        else:
                print("Integer is not prime")
