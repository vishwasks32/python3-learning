#!/usr/bin/env python3
#
# Author : Vishwas K Singh
# Email : vishwasks32@gmail.com

# Script to demonstrate use of list comprehensions

import random

# Generate all even numbers under 22
print([2*x for x in range(22)])

# Print a list of two tuples
print([(x,x) for x in (2,3,4,5)])

# Print a list of 10 random numbers
print([random.random() for x in range(10)])
