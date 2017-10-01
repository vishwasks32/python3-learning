#!/usr/bin/env python3
#
# Author : Vishwas K Singh
# Email : vishwasks32@gmail.com
#

print('Display usage of for')

for i in range(10):
        print(i)

print('--'*20)
kname = 'vishwas'
for i in range(len(kname)):
        print(i, " is position of", kname[i])

print('--'*20)
for i in [1,2,3,4,5]:
        print(i)
