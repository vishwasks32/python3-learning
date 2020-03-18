#!/usr/bin/env python3
#
# Author: Vishwas K Singh
# Email: vishwasks32@gmail.com
# Algorithms for computing gcd

from prime_vi import prime_factors as pf

def gcd1(a,b):
    '''Euclid algorithm to compute GCD'''
    while b != 0:
        r = a%b
        a = b
        b = r

    return a

def gcd2(a,b):
    '''Consecutive integer checking'''
    t = min(a,b)
    while True:
        if a%t == 0:
            if b%t == 0:
                return t
        t -=1

def gcd3(a,b):
    '''Middle School Procedure'''
    pf1 = pf(a)
    pf2 = pf(b)
    pf1_dict = dict()
    pf2_dict = dict()

    for item in pf1:
        pf1_dict[item] = pf1_dict.get(item,0) + 1

    for itm in pf2:
        pf2_dict[itm] = pf2_dict.get(itm,0) + 1

    nw_dict = dict()
    for key in pf1_dict.keys():
        if key in pf2_dict.keys():
            nw_dict[key] = min(pf1_dict[key],pf2_dict[key])


    num_gcd = 1
    for (k,v) in nw_dict.items():
        num_gcd *= pow(k,v) 

    return num_gcd

if __name__ == '__main__':
    num1 = int(input("Enter the First Number: "))
    num2 = int(input("Enter the Second Number: "))

    res1 = gcd1(num1,num2)
    res2 = gcd2(num1,num2)
    res3 = gcd3(num1,num2)
    print("Euclid's Algorithm: ")
    print("GCD of %d and %d is %d"%(num1,num2,res1))
    print("Consecutive Integer Checking: ")
    print("GCD of %d and %d is %d"%(num1,num2,res2))
    print("Middle School Procedure: ")
    print("GCD of %d and %d is %d"%(num1,num2,res3))
