#!/usr/bin/env python3
#
# Author: Vishwas K Singh
# Email: vishwasks32@gmail.com
# To Generate all the list of prime numbers less than a number
import math

def prime_nums_list(n):
    ''' Sieve of Eratosthenes returns list of prime numbers'''
    p_list = list()
    t_list = list()

    for i in range(2,n):
        p_list.append(i)

    for i in range(2,math.ceil(math.sqrt(n)),1):
        t_list.append(i)

    k_list = p_list.copy()

    for i in range(len(t_list)):
        for j in range(len(p_list)):
            if (p_list[j] != t_list[i]) and (p_list[j] % t_list[i] == 0):
                if p_list[j] in k_list:
                    k_list.remove(p_list[j])


    return k_list

def prime_factors(n):
    ''' Prime Factor Expansion'''
    prime_factors = list()
    for d in range(2,n):
        if d*d <= n:
            while n %d == 0:
                prime_factors.append(d)
                n = int(n/d)

    if n>1:
        prime_factors.append(n)

    return prime_factors


if __name__=='__main__':
    num = int(input("Enter the number: "))
    prime_facts = prime_factors(num)
    print(prime_facts)
